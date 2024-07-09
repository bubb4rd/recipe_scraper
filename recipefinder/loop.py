import json

def filter_recipes(input_file, output_file):
  """
  Filters recipes from an input JSON file and writes recipe links to an output JSON file as a list.
  """
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    data = json.load(f_in)
    recipe_links = [recipe["recipe_link"] for recipe in data if "recipe_link" in recipe]
    json.dump(recipe_links, f_out, indent=4)

filter_recipes('cookbook.json', 'recipe_link_list.json')
def filter_categories(input_file, output_file):
  """
  Filters recipes from an input JSON file and writes recipe links to an output JSON file as a list.
  """
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    data = json.load(f_in)
    categories = [category["name"] for category in data if "name" in category]
    json.dump(categories, f_out, indent=4)
filter_categories('recipe.json', 'recipe_categories_list.json')