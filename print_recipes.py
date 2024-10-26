import requests
import os
import json

# Important to set when running locally
NOTION_API_KEY = os.environ["NOTION_API_KEY"]

# ID of the Notion "Cooking" database
COOKING_ID = "013eb25bb1444da6a8a842fba94b3f0e"


def get_db_data():
    response = requests.post(
        f"https://api.notion.com/v1/databases/{COOKING_ID}/query",
        headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
    )
    if response.status_code != 200:
        raise Exception(
            f"Failed to get database data: {response.status_code=}, {response.text=}"
        )
    db_data = response.json()
    if "results" not in db_data:
        raise Exception(f"No results found in {db_data}, {response.text=}")
    return db_data


def get_recipe_text(recipe_id):
    recipe_page_data = get_recipe_page_data(recipe_id)

    content_lines = []
    counter = 0

    for block in recipe_page_data["results"]:
        block_type = block["type"]
        if block_type not in ["paragraph", "bulleted_list_item", "numbered_list_item"]:
            print(f"WARNING: Can't handle {block_type} yet")
            continue

        block_rich_text = block[block_type]["rich_text"]
        if len(block_rich_text) == 0:
            content_lines.append("")
            continue

        if block_type == "numbered_list_item":
            counter += 1
        else:
            counter = 0

        cur_line = ""
        if block_type == "bulleted_list_item":
            cur_line += "- "
        elif block_type == "numbered_list_item":
            cur_line += f"{counter}. "
        cur_line += block_rich_text[0]["plain_text"]
        content_lines.append(cur_line)

    return "\n".join(content_lines)


def get_recipe_data(db_data):
    return [
        {
            "id": item["id"],
            "name": item["properties"]["Name"]["title"][0]["plain_text"],
            "url": item["properties"]["URL"]["url"],
        }
        for item in db_data["results"]
    ]


def get_recipe_page_data(recipe_id):
    recipe_page_data = requests.get(
        f"https://api.notion.com/v1/blocks/{recipe_id}/children",
        headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28",
        },
    ).json()
    return recipe_page_data


def get_recipe_properties(recipe_id):
    recipe_page_data = get_recipe_page_data(recipe_id)
    recipe_text = get_recipe_text(recipe_page_data)


def get_all_recipes_data(db_data):
    all_recipe_data = []
    for recipe_data in get_recipe_data(db_data):
        recipe_text = get_recipe_text(recipe_data["id"])
        all_recipe_data.append(dict(**recipe_data, text=recipe_text))
    return all_recipe_data


if __name__ == "__main__":
    db_data = get_db_data()

    all_recipe_data = get_all_recipes_data(db_data)

    with open("recipes.json", "w") as f:
        json.dump(all_recipe_data, f)
