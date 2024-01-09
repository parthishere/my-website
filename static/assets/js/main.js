//Get the button:
mybutton = document.getElementById("myBtn");
themebutton = document.getElementById("themeChange");

const favDialog1 = document.getElementById("favDialog1")
const showDialogBtn1 = document.getElementById("showDialogBtn1")

const favDialog2 = document.getElementById("favDialog2")
const showDialogBtn = document.getElementById("showDialogBtn2")

const favDialog3 = document.getElementById("favDialog3")
const showDialogBtn3 = document.getElementById("showDialogBtn3")

const favDialog4 = document.getElementById("favDialog4")
const showDialogBtn4 = document.getElementById("showDialogBtn4")

const favDialog5 = document.getElementById("favDialog5")
const showDialogBtn5 = document.getElementById("showDialogBtn5")

const favDialog6 = document.getElementById("favDialog6")
const showDialogBtn6 = document.getElementById("showDialogBtn6")

const favDialog7 = document.getElementById("favDialog7")
const showDialogBtn7 = document.getElementById("showDialogBtn7")

const favDialog8 = document.getElementById("favDialog8")
const showDialogBtn8 = document.getElementById("showDialogBtn8")

const favDialog9 = document.getElementById("favDialog9")
const showDialogBtn9 = document.getElementById("showDialogBtn9")

const favDialog10 = document.getElementById("favDialog10")
const showDialogBtn10 = document.getElementById("showDialogBtn10")

const favDialog11 = document.getElementById("favDialog11")
const showDialogBtn11 = document.getElementById("showDialogBtn11")


showDialogBtn1.addEventListener("click", () => favDialog1.showModal())
showDialogBtn2.addEventListener("click", () => favDialog2.showModal())
showDialogBtn3.addEventListener("click", () => favDialog3.showModal())
showDialogBtn4.addEventListener("click", () => favDialog4.showModal())
showDialogBtn5.addEventListener("click", () => favDialog5.showModal())
showDialogBtn6.addEventListener("click", () => favDialog6.showModal())
showDialogBtn7.addEventListener("click", () => favDialog7.showModal())
showDialogBtn8.addEventListener("click", () => favDialog8.showModal())
showDialogBtn9.addEventListener("click", () => favDialog9.showModal())
showDialogBtn10.addEventListener("click", () => favDialog10.showModal())
showDialogBtn11.addEventListener("click", () => favDialog11.showModal())



// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

var $container = $('.isotope');
    
$container.imagesLoaded(function () {
	$('.isotope').isotope({
		itemSelector: '.item'
	});
});

// filter items on click
$('.filters').on( 'click', '.type', function() {
	var filterValue = $(this).attr('data-filter');
	console.log(filterValue);
	$container.isotope({ filter: filterValue });
});

// change is-checked class on buttons
$('.filters').each( function( i, typeGroup ) {
	var $typeGroup = $( typeGroup );
	$typeGroup.on( 'click', '.type', function() {
		$typeGroup.find('.active').removeClass('active');
		$( this ).addClass('active');
	});
});



var $container2 = $('.isotope2');

$container2.imagesLoaded(function () {
	$('.isotope2').isotope({
		itemSelector: '.item'
	});
});

// filter items on click
$('.filters2').on( 'click', '.type', function() {
var filterValue = $(this).attr('data-filter');
console.log(filterValue);
$container2.isotope({ filter: filterValue });
});

// change is-checked class on buttons
$('.filters2').each( function( i, typeGroup ) {
	var $typeGroup = $( typeGroup );
	$typeGroup.on( 'click', '.type', function() {
	$typeGroup.find('.active').removeClass('active');
	$( this ).addClass('active');
	});
});

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
	// themebutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
	// themebutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
};


"use strict";

//Enable tooltips everywhere
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})


/* Vanilla RSS - https://github.com/sdepold/vanilla-rss */

	const rss = new RSS(
	    document.querySelector("#rss-feeds"),
	    //Change this to your own rss feeds
        "https://feeds.feedburner.com/TechCrunch/startups",
	    {
		     // how many entries do you want?
		    // default: 4
		    // valid values: any integer
		    limit: 3,
		    
		    
		    // will request the API via https
			// default: false
			// valid values: false, true
			ssl: true,
		  
			 // outer template for the html transformation
			// default: "<ul>{entries}</ul>"
			// valid values: any string
			layoutTemplate: "<div class='items'>{entries}</div>",
		
			// inner template for each entry
			// default: '<li><a href="{url}">[{author}@{date}] {title}</a><br/>{shortBodyPlain}</li>'
			// valid values: any string
			entryTemplate: '<div class="item"><h3 class="title"><a href="{url}" target="_blank">{title}</a></h3><div><p>{shortBodyPlain}</p><a class="more-link" href="{url}" target="_blank"><i class="fas fa-external-link-alt"></i>Read more</a></div></div>',
		    
	    }
	);
	rss.render();

    
    /* Github Calendar - https://github.com/IonicaBizau/github-calendar */
    new GitHubCalendar("#github-graph", "parthishere", { responsive: true });
    
    
    /* Github Activity Feed - https://github.com/caseyscarborough/github-activity */
    GitHubActivity.feed({ username: "parthishere", selector: "#ghfeed" });



