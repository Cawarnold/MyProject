//// Practice_JavaScript ////



///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////

// Practice with the interactive lessons on:
// https://www.codecademy.com/learn/javascript

///////////////////////////////////
///////////////////////////////////
// Objects I
///////////////////////////////////
///////////////////////////////////


//////////////
// Building an Address Book
//////////////


//////////////	Objects in address books are fun!
////// Lesson 1/6 Digitizing People

// Meet Bob. Bob is our friend. But how do we get in touch with Bob?

// Look at the code in the editor. 
// We have Bob's information stored in an associative array named bob. 
// bob has a property called firstName which has a value of "Bob". 
// Similarly, it has properties lastName, phoneNumber and email which each have values.

// To access the values for each property we write array.property. 
// Check out line 8 where we log to the console bob.firstName.

var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-777",
    email: "bob.jones@example.com"
};

//// Instructions:

// Copying the format we used on line 8, 
// fill in lines 9 and 10 so that Bob's lastName and email are printed out.

console.log(bob.firstName);
console.log(bob.lastName);
console.log(bob.email);


//////////////	Objects in address books are fun!
////// Lesson 2/6 More People

// Just like with strings and numbers, 
// we can put multiple objects into an array. 
// We want to practice extracting information 
// from different objects which are stored in the same array.

// This allows us to put all of our contact objects into a unified list. 
// If the objects are contact entries, then the list is the book binding that 
// ties all of the contact entries together.

var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

//// Instructions:

// Create an object called mary. It has the same properties as bob. 
// Her name is Mary Johnson, 
// her phoneNumber is "(650) 888 - 8888" 
// and her email is "mary.johnson@example.com".

// Create an array called contacts. Put bob in first (at index 0), 
// then mary (at index 1).

// Write a console.log statement that prints out Mary's phone number.


var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650)  888-8888",
    email: "mary.johnson@example.com"
};

var contacts = new Array();

contacts[0] = bob;
contacts[1] = mary;

console.log(contacts[0].phoneNumber)	// failed - but did give her number.
console.log(mary.phoneNumber)			// worked


//////////////	Objects in address books are fun!
////// Lesson 3/6 Displaying People

// We currently can print out information about any person 
// in our contacts with console.log. 
// That gets tiring. 
// If only we knew some code that stores blocks of code that we can call.

// Good thing we know about functions!

// We can create a function that consistently displays a specific property of an object.

//// Instructions:

// Define a function called printPerson that takes a parameter called person.
// In the function body, print out the person parameter's firstName property 
// by accessing it with a dot just like before. 
// Then print a space, then their lastName in the same way.

// Call the printPerson() function to print out the first item in the contacts array. 
// The first item in an array is at position 0.

// Then on the next line, call printPerson() again to print out the second item 
// in the contacts array.

// Don't worry if your output appears twice - we're just double checking your code!

var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650) 888-8888",
    email: "mary.johnson@example.com"
};

var contacts = [bob, mary];

// printPerson added here
var printPerson = function(person) {
	console.log(person.firstName + ' ' + person.lastName);
};

printPerson(contacts[0])

printPerson(contacts[1])

//////////////	Objects in address books are fun!
////// Lesson 4/6 Listing Everybody

// Address book programs usually have a screen that lists all of the contacts. 
// Let's build that feature.

// We could write out separate lines of code to display all of the people 
// like in the last exercise, but that's tedious. 
// Instead, we can use a for loop to do this automatically.

//// Instructions:

// We'll be creating a function that lists all of the users.

// Create a function called list that does not take any parameters.

// At the start of the function, define a variable to store 
// the number of items in the contacts array. 
// Call it contactsLength.

// All of the items in an array are numbered, starting at 0. 
// To cycle through all of the elements of the array, 
// create a for loop that cycles from 0 up to one less than the number
// of items in the contacts array.

// Inside of the loop, add code to call printPerson, 
// passing in the element of the array that the loop is currently at.

// At the very bottom of the file, call the list function. 
// The list function should then loop through every member of the contacts array 
// and print its information.

var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650) 888-8888",
    email: "mary.johnson@example.com"
};

var contacts = [bob, mary];

function printPerson(person) {
    console.log(person.firstName + " " + person.lastName);
}

var list = function() {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		printPerson(contacts[i]);
	};
};

list();


//////////////	Objects in address books are fun!
////// Lesson 5/6 Finding that Special Someone

// Let's say we're looking for someone in our address book 
// with a specific last name.

// We can do this with a technique for searching arrays called "linear search". 
// With it, we use a loop to check through all of the items in the array one-by-one 
// until we see the item that we want.

// We can apply linear search to print out all of the people that 
// have a particular last name.

//// Instructions:

// We'll be creating a function that can search for people with a specific last name 
// and print those people out with the printPerson function.

//	Create a function called search that takes a parameter called lastName. 
	// Leave the list function alone.

// Like with the last exercise, define a variable and store the number of items 
	// in the array in it. (Since every function has its own context, or scope, 
	// you can call this variable contactsLength, too, if you like!)

// Create a for loop that runs through all of the items in the array. 
	// For this step, the code for search is identical to that of list.

// The twist comes here: in the body of the loop, 
	// rather than printing out every single item in the array, 
	// add an if statement that checks to see if the lastName property of the object 
	// is equal to the lastName argument. 
	// Have the function run printPerson on the person if and only if 
	// the lastName property of the person matches the lastName argument.

// At the bottom of the file, call the search function, 
	// passing in "Jones" as the last name to search for.

var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650) 888-8888",
    email: "mary.johnson@example.com"
};

var contacts = [bob, mary];

function printPerson(person) {
    console.log(person.firstName + " " + person.lastName);
}

function list() {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		printPerson(contacts[i]);
	}
}

/*Create a search function
then call it passing "Jones"*/

function search(lastName) {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		if (lastName === contacts[i].lastName) {
			printPerson(contacts[i]);
		}
	}
}

search("Jones");


//////////////	Objects in address books are fun!
////// Lesson 6/6 We Made a Friend!

// We have our address book in the contacts array, 
// but what if we make a new friend and want to add them as well?

// Objects, just like other types of data, can be put into arrays 
// with a array[position] = object statement. 
// To append something to the end of the array, 
// you need to put it in the position one after the last item.

// Since arrays are numbered starting at zero, 
// the number of the last item in the array will be one less 
// than the quantity of items in the array. 
// The size of the array is thus the position to insert at.

// The length of an array, like the length of a string, 
// can be found with array.length.

// We can do the insert in a succinct way by adding the new object directly into 
// the array position without even giving it a name. 
// This can be confusing, but we will be able to refer to it by its array position, 
// so it does not need a direct name. 

// Do it like this:
contacts[contacts.length] = {
    firstName: firstName,
    lastName: lastName,
    phoneNumber: phoneNumber,
    email: email
};

// (Assuming you defined the add function with the parameters 
// firstName, lastName, phoneNumber, and email.)

// That will automatically create a new object and add it into the array. 
// Pretty neat.

//// Instructions:

// We'll be creating a function that allows us to add our new friend to the address book.

// Create a function called add with the parameters 
// firstName, lastName, and email, phoneNumber.

// In this new function, you want to create a new contact object like bob and mary. 
// Instead of having this object's property values be filled with strings though, 
// set them to the appropriate function parameters passed in.

// Add this new contact object to the contacts array.

// Call add with whatever first name, last name, phone number, and email arguments you like.

// Make sure you call the list function, to check if your new entry is added. 
// And delete any other function that logs output in the console, i.e 'search' function.

// Run the code!


var bob = {
    firstName: "Bob",
    lastName: "Jones",
    phoneNumber: "(650) 777-7777",
    email: "bob.jones@example.com"
};

var mary = {
    firstName: "Mary",
    lastName: "Johnson",
    phoneNumber: "(650) 888-8888",
    email: "mary.johnson@example.com"
};

var contacts = [bob, mary];

function printPerson(person) {
    console.log(person.firstName + " " + person.lastName);
}

function list() {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		printPerson(contacts[i]);
	}
}

/*Create a search function
then call it passing "Jones"*/
function search(lastName) {
	var contactsLength = contacts.length;
	for (var i = 0; i < contactsLength; i++) {
		if (lastName === contacts[i].lastName) {
			printPerson(contacts[i]);
		}
	}
}

search("Jones");

function add(firstName, lastName, email, phoneNumber) {
	contacts[contacts.length] = {
		firstName: firstName,
		lastName: lastName,
		phoneNumber: phoneNumber,
		email: email
	};
}

add("chris","arnold","ch@tr","0208");

list();


///////////////////////////////////
///////////////////////////////////
// Objects I
///////////////////////////////////
///////////////////////////////////


//////////////
// Building an Address Book
//////////////


//////////////	Objects in address books are fun!
////// Lesson 1/6 Digitizing People



