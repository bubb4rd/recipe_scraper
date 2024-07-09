import scrapy 
import json
class RecipeFinder(scrapy.Spider):
    name = 'finder'
    start_urls = ['https://www.allrecipes.com/recipes-a-z-6735880']

    def parse(self, response):
        for category in response.css('a.type--dog-link'):
            try:
                yield {
                    'name': category.css('a.type--dog-link::text').get(),
                    'link': category.css('a.type--dog-link').attrib['href'],
                }
            except: {
            }
        with open("recipe.json") as f: 
            data = json.load(f) 
        
        # Iterate through the JSON array 
        for item in data: 
            link = item['link']
            if link is not None:
                yield response.follow(link, callback=self.parse_recipe)

    def parse_recipe(self, response):
        for recipe in response.css('a.mntl-card'):
            try:
                yield {
                    'recipe_name': recipe.css('span.card__title-text::text').get(),
                    'recipe_link': recipe.css('a.mntl-card').attrib['href'],
                }
            except: {
                
            }