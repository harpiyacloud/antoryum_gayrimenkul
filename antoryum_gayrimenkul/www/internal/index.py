import harpiya

def get_context(context):
	harpiya.flags.redirect_location = "/internal/getting-started/overview"
	raise harpiya.Redirect