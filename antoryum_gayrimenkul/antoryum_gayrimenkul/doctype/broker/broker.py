# Copyright (c) 2022, Harpiya Software Technologies and contributors
# For license information, please see license.txt

import harpiya
from harpiya.model.document import Document

class Broker(Document):
	def validate(self):
		if self.user and not harpiya.db.exists("User", self.user):
			harpiya.get_doc(
				{"doctype": "User", "email": self.user, "first_name": self.user.split("@")[0]}
			).insert()
