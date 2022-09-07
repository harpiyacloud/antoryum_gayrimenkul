// Copyright (c) 2022, Harpiya Software Technologies and contributors

harpiya.ui.form.on("Gallery", {
	refresh: (frm) => {
		frm.add_custom_button(__('Klasörden Resimleri Getir'), () => {
			const d = new harpiya.ui.Dialog({
				title: __('Klasörden Resimleri Getir'),
				fields: [
					{
						label: __('Klasör Adı'),
						fieldtype: 'Link',
						fieldname: 'folder',
						options: 'File',
						reqd: 1
					}
				],
				primary_action_label: __('Tabloya Ekle'),
				primary_action: ({ folder }) => {
					harpiya.db.get_list('File', {
						fields: ['file_url', 'file_name'],
						filters: {
							folder: folder
						}
					}).then(images => {
						frm.doc.gallery_items = frm.doc.gallery_items || [];
						images.forEach(image => {
							var new_row = frm.add_child("gallery_items");
							new_row.image = image.file_url
						});

						frm.refresh_field('gallery_items');
						d.hide();
					});
				}
			});

			d.show();
		})
	},
})