app_name = "qutell_modification"
app_title = "Qutell modification"
app_publisher = "Hisham Qasrawii"
app_description = "Qutell modification"
app_email = "qasrawii86@gmail.com"
app_license = "mit"
# داخل hooks.py
fixtures = [
    # تخصيصات الفورم
    {"dt": "Custom Field",     "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Property Setter",  "filters": [["module", "=", "Qutell modification"]]},
    # سكربتات
    {"dt": "Client Script",    "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Server Script",    "filters": [["module", "=", "Qutell modification"]]},
    # تقارير ولوحات
    {"dt": "Report",           "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Workspace",        "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Dashboard",        "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Dashboard Chart",  "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Number Card",      "filters": [["module", "=", "Qutell modification"]]},
    # طباعات واشعارات 
    {"dt": "Print Format",     "filters": [["module", "=", "Qutell modification"]]},
    {"dt": "Notification",     "filters": [["module", "=", "Qutell modification"]]},
    # في حال أنشأت DocTypes "مخصّصة" من الديسك بدون ملفات قياسية
    {"dt": "DocType",          "filters": [["custom", "=", 1], ["module", "=", "Qutell modification"]]},
]


# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "qutell_modification",
# 		"logo": "/assets/qutell_modification/logo.png",
# 		"title": "Qutell modification",
# 		"route": "/qutell_modification",
# 		"has_permission": "qutell_modification.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/qutell_modification/css/qutell_modification.css"
# app_include_js = "/assets/qutell_modification/js/qutell_modification.js"

# include js, css files in header of web template
# web_include_css = "/assets/qutell_modification/css/qutell_modification.css"
# web_include_js = "/assets/qutell_modification/js/qutell_modification.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "qutell_modification/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "qutell_modification/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "qutell_modification.utils.jinja_methods",
# 	"filters": "qutell_modification.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "qutell_modification.install.before_install"
# after_install = "qutell_modification.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "qutell_modification.uninstall.before_uninstall"
# after_uninstall = "qutell_modification.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "qutell_modification.utils.before_app_install"
# after_app_install = "qutell_modification.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "qutell_modification.utils.before_app_uninstall"
# after_app_uninstall = "qutell_modification.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "qutell_modification.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"qutell_modification.tasks.all"
# 	],
# 	"daily": [
# 		"qutell_modification.tasks.daily"
# 	],
# 	"hourly": [
# 		"qutell_modification.tasks.hourly"
# 	],
# 	"weekly": [
# 		"qutell_modification.tasks.weekly"
# 	],
# 	"monthly": [
# 		"qutell_modification.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "qutell_modification.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "qutell_modification.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "qutell_modification.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["qutell_modification.utils.before_request"]
# after_request = ["qutell_modification.utils.after_request"]

# Job Events
# ----------
# before_job = ["qutell_modification.utils.before_job"]
# after_job = ["qutell_modification.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"qutell_modification.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

