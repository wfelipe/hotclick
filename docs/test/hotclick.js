(function(){
	function log(){
		if( ! h.debug ){ return false; }

		window.console && console.log
			? console.log( arguments )
			: alert( Array.prototype.slice.call(arguments).join(', ') );
	}

	var h = window.HotClick = {
		debug: 1,
		linkRecursion: 10,
		init: function(clickurl){
			this.clickurl = clickurl || '';

			this.event();

			this.ajax();

			log('HotClick initialized');
		},
		event: function(){
				// mouseup is when the effective click is registered
			document.addEventListener && document.addEventListener('mouseup', this.click, false);
			document.attachEvent && document.attachEvent('onmouseup', this.click);
		},
		click: function(event){
			var e = h.fixEvent( event ),
					opt = {
						type: e.target.tagName,
						platform: navigator.platform,
						link: escape( h.findLink( event.target ) || '' ),
						x: e.pageX || ( e.clientX + ( document.documentElement.scrollLeft || document.body.scrollLeft ) ),
						y: e.pageY || ( e.clientY + ( document.documentElement.scrollTop	|| document.body.scrollTop ) )
					};

			// ignore right click
			if( e.which == 3 ){
				return false;
			}

			log( 'click:', opt );

			h.req(h.clickurl + '?' + [
				'x='+ opt.x,
				'y='+ opt.y,
				'link='+ opt.link
			].join('&') );

			return false;
		},
		findLink: function(element,recursion){
			// use the default max
			recursion = recursion || this.linkRecursion;

			log( 'findLink: ', element, recursion );

			if( element.tagName == 'BODY' || element.parentNode.tagName == 'BODY' || recursion == 0  ){
				return false;
			} else if( element.parentNode.tagName == 'A' ){
				return element.parentNode.href;
			} else {
				return this.findLink( element.parentNode, --recursion );
			}
		},
		fixEvent: function(event){
			// Fix target property, if necessary
			if ( !event.target ) {
				event.target = event.srcElement || document; // Fixes #1925 where srcElement might not be defined either
			}

			// check if target is a textnode (safari)
			if ( event.target.nodeType === 3 ) {
				event.target = event.target.parentNode;
			}

			// Add which for click: 1 === left; 2 === middle; 3 === right
			// Note: button is not normalized, so don't use it
			if ( !event.which && event.button !== undefined ) {
				event.which = (event.button & 1 ? 1 : ( event.button & 2 ? 3 : ( event.button & 4 ? 2 : 0 ) ));
			}

			return event;
		},
		ajax: function(){
			if( window.XMLHttpRequest && !window.ActiveXObject ){
				this.xhr = new window.XMLHttpRequest();
			} else {
				try {
					this.xhr = new window.ActiveXObject("Microsoft.XMLHTTP");
				} catch(e) {
					this.xhr = false;
				}
			}
		},
		req: function(url){
			var xhr = this.xhr;
			xhr.open('get', url, false);
			xhr.send( null );
		}
	};
})();
