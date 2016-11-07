//// main script for the JavaScript ////

// Create a popup on the main page
	// alert('Hello JavaScript!');

// create variable skillset that selects HTML element
	// var skillset = document.getElementsByClassName('skillset');

// create alert on skillset to make the skillset variable's value a pop-up.
	// alert(skillset);

// create a function named main, with nothing in it / no parameters.
	// function main(){}

// This checks if the page is ready for our code.
	// $(document).ready(main);
	// when the document is ready it will callback the main function.
	// main is a callback -- jQuery calls back the main function.
	// prevents our jQuery running before the elements they use are rendered.

//// selectors:
// You can write a jQuery selector by wraping the class name in this code: 
	// $('.class-name-here').

// Note: It is necessary to include the . for class names. 
// If you were selecting an id, it would be necessary to include the #, 
	// like so: 
	// $('#id-name-here')

// to hide skillset
	// function main() {
  	//  $('.skillset').hide();
	// }

// to fadeIn skillset
	// function main() {
	//  $('.skillset').hide();
	//  $('.skillset').fadeIn(1000);
	// }

// to make button clickable
	// $('.projects-button').on('click', function() {});
 
// to make button show something
	// $('.projects-button').on('click', function() {
  	//	$('.projects').show();
  	// });

// to make button toggle on and off
  // $('.projects-button').on('click', function() {
  // 	$('.projects').toggle();
  // });

// to make button change colour when toggled onn/off
	// $('.projects-button').on('click', function() {
	//   	$('.projects').toggle();
	// 	$('.projects-button').toggleClass('active')
	//   });

// to make button only toggle specific element colour change
	// $(this).toggleClass('active')

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$('.projects').toggle();
	$(this).toggleClass('active')
  });
}





$(document).ready(main);








