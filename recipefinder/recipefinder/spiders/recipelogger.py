import scrapy 
import json

class RecipeLogger(scrapy.Spider):
    name = 'logger'
    start_urls = ['https://www.allrecipes.com/recipe/174668/blackened-seasoning-mix/']
    # def start_requests(self):
    #     with open("list.json", "r") as f:
    #         data = json.load(f)
    #         for url in data:
    #             yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        ingredient_list = []
        for quantity in range(0, len(response.css("span[data-ingredient-quantity='true']::text").extract())):
            ingredient_quantity = response.css("span[data-ingredient-quantity='true']::text").extract()[quantity]
            ingredient_unit = response.css("span[data-ingredient-unit='true']::text").extract()[quantity]
            ingredient_name = response.css("span[data-ingredient-name='true']::text").extract()[quantity]
            ingredient = ingredient_quantity + " " + ingredient_unit + " " +  ingredient_name
            ingredient_list.append(ingredient)
        # print(ingredient)
        try:
            
            yield {
                'name': response.css('h1.article-heading::text').get(),
                'serving_size': response.css('div.mm-recipes-details__value::text')[-1].get(),
                'link': response.url,
                'cals': response.css('td.type--dog-bold::text').get(),
                'fat': response.css('td.type--dog-bold::text')[1].get(),
                'carbs': response.css('td.type--dog-bold::text')[2].get(),
                'protein': response.css('td.type--dog-bold::text')[3].get(),
                'img': response.css('img.primary-image__image').attrib['src'],
                "ingredients": ingredient_list
            }
        except: 
            yield {
                'name': 'error',
            }