(function(){
	function log(){
		if( ! h.debug ){ return false; }

		window.console && console.log
			? console.log( arguments )
			: alert( Array.prototype.slice.call(arguments).join(', ') );
	}

	var h = window.HotClick = {
		debug: 1,
		init: function(){
			this.event();

			log('HotClick initialized');
		},
		event: function(){
				// mouseup is when the effective click is registered
			document.addEventListener && document.addEventListener('mouseup', this.click, false);
			document.attachEvent && document.attachEvent('onmouseup', this.click);
		},
		click: function(e){
				// only pay attention on left click
			if( e.button != 0 ){
				return;
			}

			log(e, e.clientX, e.clientY);
			log(e.originalTarget, e.currentTarget);
		}
	};
})();
