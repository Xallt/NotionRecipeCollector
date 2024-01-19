require_relative 'lib/recipe_collector'

NOTION_API_KEY = ENV['NOTION_API_KEY']

collector = RecipeCollector.new

puts collector.get_recipes(NOTION_API_KEY)