function hotclick_click(event) {
	console.log(event, event.clientX, event.clientY);
	console.log(event.currentTarget, event.originalTarget.href);
}

function hotclick_listener(clickurl) {
	/** Add onmousedown event using listeners */
	if (document.addEventListener)
	{
		document.addEventListener('mousedown', hotclick_click, false);
	}
	else if (document.attachEvent)
	{
		document.attachEvent('onmousedown', hotclick_click);
	}
}
