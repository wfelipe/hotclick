function hotclick_click(e) {
    // only pay attention on left click
	if( e.button != 0 ){
		return;
	}

	console.log(e, e.clientX, e.clientY);
	console.log(e.originalTarget, e.currentTarget);
}

function hotclick_listener(clickurl) {
    // mouseup is when the effective click is registered
	document.addEventListener && document.addEventListener('mouseup', hotclick_click, false);
	document.attachEvent && document.attachEvent('onmouseup', hotclick_click);
}
