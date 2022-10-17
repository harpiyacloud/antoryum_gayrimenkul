// Copyright (c) 2022, Harpiya Software Technologies and contributors

harpiya.ui.form.on('Estate', {
	refresh(frm) {
		frm.fields_dict["images"].grid.add_custom_button(__('Resim Ekle'), 
			function() {
				new harpiya.ui.FileUploader({
					folder: "Ana/Ekler",
					restrictions: {
						allowed_file_types: ["image/*"],
					},
					on_success: file_doc => {
						frm.doc.images = frm.doc.images || [];
						var new_row = frm.add_child("images");
						new_row.image = file_doc.file_url
						new_row.tag = file_doc.file_name
						frm.refresh_field('images');
					}
				});		
        }).css({'margin-right': 10})
		frm.fields_dict["images"].grid.grid_buttons.find('.btn-custom').removeClass('btn-default').addClass('btn-info');	
	},
	title: function(frm) {
		frm.trigger("set_route");
	},

	upload_image(frm) {
		
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
