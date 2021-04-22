const ready = (id) => {
    let isIdExist = false
	// If the body element and the #main element exist
	if (document.body && document.querySelector(id)) {
		// Run your code here...
		// Return so that we don't call requestAnimationFrame() again
        isIdExist = true
		return isIdExist;
	}

	// If the body element isn't found, run ready() again at the next pain
    window.requestAnimationFrame(ready);
    
};

// Initialize our ready() function
window.requestAnimationFrame(ready);


ready()