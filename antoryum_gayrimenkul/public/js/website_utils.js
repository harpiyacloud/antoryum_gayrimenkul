if(!window.antoryum) window.antoryum = {};


antoryum.subscribe_to_newsletter = function(opts, btn) {
	return harpiya.call({
		type: "POST",
		method: "harpiya.email.doctype.newsletter.newsletter.subscribe",
		btn: btn,
		args: {"email": opts.email},
		callback: opts.callback
	});
}