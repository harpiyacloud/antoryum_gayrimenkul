from . import __version__ as app_version

app_name = "antoryum_gayrimenkul"
app_title = "Antoryum Gayrimenkul"
app_publisher = "Harpiya Software Technologies"
app_description = "Antoryum Website & Uygulama"
app_email = "info@harpiya.cloud"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/antoryum_gayrimenkul/css/antoryum_gayrimenkul.css"
# app_include_js = "/assets/antoryum_gayrimenkul/js/antoryum_gayrimenkul.js"

# include js, css files in header of web template
web_include_css = [
    "/assets/antoryum_gayrimenkul/css/plugins.css",
    "/assets/antoryum_gayrimenkul/css/style.css",
    "/assets/antoryum_gayrimenkul/css/color.css",
    ]
web_include_js =[ 
    "/assets/antoryum_gayrimenkul/js/plugins.js",
    "/assets/antoryum_gayrimenkul/js/scripts.js",
    "/assets/antoryum_gayrimenkul/js/website_utils.js"
    ]
website_route_rules = [
	{"from_route": "/portfoy/<category>", "to_route": "Estate"},
]

base_template_map = {
	r"internal.*": "templates/doc.html",
}


# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "antoryum_gayrimenkul/public/scss/website.bundle"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "antoryum_gayrimenkul.utils.jinja_methods",
#	"filters": "antoryum_gayrimenkul.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "antoryum_gayrimenkul.install.before_install"
# after_install = "antoryum_gayrimenkul.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "antoryum_gayrimenkul.uninstall.before_uninstall"
# after_uninstall = "antoryum_gayrimenkul.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See harpiya.core.notifications.get_notification_config

# notification_config = "antoryum_gayrimenkul.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "harpiya.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "harpiya.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"antoryum_gayrimenkul.tasks.all"
#	],
#	"daily": [
#		"antoryum_gayrimenkul.tasks.daily"
#	],
#	"hourly": [
#		"antoryum_gayrimenkul.tasks.hourly"
#	],
#	"weekly": [
#		"antoryum_gayrimenkul.tasks.weekly"
#	],
#	"monthly": [
#		"antoryum_gayrimenkul.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "antoryum_gayrimenkul.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"harpiya.desk.doctype.event.event.get_events": "antoryum_gayrimenkul.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Harpiya apps
# override_doctype_dashboards = {
#	"Task": "antoryum_gayrimenkul.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"antoryum_gayrimenkul.auth.validate"
# ]
