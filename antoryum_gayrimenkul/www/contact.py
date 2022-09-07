# Copyright (c) 2022, Harpiya Software Technologies

import harpiya
from harpiya import _
from harpiya.utils import now

sitemap = 1


def get_context(context):
	doc = harpiya.get_doc("Contact Us Settings", "Contact Us Settings")

	if doc.query_options:
		query_options = [opt.strip() for opt in doc.query_options.replace(",", "\n").split("\n") if opt]
	else:
		query_options = ["Satış", "Destek", "Genel"]

	out = {"query_options": query_options, "parents": [{"name": _("Anasayfa"), "route": "/"}]}
	out.update(doc.as_dict())

	return out


max_communications_per_hour = 1000


@harpiya.whitelist(allow_guest=True)
def send_message(subject="Website Query", message="", sender="", name=""):
	if not message:
		harpiya.response["message"] = _("Lütfen bir şeyler yazın")
		return

	if not sender:
		harpiya.response["message"] = _("E-posta adresi gerekli")
		return

	# guest method, cap max writes per hour
	if (
		harpiya.db.sql(
			"""select count(*) from `tabCommunication`
		where `sent_or_received`="Received"
		and TIMEDIFF(%s, modified) < '01:00:00'""",
			now(),
		)[0][0]
		> max_communications_per_hour
	):
		harpiya.response[
			"message"
		] = "Üzgünüz: Bu türden makul olmayan sayıda talep aldığımızı düşünüyoruz. Lütfen daha sonra tekrar deneyin"
		return

	# send email
	forward_to_email = harpiya.db.get_single_value("Contact Us Settings", "forward_to_email")
	if forward_to_email:
		harpiya.sendmail(recipients=forward_to_email, sender=sender, content=message, subject=subject)

	# add to to-do ?
	harpiya.get_doc(
		dict(
			doctype="Communication",
			sender=sender,
			subject=_("Websitesi İletişim Sayfasından Yeni Mesaj") + name,
			sent_or_received="Received",
			content=message,
			status="Open",
		)
	).insert(ignore_permissions=True)

	return "okay"