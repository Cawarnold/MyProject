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
// Objects II
///////////////////////////////////
///////////////////////////////////


//////////////
// Building a cash register
//////////////


//////////////	Cha Ching!
////// Lesson 1/7 Shut the Shop!

// You are working for a large supermarket and the cash register 
// has just failed.
// The boss is not happy as he can't make any money.

// To save the day it happens that you let slip to your boss 
// that you know JavaScript and can build a quick virtual 
// cash register until head office sends support staff.

// Your boss is over the moon and wants you to get started right away.

//// Instructions:

// Create a new object called cashRegister with the property 
// total initialized to 0.

var cashRegister = {
	total: 0
};

console.log(cashRegister.total);

// Then change the property total to 2.99 using dot notation.

cashRegister.total = 2.99;
console.log(cashRegister.total);

//////////////	Cha Ching!
////// Lesson 2/7 Manually Add It Up?

// Great! The bossman can see that you can tell the cash register the total. 
// But we need the cash register to do more.

// Your boss wants a way to manually add the cost of each item. 
// We have written the add method for you. 
// There are two things we should note.

// We are using literal notation to include the method add.
// We've used the += operator. 
	// This is a shorthand way of saying
	// this.total = this.total + itemCost;

// In general, a += b; means "add b to a and put the result 
// of that addition back into a. 
// This is also available for the other basic arithmetic functions: 
// -=, *=, and /= do what you expect.

var cashRegister = {
    total:0,
    add: function(itemCost){
        this.total += itemCost;
    }
};

//call the add method for our items

//Show the total bill
console.log('Your bill is '+cashRegister.total);


//// Instructions:

// Use the add method to sum up the cost of the following four items.

	// Eggs 0.98
	// Milk 1.23
	// Magazine 4.99
	// Chocolate 0.45

// If we only call the method once, it will just add the first item. 
// So to add up the cost of four items, 
// how many times will we have to call the method?

cashRegister.add(0.98)
cashRegister.add(1.23)
cashRegister.add(4.99)
cashRegister.add(0.45)



//////////////	Cha Ching!
////// Lesson 3/7 Short-Term Memory

// But this method only works as long as you can remember the cost 
// of every item in the store. 
// We need something like a bar code scanner where just knowing 
// the item name will automatically add the cost of that item to the total.

// So we create a method called scan. 
// This method takes some 'item' parameter, 
// and adds the cost of this 'item' to the total. 
// 'item' is a string.

// We also use a switch statement. 
// Previously, we would have probably used multiple if-else statements. 
// Here, things work in a similar way.

// For example, if the item is "eggs" (line 8), 
// we then call the add method, passing through 0.98 as the itemCost. 
// This will add 0.98 to cashRegister.total. 

// If instead the item is "milk" or "chocolate" or "magazine", 
// the relevant itemCost is added. Note no default case is needed 
// for this switch statement.

//// Instructions:

// Write the add method which has a single parameter, itemCost. 
// It will add the itemCost to the total.

// We have partially written the scan method for you and started a switch statement.
// Add the following 2 items to the switch statement:
	// "magazine", 4.99
	// "chocolate", 0.45

// Finally, use the scan method to buy "eggs" twice and a "magazine" three times.

var cashRegister = {
    total: 0,
//insert the add method here    
    add: function (itemCost) {
    	this.total += itemCost;
    	return this.total;
    },
    
    scan: function (item) {
        switch (item) { 
        case "eggs": 
            this.add(0.98); 
            break;
        
        case "milk": 
            this.add(1.23); 
            break;
        
        //Add other 2 items here
        case "magazine":
        	this.add(4.99);
        	break;
        case "chocolate":
        	this.add(0.45);
        	break;        
        }
        return true;
    }
};

//Scan 2 eggs and 3 magazines
cashRegister.scan("eggs");
cashRegister.scan("eggs");
cashRegister.scan("magazine");
cashRegister.scan("magazine");
cashRegister.scan("magazine");

//Show the total bill
console.log('Your bill is '+ cashRegister.total);

//// CA: NOTICE how each part of the object is separated by commas.

// We know add and scan are both methods because they use the keyword function 
// and are found inside an object.
// In the scan method, we make use of the add method. 
// We call it with this so that add refers to its own defined method.
// Comma! don't forget that a comma (,) will be needed after closing the new add method.



//////////////	Cha Ching!
////// Lesson 4/7 I Have to Scan It More Than Once?

// Is that a smile on the boss's face? 
// Well, there was one until he realized that your system requires every item 
// to be scanned individually. 
// He finds this pretty inefficient and you probably agree. 
// Let's get real—it was pretty annoying having to call the scan method 
// five times in the previous exercise!

// What can we do? What is the limitation of the scan method? 
// Well, it has just one parameter, item, 
// and you can't specify anything related to quantity.

//// Instructions:

// Modify the scan method such that if we tell it the quantity of each item, 
// it will be able to add the right amount to the total. 
// Since you currently tell scan nothing about quantity, 
// it may be useful to create another parameter.

// Scan 4 of each item using your improved scan method. 
// Previously we would have needed to call scan 16 times! Now it is down to 4.

var cashRegister = {
    total:0,

    add: function(itemCost){
        this.total += itemCost;
    },
    // function(item,count=1) -- count=1 mean 1 is the default value of count.
    scan: function(item,count=1) {
        switch (item) {
        case "eggs": this.add(0.98*count); break;
        case "milk": this.add(1.23*count); break;
        case "magazine": this.add(4.99*count); break;
        case "chocolate": this.add(0.45*count); break;
        }
    }
};

// scan each item 4 times
//cashRegister.scan("eggs");
cashRegister.scan("eggs",4);
cashRegister.scan("milk",4);
cashRegister.scan("magazine",4);
cashRegister.scan("chocolate",4);

//Show the total bill
console.log('Your bill is '+cashRegister.total);

//// Hint:
// Modify the scan method to have a second parameter, quantity. 
// Now, we must call it using something like cashRegister.scan("chocolate", 1);
// In the scan method, we currently only add 0.45 when "chocolate" is passed. 
// How can we improve this? 
// Let's multiply this by the quantity parameter. 
// And we need to do this for each item.

// This means, for "chocolate", we need the code to be :
this.add(0.45 * quantity);
// Unit Test Our test expects the second parameter to be quantity as the examples above.


//////////////	Cha Ching!
////// Lesson 5/7 Bleep Bleep

// The boss looks down at his pager to see Register 8 needs assistance. 
// They have scanned an item too many times and need to void the last transaction.

// So he turns to you and says: "Okay JavaScript Ninja! What do we do now?!"

//// Instructions:

// We need to keep track of how much the last transaction was. 
// Modify the add method to keep track of the amount of the last transaction. 
// This should be tracked in a new property, lastTransactionAmount.

// Add a method called voidLastTransaction that subtracts 
// the last amount transacted from total.

// Then use the new method to void the last item we scanned. 
// Finally, scan only 3 of the same item instead.

var cashRegister = {
    total:0,
    lastTransactionAmount:0,
    //Dont forget to add your property
    add: function(itemCost) {
        this.total +=  itemCost;
        this.lastTransactionAmount = itemCost;
    },
    scan: function(item,quantity) {
        switch (item) {
        case "eggs": this.add(0.98 * quantity); break;
        case "milk": this.add(1.23 * quantity); break;
        case "magazine": this.add(4.99 * quantity); break;
        case "chocolate": this.add(0.45 * quantity); break;
        }
        return true;
    },
    //Add the voidLastTransaction Method here
    voidLastTransaction: function() {
    	this.total -= this.lastTransactionAmount;
    }
    
};

cashRegister.scan('eggs',1);
cashRegister.scan('milk',1);
cashRegister.scan('magazine',1);
cashRegister.scan('chocolate',4);

//Void the last transaction and then add 3 instead
console.log('Your bill is '+cashRegister.total);
cashRegister.voidLastTransaction();
cashRegister.scan('chocolate',3);

//Show the total bill
console.log('Your bill is '+cashRegister.total);


//////////////	Cha Ching!
////// Lesson 6/7 Over the Moon

// Great! The store is ticking along making money again. 
// The boss is so happy you have just been given a bonus staff discount 
// to the value of 20%.

// However the current system doesn't know how to apply the different 
// levels of staff discount that apply. 
// Now the rest of the staff is not happy and demanding you make improvements!

// Let's sort it out so that staff can get their well deserved discount.


//// Instructions:

// Create an object constructor called StaffMember which takes two parameters—name 
// and discountPercent. 
// And then have the (public) properties name and discountPercent equal the parameters.

// To help, we have already created two employees using this constructor. 
// Sally and Bob already have their staff discount set up: Sally getting 5% off 
// and Bob getting 10%.

// Create a new instance of the object for yourself called me with your massive staff 
// discount bonus of 20%.


// create a constructor for the StaffMember class
function StaffMember(name,discountPercent) {
	this.name = name;
	this.discountPercent = discountPercent;
}


var sally = new StaffMember("Sally",5);
var bob = new StaffMember("Bob",10);

//Create a StaffMember for yourself called me
var me = new StaffMember("CA",20);



//////////////	Cha Ching!
////// Lesson 7/7 You Deserved It!

// Whew! It's been a long day fixing cash registers and now let's actually apply 
// our well-earned discount. 
// Now that we have our objects representing the staff, 
// let's update our cash register to actually apply the discount.

//// Instructions:

// On line 10 create a new object called me of type StaffMember 
// for yourself with a staff discount of 20%

// Create a new method called applyStaffDiscount in the cashRegister object 
// which accepts a parameter employee. When this method is called, 
// cashRegister should apply the staff member's discountPercent to total.

// Under the comment, 'Apply your staff discount by passing the me object, 
// call your new applyStaffDiscount and pass the object me.


function StaffMember(name,discountPercent){
    this.name = name;
    this.discountPercent = discountPercent;
}

var sally = new StaffMember("Sally",5);
var bob = new StaffMember("Bob",10);

// Create yourself again as 'me' with a staff discount of 20%
var me = new StaffMember("CA",20);

var cashRegister = {
    total:0,
    lastTransactionAmount: 0,
    add: function(itemCost){
        this.total += (itemCost || 0);
        this.lastTransactionAmount = itemCost;
    },
    scan: function(item,quantity){
        switch (item){
        case "eggs": this.add(0.98 * quantity); break;
        case "milk": this.add(1.23 * quantity); break;
        case "magazine": this.add(4.99 * quantity); break;
        case "chocolate": this.add(0.45 * quantity); break;
        }
        return true;
    },
    voidLastTransaction: function(){
        this.total -= this.lastTransactionAmount;
        this.lastTransactionAmount = 0;
    },
    // Create a new method applyStaffDiscount here
    applyStaffDiscount: function(employee){
    	StaffMember.employee
    }
    
};

cashRegister.scan('eggs',1);
cashRegister.scan('milk',1);
cashRegister.scan('magazine',3);
// Apply your staff discount by passing the 'me' object 
// to applyStaffDiscount


// Show the total bill
console.log('Your bill is '+cashRegister.total.toFixed(2));




















