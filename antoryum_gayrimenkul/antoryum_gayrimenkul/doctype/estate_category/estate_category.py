# Copyright (c) 2022, Harpiya Software Technologies and contributors
# For license information, please see license.txt

# import harpiya
from slugify import slugify
from harpiya.website.utils import clear_cache
from harpiya.website.website_generator import WebsiteGenerator

class EstateCategory(WebsiteGenerator):
	def autoname(self):
		self.name  = slugify(self.title)

	def on_update(self):
		clear_cache()

	def set_route(self):
		self.route = "portfoy/" + self.name
