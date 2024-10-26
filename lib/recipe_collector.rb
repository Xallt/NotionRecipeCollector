require 'json'

class RecipeCollector
  def get_recipe_data(notion_api_key)
    # Check for python command
    python_command = if system("which python > /dev/null 2>&1")
      "python"
    elsif system("which python3 > /dev/null 2>&1")
      "python3"
    else
      raise "Error: Neither 'python' nor 'python3' command found. Please install Python."
    end

    # Use the found python command
    output = `NOTION_API_KEY=#{notion_api_key} #{python_command} #{File.expand_path('../../print_recipes.py', __FILE__)}`
    
    recipe_file = File.read('recipes.json')
    JSON.parse(recipe_file)
  end
end
