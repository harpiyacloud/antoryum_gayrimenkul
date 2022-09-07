# Copyright (c) 2022, Harpiya Software Technologies

from math import ceil

import harpiya
from harpiya import _
from harpiya.utils import (
	cint,
	get_fullname,
	global_date_format,
	markdown,
	sanitize_html,
	strip_html_tags,
	today,
)
from harpiya.website.utils import (
	clear_cache,
	find_first_image,
	get_comment_list,
	get_html_content_based_on_type,
)
from harpiya.website.website_generator import WebsiteGenerator
from slugify import slugify

class Estate(WebsiteGenerator):
	@harpiya.whitelist()
	def make_route(self):
		if not self.route:
			return (
				harpiya.db.get_value("Estate Category", self.estate_category, "route")
				+ "/"
				+ slugify(self.title)
			)

	def validate(self):
		super().validate()

		if self.published and not self.published_on:
			self.published_on = today()

		self.set_read_time()

	def on_update(self):
		super().on_update()
		clear_cache("writers")

	def on_trash(self):
		super().on_trash()

	def get_context(self, context):
		# this is for double precaution. usually it wont reach this code if not published
		if not cint(self.published):
			raise Exception("This estane has not been published yet!")

		context.no_breadcrumbs = True

		# temp fields
		context.full_name = get_fullname(self.owner)
		context.updated = global_date_format(self.published_on)
		context.social_links = self.fetch_social_links_info()


		if self.broker:
			context.broker_info = harpiya.get_doc("Broker", self.broker).as_dict()
			context.author = self.broker

		context.content = get_html_content_based_on_type(self, "content", self.content)

		context.description = (
			strip_html_tags(context.content[:140])
		)

		context.metatags = {
			"name": self.title,
			"description": context.description,
		}

		image = find_first_image(context.content)
		context.metatags["image"] = self.manset_resmi or image or None

		self.load_likes(context)

		context.category = harpiya.db.get_value(
			"Estate Category", context.doc.estate_category, ["title", "route"], as_dict=1
		)
		context.parents = [
			{"name": _("Anasayfa"), "route": "/"},
			{"name": _("Portföy"), "route": "/portfoy"},
			{"label": context.category.title, "route": context.category.route},
		]

	def fetch_social_links_info(self):
		if not harpiya.db.get_single_value("Estate Settings", "enable_social_sharing", cache=True):
			return []

		url = harpiya.local.site + "/" + self.route

		social_links = [
			{
				"icon": "twitter",
				"link": "https://twitter.com/intent/tweet?text=" + self.title + "&url=" + url,
			},
			{"icon": "facebook", "link": "https://www.facebook.com/sharer.php?u=" + url},
			{"icon": "linkedin", "link": "https://www.linkedin.com/sharing/share-offsite/?url=" + url},
			{"icon": "envelope", "link": "mailto:?subject=" + self.title + "&body=" + url},
		]

		return social_links

	def load_likes(self, context):
		user = harpiya.session.user

		filters = {
			"comment_type": "Like",
			"reference_doctype": self.doctype,
			"reference_name": self.name,
		}

		context.like_count = harpiya.db.count("Comment", filters) or 0

		filters["comment_email"] = user

		if user == "Guest":
			filters["ip_address"] = harpiya.local.request_ip

		context.like = harpiya.db.count("Comment", filters) or 0

	def set_read_time(self):
		content = self.content or ""

		total_words = len(strip_html_tags(content).split())
		self.read_time = ceil(total_words / 250)


def get_list_context(context=None):
	list_context = harpiya._dict(
		get_list=get_estate_list,
		no_breadcrumbs=True,
		hide_filters=True,
		# show_search = True,
		title=_("Portföy"),
	)

	category = harpiya.utils.escape_html(
		harpiya.local.form_dict.estate_category or harpiya.local.form_dict.category
	)
	if category:
		category_title = get_estate_category(category)
		list_context.sub_title = _("Posts filed under {0}").format(category_title)
		list_context.title = category_title

	elif harpiya.local.form_dict.broker:
		broker = harpiya.db.get_value("Broker", {"name": harpiya.local.form_dict.broker}, "full_name")
		list_context.sub_title = _("Posts by {0}").format(broker)
		list_context.title = broker

	elif harpiya.local.form_dict.txt:
		list_context.sub_title = _('Filtered by "{0}"').format(sanitize_html(harpiya.local.form_dict.txt))

	if list_context.sub_title:
		list_context.parents = [{"name": _("Anasayfa"), "route": "/"}, {"name": _("Portöy"), "route": "/portfoy"}]
	else:
		list_context.parents = [{"name": _("Anasayfa"), "route": "/"}]

	estate_settings = harpiya.get_doc("Estate Settings").as_dict(no_default_fields=True)
	list_context.update(estate_settings)

	if estate_settings.browse_by_category:
		list_context.estate_categories = get_estate_categories()

	return list_context


def get_estate_categories():
	from pypika import Order
	from pypika.terms import ExistsCriterion

	post, category = harpiya.qb.DocType("Estate"), harpiya.qb.DocType("Estate Category")
	return (
		harpiya.qb.from_(category)
		.select(category.name, category.route, category.title)
		.where(
			(category.published == 1)
			& ExistsCriterion(
				harpiya.qb.from_(post)
				.select("name")
				.where((post.published == 1) & (post.estate_category == category.name))
			)
		)
		.orderby(category.title, order=Order.asc)
		.run(as_dict=1)
	)


def clear_estate_cache():
	for estate in harpiya.db.sql_list(
		"""select route from
		`tabEstate` where ifnull(published,0)=1"""
	):
		clear_cache(estate)

	clear_cache("writers")


def get_estate_category(route):
	return harpiya.db.get_value("Estate Category", {"name": route}, "title") or route


def get_estate_list(
	doctype, txt=None, filters=None, limit_start=0, limit_page_length=20, order_by=None
):
	conditions = []
	if filters and filters.get("estate_category"):
		category = filters.get("estate_category")
	else:
		category = harpiya.utils.escape_html(
			harpiya.local.form_dict.estate_category or harpiya.local.form_dict.category
		)

	if filters and filters.get("broker"):
		conditions.append("t1.broker=%s" % harpiya.db.escape(filters.get("broker")))

	if category:
		conditions.append("t1.estate_category=%s" % harpiya.db.escape(category))

	if txt:
		conditions.append(
			'(t1.content like {0} or t1.title like {0}")'.format(harpiya.db.escape("%" + txt + "%"))
		)

	if conditions:
		harpiya.local.no_cache = 1

	query = """\
		select
			t1.title, 
   			t1.name,
      		t1.estate_category, 
        	t1.route, 
         	t1.published_on, 
          	t1.read_time,
			t1.estate_type,
			t1.estate_price,
			t1.currency,
			t1.mahalle,
			t1.ilce,
			t1.il,
			t1.enlem,
			t1.boylam,
				t1.published_on as creation,
				t1.read_time as read_time,
				t1.featured as featured,
				t1.manset_resmi as manset_resmi,
				t1.content as content,
				t2.full_name, t2.avatar, t1.broker
		from `tabEstate` t1, `tabBroker` t2
		where ifnull(t1.published,0)=1
		and t1.broker = t2.name
		{condition}
		order by featured desc, published_on desc, name asc
		limit {page_len} OFFSET {start}""".format(
		start=limit_start,
		page_len=limit_page_length,
		condition=(" and " + " and ".join(conditions)) if conditions else "",
	)

	posts = harpiya.db.sql(query, as_dict=1)

	for post in posts:
		post.content = get_html_content_based_on_type(post, "content", post.content)
		post.published = global_date_format(post.creation)
		post.content = strip_html_tags(post.content)

		post.avatar = post.avatar or ""
		post.category = harpiya.db.get_value(
			"Estate Category", post.estate_category, ["name", "route", "title"], as_dict=True
		)

		if (
			post.avatar
			and (not "http:" in post.avatar and not "https:" in post.avatar)
			and not post.avatar.startswith("/")
		):
			post.avatar = "/" + post.avatar

	return posts
