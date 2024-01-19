import requests
import os

# Important to set when running locally
NOTION_API_KEY = os.environ["NOTION_API_KEY"]

# ID of the Notion "Cooking" database
COOKING_ID = "013eb25bb1444da6a8a842fba94b3f0e"

if __name__ == "__main__":
    db_data = requests.post(
        f"https://api.notion.com/v1/databases/{COOKING_ID}/query",
        headers={
            "Authorization": f"Bearer {NOTION_API_KEY}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
    ).json()

    for recipe_data in db_data["results"]:
        print(recipe_data["properties"]["Name"]["title"][0]["text"]["content"])
