// Copyright (c) 2022, Harpiya Software Technologies and contributors

harpiya.ui.form.on('Estate', {
	refresh: function(frm) {

	},
	title: function(frm) {
		frm.trigger("set_route");
	},

	estate_category(frm) {
		frm.trigger("set_route");
	},

	set_route(frm) {
		if (frm.doc.route) return;
		if (frm.doc.title && frm.doc.estate_category) {
			frm.call("make_route").then((r) => {
				frm.set_value("route", r.message);
			});
		}
	},
});
