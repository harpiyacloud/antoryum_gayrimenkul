// Copyright (c) 2022, Harpiya Software Technologies
// MIT License. See license.txt

harpiya.ready(function() {

	if(harpiya.utils.get_url_arg('subject')) {
	  $('[name="subject"]').val(harpiya.utils.get_url_arg('subject'));
	}

	$('.btn-send').off("click").on("click", function() {
		var name = $('[name="name"]').val();
		var email = $('[name="email"]').val();
		var message = $('[name="message"]').val();

		if(!(name && email && message)) {
			harpiya.msgprint('{{ _("Lütfen gerekli tüm alanları doldurun! Teşekkürler") }}');
			return false;
		}

		if(!validate_email(email)) {
			harpiya.msgprint('{{ _("Lütfen geçerli bir e-posta adresi girin.") }}');
			$('[name="email"]').focus();
			return false;
		}

		$("#contact-alert").toggle(false);
		harpiya.send_message({
			subject: $('[name="subject"]').val(),
			sender: email,
			message: message,
			callback: function(r) {
				if(r.message==="okay") {
					harpiya.msgprint('{{ _("Mesajınız için teşekkür ederiz.") }}');
				} else {
					harpiya.msgprint('{{ _("Hata oluştu") }}');
					console.log(r.exc);
				}
				$(':input').val('');
			}
		}, this);
		return false;
	});

});

var msgprint = function(txt) {
	if(txt) $("#contact-alert").html(txt).toggle(true);
}
