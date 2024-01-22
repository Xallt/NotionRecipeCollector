require 'json'

class RecipeCollector
  def get_recipe_data(notion_api_key)
    output = `NOTION_API_KEY=#{notion_api_key} python #{File.expand_path('../../print_recipes.py', __FILE__)}`
    recipe_file = File.read('recipes.json')
    JSON.parse(recipe_file)
  end
end