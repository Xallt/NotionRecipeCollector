class RecipeCollector
  def get_recipes(notion_api_key)
    recipe_list = `NOTION_API_KEY=#{notion_api_key} python #{File.expand_path('../../print_recipes.py', __FILE__)}`.chomp
    recipe_list
  end
end