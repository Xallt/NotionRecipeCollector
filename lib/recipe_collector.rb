class RecipeCollector
  def get_recipes(notion_api_key)
    recipe_list = `NOTION_API_KEY=#{notion_api_key} python print_recipes.py`.chomp
    recipe_list
  end
end