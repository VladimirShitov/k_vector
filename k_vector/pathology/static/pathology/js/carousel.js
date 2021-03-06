console.log("carousel.js is loaded");

var images = document.getElementsByClassName('my-carousel-img');
var i = 0;
carousel = document.getElementById("my-carousel");
var x;
var y;

// Show the first image
images[0].classList.remove("inactive");
images[0].classList.add("active");

const OFFSET = 25;

change_image = function(is_forward) {
	current_image = images[i];
	current_image.classList.remove("active");
	current_image.classList.add("inactive");

	if (is_forward) {
		i = (i < images.length - 1) ? i+1 : 0;
	} else {
		i = (i > 0) ? i-1 : images.length - 1;
	}

	next_image = images[i];
	next_image.classList.remove("inactive");
	next_image.classList.add("active");
}

run_carousel = function(e) {
	event = (e.touches === undefined) ? e : e.touches[0];
	// Photos are taken in the direction of clock rotation if you look at them from the top
	if(x - event.pageX > OFFSET) {
		change_image(false);
		x = event.pageX;
		y = event.pageY;
	}
	else if(event.pageX - x > OFFSET) {
		change_image(true);
		x = event.pageX;
		y = event.pageY;
	}
}

carousel.ondragstart = function() {
	return false;
}

carousel.onmousedown = function(e) {
	x = e.pageX;
	y = e.pageY;
	carousel.onmousemove = function(e) { run_carousel(e) };
	document.onmouseup = function() {
		carousel.onmousemove = null;
	}
}

handleTouchStart = function(e) {
	e.preventDefault();
	x = e.touches[0].pageX;
	y = e.touches[0].pageY;
	carousel.addEventListener("touchmove", run_carousel, false);
	document.addEventListener("touchend", function(e) {
		carousel.removeEventListener("touchmove", run_carousel);
	}, false);
}

carousel.addEventListener("touchstart", handleTouchStart, false);
