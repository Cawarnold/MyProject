// Guide


///////////// Summary notes /////////////

//// Run JavaScript from your cmd ////
// install node.js
// update PATH: C:\Users\U6030064\AppData\Roaming\npm;C:\Program Files\nodejs
// go to terminal, navigagte to file, run:
// node filename.js


//// Basics ////




// Find type of object & hasOwnProperty
console.log(typeof Object.prototype);
console.log(Object.prototype.hasOwnProperty("hasOwnProperty"));

// Accessing the key / value of an object

// create object
var languages = {
    english: "Hello!",
    french: "Bonjour!",
    notALanguage: 4
};

// access key / value pari of object
console.log(typeof languages);
for (var key in languages) {
	var value = languages[key];
	if (typeof value === "string") {
		console.log(value);
	};
};



//// OOP - object-oriented programming ////

// A class can be thought of as a type, or a category of objects—kind of like how Number 
// and String are types in JavaScript.
// So we know that a class will have certain properties and methods, 
// "prototype" is what JavaScript uses to keep track of the properties
// and methods of an object.

// Create Class called "Dog", with a property "breed" and "bark".
function Dog (breed) {
  this.breed = breed;
  this.numLegs = 4;
  this.age = 8; // private variable (can only be accessed from within the class)
  this.bark = function() {
  	console.log("Woof");
  };
  this.sayName = function () {
	    console.log("Hi my name is " + this.name);
  var owner = function() {
      return "bob"; // private method
   };
};

// Same as 
function Dog (breed) {
  this.breed = breed;
};
// Make all Dogs bark:
Dog.prototype.bark = function() {
  console.log("Woof");
};
// Make all Dogs sayName:
Dog.prototype.sayName = function() {
	console.log("Hi my name is " + this.name);
}

// How many legs does hudson have?
var hudson = new Dog("Retriever");
console.log(emperor.numLegs);


//// Four major principles of Object-Oriented Programming (OOP) ////

// Encapsulation, Data Abstraction, Polymorphism and Inheritance



// Inheritance (DRY - Don't Repeat Yourself)



///////////////////////////////////////////////////////////////////////////////////////
//        								Codecademy
///////////////////////////////////////////////////////////////////////////////////////

//// Resources:

//  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array



//////////////////////////////////////
// Learn - JavaScript  
// https://www.codecademy.com/learn/learn-javascript
//////////////////////////////////////


//////////////
// Building Blocks
//////////////


//////////////
////// Lesson 1/8 Introduction

// Welcome to Learn JavaScript!

// JavaScript is the most widely used programming language on the web 
// and is used on most websites, including this one.

// By the end of this course, you'll have a strong foundation in JavaScript. 
// You'll be able to write full-fledged programs, make HTML and CSS dynamic,
// and write impressive web applications.


// This unit has two parts:

	// Learn the building blocks of JavaScript
	// Do some fun stuff with those parts

// Because this course starts with the building blocks of JavaScript, 
// make sure to take notes and pace yourself. 
// This foundation will take us through the rest of the JavaScript course.


//////////////
////// Lesson 2/8 Types

// The building blocks of JavaScript make up every program and line of JavaScript.

// Just like a language has nouns, verbs, and prepositions, 
// JavaScript has its own building blocks. 
// Instead of calling them building blocks, however, developers call them data types.


// There are three essential data types to know for now, 
// and here is your first test of memorization 
// (don't worry, we will practice):

	// String: Any grouping of words or numbers surrounded by 
			//	single quotes: ' ... ' or double quotes " ... ".

	// Number: Any number, including numbers with decimals, 
			// without quotes: 4, 8, 1516, 23.42.

	// Boolean: This is always one of two words. 
			// Either true or false, with no quotations.


//// Question:

	// In the code editor, there are three variables 
	// (we will learn about variables in the next lesson). 
	// For now, replace each variable's value with each corresponding type.

	// On line 1, there's a variable named myString equal to undefined. 
	// Replace undefined, with a string of your name.

//// Console Before:
var myString = 'undefined';
var myNumber = undefined;
var myBoolean = undefined;


// Do not edit the code under this line
console.log("Name: " + myString);
console.log("Lucky Number: " + myNumber);
console.log("Good joke? " + myBoolean);

//// Console After:
var myString = 'Christian';
var myNumber = 28;
var myBoolean = true;


// Do not edit the code under this line
console.log("Name: " + myString);
console.log("Lucky Number: " + myNumber);
console.log("Good joke? " + myBoolean);


//////////////
////// Lesson 3/8 console

// We can't do much programming with our knowledge of types right now, 
// so let's build something cool. 
// Let's learn how to ask JavaScript to talk to us.

// To do this, we need two things:

// A way to ask JavaScript to talk.
// Something for JavaScript to say.
// We can ask JavaScript to print words to the console with this line of code:

console.log('Your message here.');

// In human-speak, this is saying: 
	// "Hey console, please print/log this thing inside the parentheses. Bye, thanks!"

// By writing this line, we've also solved the second thing we need: 
// Something for JavaScript to say. 
// We can put a String, Number, or Boolean (or any data type) 
// inside the parentheses of a console.log statement.


// Fun fact: We can log multiple things at once by separating them with commas, like this:

console.log('bacon', 'pesto');

// Use console.log to print out two of your favorite pizza toppings (plural).

//// Console:

console.log("Chorizo", "tomato");


//////////////
////// Lesson 4/8 Math Operators

// Don't worry, math does not need to be your strong-suit to learn JavaScript. 
// There are just a few operations we'll need to know 
// to make some awesome programs later in the course!).

// JavaScript includes the general math operators that you can find on a calculator:

	// Add: +
	// Subtract: -
	// Multiply: *
	// Divide: /

// These all work how you might guess: 3 + 4 will equal 7, 50 / 10 will equal 5.

// Let's use each one of these math operators.

//// Instructions:

// Inside of a console.log:
	// add 3.5 to your age.
	// take the current year and subtract 1969.
	// then divide 65 by 240.
	// then multiply the full answer from step 3 by 100.

//// Console:

console.log(38+3.5);
console.log(2016-1969);
console.log(65/240);
console.log(65/240*100);


//////////////
////// Lesson 5/8 Math Operators II

// Now let's generate a space fact 
// while we learn a brand new operator called the modulus.

// The idea behind the modulus is to show you the remainder after you divide a number.

// So, if you divide 13 / 5, 5 goes into 13 two times, 
// and there will be 3 remaining. A modulus, denoted by a %,
// would take 13 % 5 and return the remainder 3.

// How on Earth is this useful?
// Let's ask a question a modulus can solve:
	// What will the moon phase be one year from today?

//// Instructions:

// Let's say it's a full moon tonight, 
// and we want to know what the moon will look like one year from today. 
// We know from the moon phase image to the right that 
// the moon circles the Earth every 27 days, 
// so let's start by dividing 365 by 27.

// Remember to put your calculations inside console.log to print them to the screen.

//// Console:

console.log(365/27);

// That gives us a number (13), followed by a decimal(.518...).
// To figure out what phase the moon will be in a year, 
// we need to know how many extra days the moon will rotate 
// around the earth before the end of the year. 
// We need the decimal we just found displayed as remaining days.
// Use the modulus operator to find the remaining days, then run your code.

console.log(365%27);

// Now we know how many days into the moon's phase it will be in exactly one year.

// We can now figure out, based on the moon phase image, 
// what the moon phase will be 365 days from today. 
// If it's a full moon today, a year from now it will be a new moon.


//////////////
////// Lesson 6/8 Random

// As it turns out, JavaScript has some tricks up its sleeve to make our lives easier.

// JavaScript has built in functions, which help us do everyday things. 
// We'll learn more about functions later in the course, 
// so don't worry about understanding what they are right now.

// Sometimes it's necessary to generate a random number within a program. 
// We can do that with this code:

Math.random();

// This code will return a random number between 0 and 1. 
// JavaScript will generate a random number for us with this code.

// To generate a random number between 0 and 50, 
// we could multiply this result by 50, like so:

Math.random() * 50;

// The problem with this is that the answer will most likely be a decimal. 
// Luckily, JavaScript has our back with another built in function called Math.floor. 
// Math.floor will take a decimal number, 
// and round down to the nearest whole number. It is used like this:

Math.floor(Math.random() * 50);

// In this case:
// Math.random will generate a random number between 0 and 1.
// We then multiplied that number by 50, so now we have a number between 0 and 50.
// Then, Math.floor will round the number down to the nearest whole number.
// Let's utilize these two methods to generate a random number between 0 and 100.


//// Instructions:

// Inside of a console.log, create a random number with Math.random, 
// then multiply it by 100.

// If you run the program few times, you'll see random numbers in the console.

//// Console:

console.log(Math.random() * 100);

// Now, utilize Math.floor to make the output a whole number.

// Inside the console.log you wrote in the last step, 
// put Math.random() * 100 inside the parentheses of Math.floor.

//// Console:

console.log(Math.floor(Math.random() * 100));


//////////////
////// Lesson 7/8 Comments

// As we write JavaScript, we can create comments in our code.

// Comments are lines that are not evaluated when the code runs. 
// They exist just for human readers, in other words. 
// Comments can be extremely useful when we're looking back at code 
// we've written later on and for other people who will be looking at your code.

// There are two types of code comments in JavaScript:

	// A single line comment will comment out a single line, 
	// and is denoted with two forward slashes // preceding a line of JavaScript code.

// The first 5 decimals of pi
console.log('Pi is equal to ' + 3.14159);

	// A multi-line comment will comment out multiple lines, 
	// and is denoted with /* to begin the comment, and */ to end the comment.

/*
console.log('All of this code');
console.log('Is commented out');
console.log('And will not be executed);
*/

//// Instructions:

// Let's practice adding some code comments.

// To the right, we've provided you with the beginning 
// of the book Catch-22 by Joseph Heller.

// On line 1, write a single line comment that says 'Opening line'.

// Single line comments are great for adding context to your code.

// Multi-line comments are often best suited to prevent 
// a block of code from running. Comment out lines 4 - 9 with a multi-line comment.

// Opening line
console.log('It was love at first sight.');

/*console.log('The first time Yossarian saw the chaplain he fell madly in love with him.');
console.log('Yossarian was in the hospital with a pain in his liver that fell just short of being jaundice.');
console.log('The doctors were puzzled by the fact that it wasn\'t quite jaundice.');
console.log('If it became jaundice they could treat it.');
console.log('If it didn\'t become jaundice and went away they could discharge him.');
console.log('But this just being short of jaundice all the time confused them.');*/


//////////////
////// Lesson 8/8 Review Types and Operators

// Let's take one more glance at the concepts we just learned:

// There are three essential data types in JavaScript: strings, numbers, and booleans.
// We can write out anything to the console with console.log.
// We can do math with operators like +, -, *, and /.
// We can find the remainder after dividing two numbers with a modulus: %.
// We can generate a random number with Math.random, 
	// then make it a whole number with Math.floor.
// We write a single line comment with // and a multi-line comment with /* and */.
// You've just finished one of the toughest parts of this course, nice work!


//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Variables
//////////////

//////////////
////// Lesson 1/6 Variables

// To write programs in JavaScript, we'll need to make our code reusable.

//  Part of making code reusable is removing the data we want to perform 
// some logic on to leave only the logic. 
// Then we can use our logic on any data. 

// Here's what we mean:
// Imagine you're writing a weather app. 
// Your thermometer outside reports the temperature in Celsius 
// and your goal is to report the temperature in Fahrenheit.

// You write a program that takes a temperature like 15 degrees Celsius, 
// then multiplies and divides it until you get the temperature in Fahrenheit.

// Once you've done this though, you see the temperature now reads 16 degrees Celsius. 
// In order to find Fahrenheit again, you'd need to write a whole new program 
// to convert 16 degrees Celsius to Fahrenheit.

// This would happen because the Celsius-to-Fahrenheit logic 
// is operating directly on the Celsius data.

// Luckily, JavaScript offers variables. 
// Variables allow us to assign data to a word, 
// then we can use that word within our program instead of the data. 
// Then, if the variable's value changes we only have to change 
// the variable's value instead of re-writing the entire program.


//////////////
////// Lesson 2/6 Create a Variable

// Let's dive in and see a variable in the wild. Here is how you declare a variable:

var myName = 'Arya';
console.log(myName);
// Output: Arya

// You can almost read it aloud: "Variable myName is equal to Arya."

// Let's dissect that statement and look at its parts:

	// var, short for variable, 
			//is the JavaScript keyword that will create a new variable for us.
	// myName is chosen by a developer (that's you!). 
			// Notice that the word has no spaces, 
			// and each new word is capitalized. 
			// This is a common convention in JavaScript, 
			// and is called camelCase.
	// = means to assign whatever's next to the variable.
	//'Arya' is the value that the equals = assigns into the variable myName.

// After the variable is declared, 
// we can print the variable with: console.log(myName). 
// This will print 'Arya' to the console.

//// Instructions:

// Variables must be strong to hold all of our stuff. Exactly how strong are they?
// Create a variable named strength, and assign the string '50,000 pounds' to it.

//// Console 1:

var strength = '50,000 pounds';

// Now, under the strength variable, type

//// Console 2:

console.log('How much stuff can a variable hold? ', strength);

// Now we know: What can a variable hold? Just about anything!


//////////////
////// Lesson 3/6 Create a Variable II

// If variables can hold strings, can they hold other data types? 
// Let's give it a shot:

var myAge = 15;
var likesChocolate = true;

console.log(myAge);
// Output: 15

console.log(likesChocolate);
// Output: true

// Variables can hold any data type, like strings, numbers, and Booleans. 
// They can also hold data types that we have not learned yet, 
// like arrays, functions and objects (more on that later).


//// Instructions:

// Under the strength variable, create a new variable named age 
// and set it equal to your age as a number.

var age = 28;

// Under your age variable, use console.log to print it to the console.

console.log(age);

// Now, create another variable named hasPet, and set it equal to a boolean.
// Then, print it to the console with console.log.

var hasPet = false;
console.log(hasPet);


//////////////
////// Lesson 4/6 Changing a Variable's Value

// Why do we care about variables?

// Variables are useful in two ways:

// They allow us to use the same value over and over, 
/// without having to write a string or other data type over and over.

// More importantly, we can assign variables different values 
// that can be read and changed by the program without altering our code.

// For example, a weather app can show you a different high temperature every day. 
// Instead of writing a new website everyday, 
// they store the information in a variable 
// and just change the value of that variable.

// We can change a variable's value if we want, like this:

var weatherCondition = 'Monday: Raining cats and dogs';
weatherCondition = 'Tuesday: Sunny';

console.log(weatherCondition); 
// Output: 'Tuesday: Sunny'

// We created a variable by using the keyword var and the name weatherCondition.
// Then, we took the existing weatherCondition variable, 
// and set its value equal to 'Tuesday: Sunny'.
// True to their name, variables are indeed variable.

//// Instructions:

// Create a variable on line 1 named morningAlarm and set it to '6:30AM'.

var morningAlarm = '6:30AM';

// On line 2, set morningAlarm equal to another time that's better for you, that is not at 6:30AM.

morningAlarm = '7:30AM';

// On line 3, use

console.log('Morning alarm is set to: ', morningAlarm)
// to print out your alarm to the console.
// Notice that you successfully changed the variable's value 
// because of your code on line 2.


//////////////
////// Lesson 5/6 String Interpolation


// In the previous lessons, we've put strings into variables. 
// Now, let's put a variable's value into a string!

// Putting a variable in a string uses concepts we've already learned. 
// The JavaScript term for this idea is interpolation.

// Interpolwhat?! —Possibly the most fun JavaScript term to say.

// We can use the + operator from earlier to interpolate (insert) 
// a variable into a string, like this:

var myPet = 'armadillo';
console.log('I own a pet ' + myPet + '.'); 
// Output: 'I own a pet armadillo.'


//// Instructions:

// Create a variable named favoriteAnimal and set it equal to your favorite animal.

var favoriteAnimal = 'Lion';

// Then, use console.log to print: 'My favorite animal: Koala', 
// but replace 'Koala' with your favoriteAnimal variable.

console.log('My favorite animal: ' + favoriteAnimal);


//////////////
////// Lesson 6/6 Review Variables

// You made it to the end of the first unit and this lesson! High five!

// We learned:

	// How to create variables.
	// How to change a variable's value.
	// How to interpolate, or insert, a variable into a string.

//In the next lesson, we will learn how to program JavaScript 
// to make decisions for us and how to generate random numbers. 
// Let's go!


//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Control flow
//////////////

// https://www.codecademy.com/en/courses/learn-javascript/lessons/control-flow/exercises/control-flow-intro?action=lesson_resume

//////////////
////// Lesson 1/8 Introduction to Control Flow

// Now that we've got the parts of JavaScript, let's see what they can do. 
// In this unit, we'll explore how we can take those parts, 
// and create decision trees, games, and much more.

// In programming, making decisions with code is called control flow.

// For instance, if we were making a choose-your-own-adventure game, 
// we'd need to program a way for a user to choose which plot line 
// they'd like to pursue. 
// Control flow statements enable JavaScript to make those decisions 
// by executing different code based on a condition.

// In this lesson, we'll learn how to make decisions with JavaScript 
// and how it can control the program's flow.


//////////////
////// Lesson 2/8 if/else Statements

// If you think about what we've been doing so far, 
// we've been writing instructions for computers.

// That's all programming really is: a list of instructions for computers.

// The main difficulty of being a developer is translating our ideas 
// in human-speak into ideas in computer-speak.

// Let's learn how we can ask JavaScript to think like us and make decisions like us.

// Let's start with human-speak. 
// Many decisions we make everyday boil down to this sentence in some form:

// "If something is true, let's do option 1, or else, if it is false, let's do option 2."

// This sentence looks fairly similar when we write it with JavaScript. See for yourself:

var needCoffee = true;
if (needCoffee) {
    console.log('Finding coffee');
} else {
    console.log('Keep on keeping on!');
}

// If the variable needCoffee is true, JavaScript will run one code block, 
// and if a variable is false, it will run another.

// needCoffee is the condition we are checking inside the if's parentheses. 
// Since it is equal to true, our program will run the code 
// between the first opening curly brace 
// { (line 2) and the first closing curly brace } (line 4). 
// It will completely ignore the else { ... } part. 
// In this case, we'd see 'Finding coffee' log to the console.

// Note: Code between curly braces are called blocks. 
// if/else statements have two code blocks.

// If we adjusted needCoffee to be false, only the else's console.log will run.
// if/else statements are how we can process yes/no questions programmatically.


//// Instructions:

// Create a variable named harryPotterFan and set it equal to a boolean, 
// based on your preference.
 
var harryPotterFan = false;

if (harryPotterFan) {
  console.log('Potter wins');
}
else {
  console.log('Voldemort wins');
}

// Then, write an if/else statement that uses harryPotterFan as its condition. 
// If it is true, then log, 'Mischief managed.'. 
// If it is false, then log, 'I lead a muggle\'s life.'.

// Note: Why is there a \ in 'I lead a muggle\'s life.'? 
// Since the string is surrounded by single quotes, 
// we can use a back slash to add a single quote within the string. 
// This is called escaping a character.

var harryPotterFan = false;

if (harryPotterFan) {
  console.log('Mischief managed.');
}
else {
  console.log('I lead a muggle\'s life.');
}


//////////////
////// Lesson 3/8 Comparison Operations

// if/else statements are made even more powerful with comparison operators.

// There are two comparisons you might be familiar with:
	// Less than: <
	// Greater than: >

// You may also recognize these:
	// Less than or equal to: <=
	// Greater than or equal to: >=

// Comparisons need two things to compare 
// and they will always return a boolean (true or false).

// How can we use comparisons and an if/else statement to see if it's time to eat?


//// Instructions:

// Write a variable named hungerLevel and set it equal to 5.

var hungerLevel = 5;

// Write an if/else statement that checks if hungerLevel is greater than 7. 
// If so, log 'Time to eat!', and if it is less than 7, log 'Let\'s eat later.'.

var hungerLevel = 5;

if (hungerLevel > 7) {
  console.log('Time to eat!');
}
else {
  console.log('Let\'s eat later.');
}

// Notice that since hungerLevel is 5, the if statement evaluates to false, 
// therefore the else's code block runs.

// Now set the hungerLevel variable equal to 10 and run your code again.

var hungerLevel = 5;

if (hungerLevel > 7) {
  console.log('Time to eat!');
}
else {
  console.log('Let\'s eat later.');
}

// Now it's 'Time to eat!'

// We can use the <, >=, and <= to compare variables in an if/else statement, 
// which is a powerful way to make decisions in JavaScript.

// Play around with these operators and values to see how exactly they work.


//////////////
////// Lesson 4/8 Comparison Operations II

// werewolf.js

// There are two more extremely useful comparisons we can make. 
// Often times, we might want to check if two things are equal, or if they are not.

// To check if two things equal each other, we can use === (three equals in a row).
// To check if two things do not equal each other, 
// we can write !== (exclamation with two equals in a row).

// Slow down here, this can be easily confused with creating variables. 
// Variables use one equals sign = to assign a value to a variable. 
// When you're comparing two variables, make sure to use three ===.

// How can we utilize === or !== and an if/else statement 
// to write a program to see whether a werewolf will turn 
// into its wolf form this evening?


//// Instructions:

// Write a variable named moonPhase and set it equal to 'full'.

var moonPhase = 'full';

// Write an if/else statement that checks if the moon is full. 
// If the moonPhase is 'full', log 'Howwwwlll!!' to the console,
// and if it is anything else, log 'I swear I am not a werewolf...'.

var moonPhase = 'full';

if  (moonPhase === 'full') {
  console.log('Howwwwlll!!');
}
else {
  console.log('I swear I am not a werewolf...');
}

// Notice the code inside the first block of curly braces { } ran. 
// That's because moonPhase equals 'full', 
// and therefore the condition evaluates to true.


//////////////
////// Lesson 5/8 else if statements

// if/else statements are either this or that for us right now. 
// They answer questions that are either yes or no.

// What can we do if we have a question that has multiple yes conditions, 
// or multiple no conditions?

// We can add more conditions to our if/else statement with: else if. 
// Check out how this fits into our current knowledge of if/else statements:

var stopLight = 'green';

if (stopLight === 'red') {
  console.log('Stop');
} else if (stopLight === 'yellow') {
  console.log('Slow down');
} else if (stopLight === 'green') {
  console.log('Go!');
} else {
  console.log('Caution, unknown!');
}

// 1. We created a variable named stopLight that is assigned to the String 'green'.

// 2. Then, there's an if/else statement with multiple conditions, using else if. 
	// else if allows us to find multiple states of the stopLight variable, 
	// and output different things based on its color.

// 3. The whole thing ends with the singular else we know and love. 
	// The else is a catch-all for any other situation. 
	// For instance, if the stopLight was blinking blue, 
	// the last else would catch it and return a default message.


//// Instructions:

// We all know that turning into a werewolf is not an instant thing. 
// It happens in stages. 
// So let's expand our program from before to accommodate that fact.

// If the moon is 'mostly full', log 'Arms and legs are getting hairier' 
// If the moon is 'mostly new', log 'Back on two feet'.

// If someone enters in an invalid moon phase, 
// make sure to the final else to log 'Invalid moon phase'.

var moonPhase = 'full';

if  (moonPhase === 'full') {
  console.log('Howwwwlll!!');
}
else if (moonPhase === 'mostly full') {
	console.log('Arms and legs are getting hairier');
}
else if (moonPhase === 'mostly new') {
	console.log('Back on two feet');
}
else {
  console.log('Invalid moon phase');
}


// Set moonPhase to 'mostly full' and run your code.
// We expect 'Arms and legs are getting hairier' to log to the console.

// Set moonPhase to 'mostly new' and run your code.
// We expect 'Back on two feet' to log to the console.

// Now set moonPhase to 'solar eclipse' and run your code.

// Since there is not an else if condition for 'solar eclipse', 
// we expect the default else code block to run. 
// You should see 'Invalid moon phase' print to the console.

// Nice work! We just made a decision tree with multiple conditions 
// using an if statement with else if conditions.


//////////////
////// Lesson 6/8 Logical Operations

// So far, we've been able to translate certain thoughts into JavaScript code, 
// like, "Are these things equal?" with ===, 
// or, "Is one thing greater than another thing?" with >.

// In English, sometimes we say "both of these things" 
// or "either one of these things." 
// Let's translate those phrases into JavaScript 
// with some special operators called logical operators.

// To say "both must be true," we can use &&.
// To say "either can be true," we can use ||.
// To say "I want to make sure this is the opposite of what it really is," we can use !.
// To say "these should not be equal to each other," we can use !==.

// For example:

if (stopLight === 'green' && pedestrians === false) {
  console.log('Go!');
} else {
  console.log('Stop');
}

// In the example above, we make sure that the stopLight is 'green' 
// and && there are no pedestrians before we log 'Go!'.

// If either of those conditions are false, we log 'Stop'.
// Just like the operators we learned previously, 
// these logical operators will return either true or false.

// These logical operators are helpful when writing if/else statements, 
// since they let us make sure multiple variables are true or false.


//// Instructions:

// Let's say the werewolf can only become its wolf form 
// when there is a full moon and it's a foggy night.

// We already have a moonPhase variable, 
// so let's start with making a foggyNight variable set equal to true.

var moonPhase = 'solar eclipse';
var foggyNight = true;

// Now, set moonPhase to 'full' again. Now that we have both conditions, 
// let's write that in our if/else statement.

// In the first condition of the if/else statement, 
// make sure that moonPhase === 'full' and foggyNight are true, using &&.

// Note: if/else statements check the true-ness or false-ness of variables, 
// so there's not need to write foggyNight === true. 
// You only need to write foggyNight, and you'll get the same result.

// Once you've added it, click 'Run'.

var moonPhase = 'full';
var foggyNight = true;

if  (moonPhase === 'full' && foggyNight) {
  console.log('Howwwwlll!!');
}
else if (moonPhase === 'mostly full') {
	console.log('Arms and legs are getting hairier');
}
else if (moonPhase === 'mostly new') {
	console.log('Back on two feet');
}
else {
  console.log('Invalid moon phase');
}


// Now, change the foggyNight variable to equal false and run it again.

// Notice that the default else will print to the console.
// That's because && requires both moonPhase and foggyNight to be true 
// to execute its code block.

// Now, let's try out ||. 
// Use || in place of the && that you wrote in the previous steps 
// to make the if/else statement print 'Howwwlll!!!' 
// if moonPhase is 'full' or if foggyNight is true.

// Leave the moonPhase variable's value as 'full' 
// and the foggyNight variable's value as false.

var moonPhase = 'full';
var foggyNight = false;

if  (moonPhase === 'full' || foggyNight) {
  console.log('Howwwwlll!!');
}
else if (moonPhase === 'mostly full') {
	console.log('Arms and legs are getting hairier');
}
else if (moonPhase === 'mostly new') {
	console.log('Back on two feet');
}
else {
  console.log('Invalid moon phase');
}

// The first if statement's block was executed. 
// That's because moonPhase is 'full', which is true. 
// The || operator only needs one thing to be true in order to return true.


//////////////
////// Lesson 7/8 switch Statements

// Before we move on, let's circle back to else if statements.

// Using else if is a great tool for when we have a few different conditions 
// we'd like to consider.

// else if is limited however. 
// If we want to write a program with 25 different conditions, 
// like a JavaScript cash register, we'd have to write a lot of code, 
// and it can be difficult to read and understand.

// To deal with times when you need many else if conditions, 
// we can turn to a switch statement to write more concise and readable code.

// Note: To a computer, a switch statement and an if/else statement are the same, 
// but a switch statement can be easier for other humans to read. 
// Part of being a good developer is writing code that both computers 
// and other humans can read.

// switch statements look like this:

var groceryItem = 'papaya';

switch (groceryItem) {
  case 'tomato':
    console.log('Tomatoes are $0.49');
    break;
  case 'lime':
    console.log('Limes are $1.49');
    break;
  case 'papaya':
    console.log('Papayas are $1.29');
    break;
  default:
    console.log('Invalid item');
    break;
}

// The switch keyword initiates the statement, and is followed by ( ... ), 
// which contains the condition that each case will compare to. 
// In the example, the condition is groceryItem.

// Inside the block, { ... }, there are cases. 
// case is like the else if part of an if/else if/else statement. 
// The word following the first case is 'tomato'. 
// If groceryItem equalled 'tomato', that case's console.log would run.

// groceryItem equals 'papaya', so the first and second case statements are skipped. 
// The third case runs since the case is 'papaya' matches groceryItem's value. 
// This particular program will log out: 'Papayas are $1.29'.

// Then the program stops with the break keyword. 
// This keyword will prevent the switch statement from executing any more of its code.

// At the end of each switch statement, there is a default condition. 
// If none of the cases are true, then this code will run.


//// Instructions:

// Let's illustrate this by converting our werewolf program to a switch statement. 
// For now, let's also delete the foggyNight variable so it doesn't fog up this concept.

// moonPhase will become the condition of the switch statement. 
// Then, each moon phase will become each case that the switch statement checks for.

// Start by writing a switch statement with moonPhase as its condition.

var moonPhase = 'full';

switch  (moonPhase) {
  case 'full':
    console.log('Howwwwlll!!');
    break;
  case 'mostly full':
    console.log('Arms and legs are getting hairier');
    break;
  case 'mostly new':
    console.log('Back on two feet');
    break;
  default:
    console.log('Invalid moon phase');
    break;    
}

// Then, write each else if condition as a case.

// If moonPhase is 'full', then use console.log to print 'Howwwwlll!!'.

// If moonPhase is 'mostly full', then use console.log to print 
// 'Arms and legs are getting hairier'.

// If moonPhase is 'mostly new', then use console.log to print 'Back on two feet'.

// Remember to add a break after each console.log, 
// like in the example in the instructions.

// Now, add a default at the end of the switch that uses console.log to print 
// 'Invalid moon phase', 
// in the case that moonPhase does not equal one of our cases.

//////////////
////// Lesson 8/8 Review Control Flow

// Way to go! We just learned a lot of control flow concepts:

// if/else statements make binary decisions 
// and execute separate code based on a condition.
// We can add extra conditions with to if/else statements with else if conditions.
// switch statements make complicated if/else statements easier to read, 
// however they achieve the same result as if/else statements.

// Comparison operators, like <, >, <=, and >= can compare two variables. 
// After they compare, they always return either true or false.

// Logical Operators, like &&, ||, !==, and !, can compare two variables 
// to see if a certain condition exists:
	// && checks if both sides are true.
	// || checks if either side is true.
	// !== checks if both sides are not equal.
	// ! changes a variable that is true to false, and vice versa.

// In the next lesson, we'll learn about functions, 
// and how to write blocks of code that are reusable.


//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Functions
//////////////

// https://www.codecademy.com/en/courses/learn-javascript/lessons/functions/exercises/intro-to-functions?action=lesson_resume&link_content_target=interstitial_lesson

//////////////
////// Lesson 1/7 Introduction to Functions

// A function is a block of code designed to perform a task.

// Functions are like recipes. 
// They take data or variables, perform a set of tasks on them, 
// and then return the result. 

// The beauty of functions is that they allow us to write a chunk of code once, 
// then we can reuse it over and over without writing the same code over and over.

// Take a look at this code:

var calculatorOn = false;

function pressPowerButton() {
  if (calculatorOn) {
    console.log('Calculator turning off.');
    calculatorOn = false;
  } else {
    console.log('Calculator turning on.');
    calculatorOn = true;
  }
}

pressPowerButton();
// Output: Calculator turning on.

pressPowerButton();
// Output: Calculator turning off.


// This code turns the calculator on if it is currently off, 
// and turns it off if the calculator is currently on.

// See if you can figure out how this code works. 
// In the next exercise, we'll walk through it line by line.


//////////////
////// Lesson 2/7 Functions

// How does this code work?

var calculatorOn = false;

function pressPowerButton() {
  if (calculatorOn) {
    console.log('Calculator turning off.');
    calculatorOn = false;
  } else {
    console.log('Calculator turning on.');
    calculatorOn = true;
  }
}

pressPowerButton();
// Output: Calculator turning on.

pressPowerButton();
// Output: Calculator turning off.

// On line 1, we have a variable named calculatorOn set to false. 
// Our program starts with the calculator in the off position.

// On line 3, there's a function named pressPowerButton. 

// Functions follow this syntax:

	// • They begin with the JavaScript keyword function.

	// • After function comes the name of the function. 
		// pressPowerButton is the name of the function. 
		// Notice there are no spaces in the name and 
		// each new word is capitalized. 
		// This is a convention in the JavaScript community called camelCase.

	// • After the function's name, comes parentheses (). 
		// We'll learn about these in the next exercise.

	// • Finally, the function has a block of code it executes 
		// between the curly braces {}.

// Inside the function is an if/else statement.
// On the last few lines, we make the function run by writing pressPowerButton(). 
// This term for this is calling the function. 
// We call it with pressPowerButton(), 
// and it runs all the code in the block of the function.

// We executed the code in the block of the function 
// twice without having to write it twice. 
// Functions can make code reusable!


//// Instructions:

// Imagine you work at a pizza restaurant 
// and you want to write a JavaScript program 
// to take orders so you don't have to write them out by hand. 

// You can write a function to perform this task!

// Start by writing a function named takeOrder. 
// Inside of its block, use console.log to print 'Order: pizza'.

function takeOrder(){
  console.log('Order: pizza');
}

// Under the function, let's take an order.

// Call the takeOrder function on the last line.

takeOrder();


//////////////
////// Lesson 3/7 Parameters

// The calculator program should be able to perform a math operation on a number. 
// We should be able to give a calculator a number, 
// have it perform a task on it like multiplication, then print a result.

// Currently, we have no way to give a function a number. 
// To do this, we can use parameters. 
// Parameters are variables that we can set when we call the function. 

// For example:

function multiplyByThirteen(inputNumber) {
  console.log(inputNumber * 13);
}

multiplyByThirteen(9);
// Output: 117

// We added inputNumber within the parentheses of the multiplyByThirteen function. 
// inputNumber is a parameter.

// Inside the multiplyByThirteen function, 
// we use console.log to print the inputNumber by 13.
// When we call the multiplyByThirteen function on the last lines, 
// we set the inputNumber parameter. 
// For instance, multiplyByThirteen(9) calls the multiplyByThirteen function, 
// and sets inputNumber as 9. 
// Then, inside the block of the multiplyByThirteen function, 
// 9 is multiplied by 13, resulting in 117 printing to the console.

// Note on terminology: inputNumber is a parameter, 
// but when we call multiplyByThirteen(9), the 9 is called an argument. 
// Therefore, arguments are provided when you call a function, 
// and parameters receive arguments as their value. 
// So, inputNumber is a parameter and its value is the argument 9, 
// since we wrote multiplyByThirteen(9).

// Parameters let us write logic inside functions 
// that can be modified based on when we call the function, 
// which will help make our functions more flexible.


//// Instructions:

// Let's include a parameter in the takeOrder function 
// to make the orders we log to the console more descriptive.

// Inside the parentheses of the takeOrder function, add a parameter named topping.

function takeOrder(topping){
  console.log('Order: pizza' + ' topped with ' + topping);
}

takeOrder('chorizo');

// Now, let's include the topping parameter inside the takeOrder function.

// Modify the console.log to interpolate the topping parameter 
// to print a string like this:

	// Order: pizza topped with bacon

// At the end of the program, modify the takeOrder function call 
// to include an argument for topping.


//////////////
////// Lesson 4/7 Parameters II

// If we can set one parameter, can we set two?

// We can set as many parameters as we'd like by adding them 
// when we declare the function, separated by commas, like this:

function getRemainder(numberOne, numberTwo) {
  console.log(numberOne % numberTwo);
}

getRemainder(365, 27);
// Output: 14

// The getRemainder function has two parameters: numberOne and numberTwo.
// When we call the getRemainder function on the last line, 
// we include two numbers as the parameters, also separated by commas. 
// This is referred to as passing in parameters to a function.

// In this case, we are telling the function to assign numberOne the value of 365 
// and numberTwo the value of 27. We are passing in 365 and 27 to the getRemainder function.

// When the getRemainder runs, the function knows what numberOne and numberTwo equal 
// since we passed in two parameters when we called the function. 
// Therefore it evaluates 365 % 27, which produces the result 14.

// By adding multiple parameters, we can build functions that are more flexible. 
// Now the function has two variables that we can define when we call the function.


//// Instructions:

// Let's add another parameter to the takeOrder function to make the order even more descriptive.
// Add a parameter named crustType so that we can add this to the console output in the upcoming steps.

function takeOrder(topping, crustType){
  console.log('Order: ' + crustType + ' crust pizza' + ' topped with ' + topping);
}

// Inside the takeOrder function, interpolate the crustType parameter to construct a sentence like this:
	// Order: thin crust pizza topped with bacon

function takeOrder(topping, crustType){
  console.log('Order: ' + crustType + ' crust pizza' + ' topped with ' + topping);
}

takeOrder('chorizo', 'thin');

// Below the takeOrder function, call the function 3 times 
// and pass in different arguments each time for topping and crustType.

takeOrder('chorizo', 'thick');

takeOrder('chorizo', 'cheesey');


//////////////
////// Lesson 5/7 return

// Using console.log as the result of a function isn't the best use of a function. 
// The purpose of a function is to take some input, perform some task on that input, 
// then return a result.

// To return a result, we can use the return keyword. 
// Take a look at our function from the last exercise, now re-written slightly:

function getRemainder(numberOne, numberTwo) {
  return numberOne % numberTwo;
}

console.log(getRemainder(365, 27));
// Output: 14


// Instead of using console.log inside the getRemainder function, we used the return keyword. 
// return will take the result of the math operation and give it back to whatever calls it.

// On the last line, we called the getRemainder function inside of a console.log statement, 
// which outputted the result of 14.

// This code achieved the same output as before, however now our code is better. 
// Why? If we wanted to use the getRemainder function in another place in our program, 
// we could without printing the result to the console. 
// Using return is generally a best practice when writing functions, 
// as it makes your code more maintainable and flexible.


//// Instructions:

// Now that we have the pizza orders, 
// you want to add them up to find the cost of the pizzas for the check. 
// Let's imagine that each pizza is $7.50, no matter the topping and crust type.

// We will need to do three things to write this in JavaScript:

// Create a variable to hold the number of pizzas ordered.
// Whenever a pizza is ordered, add one to the number of pizzas ordered.
// Take the total number of pizzas and multiply them by 7, since each pizza is $7.50.

// Begin by creating a variable named orderCount set equal to 0 at the top of your code.

var orderCount = 0;

// Inside the takeOrder function, set orderCount equal to orderCount plus 1, 
// so that each time the takeOrder function runs, 1 is added to the orderCount.

function takeOrder(topping, crustType){
  console.log('Order: ' + crustType + ' crust pizza' + ' topped with ' + topping);
  orderCount = orderCount + 1;
}

// Now it's time to calculate the subtotal of the pizzas. 
// This is the perfect job for a function.
// Declare a function named getSubTotal that has one parameter named itemCount.

function getSubTotal(itemCount) {
  return itemCount*7.5;
}

// Inside the getSubTotal function's block, use return to output the itemCount multiplied by 7.5.

function getSubTotal(itemCount) {
  return itemCount*7.5;
}

// On the last line of your program, after the takeOrder function calls, 
// call the getSubTotal function inside a console.log statement.

// getSubTotal has a parameter that represents the amount of items ordered. 
// Pass in the orderCount as an argument when making the function call.

var orderCount = 0;

function takeOrder(topping, crustType){
  console.log('Order: ' + crustType + ' crust pizza' + ' topped with ' + topping);
  orderCount = orderCount + 1;
}

function getSubTotal(itemCount) {
  return itemCount*7.5;
}

takeOrder('chorizo', 'thin');
takeOrder('chorizo', 'thick');
takeOrder('chorizo', 'cheesey');

console.log(getSubTotal(orderCount));

//// OUPUT:

	// Order: thin crust pizza topped with chorizo
	// Order: thick crust pizza topped with chorizo
	// Order: cheesey crust pizza topped with chorizo
	// 22.5


//////////////
////// Lesson 6/7 return II

// In the last exercise, we pointed out that using return makes programs more maintainable and flexible, 
// but how exactly?

// When functions return their value, we can use them together and inside one another. 
// If our calculator needed to have a Celsius to Fahrenheit operation, 
// we could write it with two functions like so:

function multiplyByNineFifths(celsius) {
  return celsius * (9/5);
}

function getFahrenheit(celsius) {
  return multiplyByNineFifths(celsius) + 32;
}

console.log('The temperature is ' + getFahrenheit(15) + '°F');
// Output: The temperature is 59°F

// Take a look at the getFahrenheit function. Inside of its block, we called multiplyByNineFifths and passed it the degrees in celsius. The multiplyByNineFifths function multiplied the celsius by (9/5). Then it returned its value so the getFahrenheit function could continue on to add 32 to it.

// Finally, on the last line, we interpolated the function call within a console.log statement. 
// This works because getFahrenheit returns it's value.

// We can use functions to section off small bits of logic or tasks, 
// then use them when we need to. 
// Writing functions can help take large and difficult problems 
// and break them into small and manageable problems.


//// Instructions:

// It's your job to calculate two more numbers for each order:

// A sales tax of 6% needs to be calculated for every full order. 
// This should be based on the subtotal.
// The total, which is the subtotal plus tax, should also be computed.

// Let's start with calculating the tax. 
// Under the getSubTotal function, declare a function named getTax. It should take no parameters.

function getTax() {
  
}

// Inside the getTax function's block, multiply the subtotal times 6% (0.06). 
// Make sure to return the result of this operation.

function getTax() {
  return getSubTotal(orderCount)*0.06;
}

// Nice work! Now that you calculated the tax, 
// declare another function named getTotal beneath the getTax function. 
// The getTotal function should have no parameters.

// Inside the getTotal function's block, add the subtotal to the tax, then return the result.

function getTax() {
  return getSubTotal(orderCount)*0.06;
}

function getTotal() {
  return getSubTotal(orderCount) + getTax();
}

// On the last line of the program, call the getTotal function inside of a console.log statement 
// to view the result.

var orderCount = 0;

function takeOrder(topping, crustType){
  console.log('Order: ' + crustType + ' crust pizza' + ' topped with ' + topping);
  orderCount = orderCount + 1;
}

function getSubTotal(itemCount) {
  return itemCount*7.5;
}

function getTax() {
  return getSubTotal(orderCount)*0.06;
}

function getTotal() {
  return getSubTotal(orderCount) + getTax();
}


takeOrder('chorizo', 'thin');
takeOrder('chorizo', 'thick');
takeOrder('chorizo', 'cheesey');

console.log(getTotal());

// Way to go! You wrote 4 functions from scratch, and even passed them into each other. 
// That's incredible!


//////////////
////// Lesson 7/7 Review Functions

// This unit introduced you to functions.

// Functions are written to perform a task.
// Functions take data or variables, perform a set of tasks on them, and then return the result.
// We can define parameters when calling the function.
// When calling a function, we can pass in arguments, which will set the function's parameters.
// We can use return to return the result of a function 
// which allows us to call functions anywhere, even inside other functions.

// Great work so far. 
// Next up: Scope! Scope informs us where variables are accessible from within our programs.




//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Scope
//////////////

// https://www.codecademy.com/en/courses/learn-javascript/lessons/scope/exercises/global-scope?action=lesson_resume&link_content_target=interstitial_lesson

//////////////
////// Lesson 1/4 Global Scope

// Scope is a big idea in programming, so let's start at a high level.

// Scope refers to where in a program a variable can be accessed. 
// The idea is that some variables are unable to be accessed everywhere within a program.

// Think of it like a an apartment building. 
// Everyone who lives in the apartment building is under the global scope of the building and its manager. 
// So, if there are rats in the shared laundry room, everyone has access to the laundry machines, 
// and the rats.

// If you write a variable outside of a function in JavaScript, 
// it's in the global scope and can be used by any other part of the program, 
// just like the laundry room can be used by everyone in an apartment.

// Let's practice this by making some global variables.

//// Instructions:

// Write two variables, one named laundryRoom set equal to 'Basement', 
// the other named mailRoom set equal to 'Room 1A'.

var laundryRoom = 'Basement';
var mailRoom = 'Room 1A';

// Below these variables, use console.log to print both variables to the console, like this:

console.log('Laundry: ' + laundryRoom +  ', Mail: ' + mailRoom);


//////////////
////// Lesson 2/4 Functional Scope

// In our theoretical apartment building, you have your own apartment. 
// It has stuff in it that is yours. 
// Other people in the building can't access it. 
// This is like functional scope. 
// You have access to your stuff inside your apartment, and in the building 
// – but not anyone else's apartment.

// When we write variables inside a function, only that function has access to its own variables. 
// Therefore, they are in the functional scope.

// In addition to a function having access to its own variables, 
// it also has access to variables in the global scope.

// In the last exercise we created both variables in the global scope. 
// That is, laundryRoom and mailRoom are accessible from anywhere in our program.

// Now, let's make two variables within a functional scope.


//// Instructions:

// Write a function named myApartment before the console.logs from the last exercise.

function myApartment(){}

// Inside of the function, write a variable named mailBoxNumber and set it equal to Box 3.

// Also, you're lucky enough to have in-unit laundry, 
// so let's re-assign laundryRoom inside our function to: laundryRoom = 'In-unit'.

function myApartment(){
  var mailBoxNumber = 'Box 3';
  var laundryRoom = 'In-unit';
}

// Inside the function, use console.log to print out both variables, 
// like this:
	console.log('Mail box: ' + mailBoxNumber + ', Laundry:' + laundryRoom);

function myApartment(){
  var mailBoxNumber = 'Box 3';
  var laundryRoom = 'In-unit';
  console.log('Mail box: ' + mailBoxNumber + ', Laundry:' + laundryRoom);
}

// Now, let's try to see the mailBoxNumber outside the function. On the last line of the program, 
// write:
	console.log(mailBoxNumber);

var laundryRoom = 'Basement';
var mailRoom = 'Room 1A';

function myApartment(){
  var mailBoxNumber = 'Box 3';
  var laundryRoom = 'In-unit';
  console.log('Mail box: ' + mailBoxNumber + ', Laundry:' + laundryRoom);
}

console.log(mailBoxNumber);

console.log('Laundry: ' + laundryRoom +  ', Mail: ' + mailRoom);


// Nothing showed up in the console! 
// That's right, and it means that JavaScript does not have access to the variable, 
// since it is hidden away in the myApartment function.

// To see the hidden variables inside the function, 
// delete the console.log on mailBoxNumber in the global scope, 
// and call the myApartment function instead.

var laundryRoom = 'Basement';
var mailRoom = 'Room 1A';

function myApartment(){
  var mailBoxNumber = 'Box 3';
  var laundryRoom = 'In-unit';
  console.log('Mail box: ' + mailBoxNumber + ', Laundry:' + laundryRoom);
}

console.log(myApartment());


//////////////
////// Lesson 3/4 Scoping

// Nice work! Now that we know how global and functional scope contain variables, 
// let's organize some code to practice.

// To the right, we provided you with incorrect sample code. 
// If you try to run it as is, you will get an error because the console.log on line 20 
// references variables that are within the functional scope of myApartment.

// Let's fix our scoping issues!


function myApartment() {
	var myCoffeeMaker = 'Aeropress';
	var buildingAddress = '150 E 14th St, New York, NY';
	var myCloset = 'Extra coats in the back';
	var buildingLaundryCode = 4927;
	var myRefridgerator = 'Filled with veggies and dark chocolate.';
	var myDog = 'Nikko';
	var buildingPhone = '(481) 516-2342';
}


// Do not edit the code after this line
console.log("**Apartment Building Information**");
console.log("Laundry code: " + buildingLaundryCode + "\nPhone: " + buildingPhone + "\nMailing address: " + buildingAddress);


//// Instructions:

// Within the myApartment function, 
// move the variables with apartment building information to the global scope, 
// so that the console.log on line 20 can run.

// Note: Do not edit the variables or their values.

function myApartment() {
	var myCoffeeMaker = 'Aeropress';
	var buildingAddress = '150 E 14th St, New York, NY';
	var myCloset = 'Extra coats in the back';
	var buildingLaundryCode = 4927;
	var myRefridgerator = 'Filled with veggies and dark chocolate.';
	var myDog = 'Nikko';
	var buildingPhone = '(481) 516-2342';
}

var buildingAddress = '150 E 14th St, New York, NY';

var buildingLaundryCode = 4927;

var buildingPhone = '(481) 516-2342';


// Do not edit the code after this line
console.log("**Apartment Building Information**");
console.log("Laundry code: " + buildingLaundryCode + "\nPhone: " + buildingPhone + "\nMailing address: " + buildingAddress);


//////////////
////// Lesson 4/4 Review Scope

// This unit introduced you to scope.

// Scope is the idea in programming that some variables are acessible/inaccessible 
// from other parts of the program.

// Global Scope refers to variables that are accessible to every part of the program.
// Functional Scope refers to variables created inside functions, 
// which are not accessible outside of its block.

// Keep up the awesome job in the next lesson where we'll learn how to make lists 
// and how to program JavaScript to do repetitive tasks for us with loops!



//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Arrays
//////////////

// https://www.codecademy.com/courses/learn-javascript/lessons/arrays/exercises/arrays?action=lesson_resume

//////////////
////// Lesson 1/7 Arrays

// We’ve learned to do a number of interesting things with data using functions 
// and using if/else statements. 
// One thing that we haven't learned yet is how to organize and store data.

// One way we organize data in real life is to make lists. 

// Let's make one here:

	// Bucket List:
		// 0. Rappel into a cave
		// 1. Take a falconry class
		// 2. Learn to juggle

// Let's now write this list in JavaScript, as an array:

var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];

// Arrays are JavaScript's way of making lists. 
// These lists can store different data types and they are ordered, 
// meaning the position of each list item is numbered by JavaScript.


//////////////
////// Lesson 2/7 Create an array

// Let's start by making an array and then seeing what it can do throughout the rest of this lesson.


//// Instructions:

// Make a variable named bucketList, and set it equal to an array with three strings inside of it.

var bucketList = ['Fly a wingsuit', 'Sail around the world', 'Lose all my teeth'];

// Use console.log to print bucketList to the screen.

console.log(bucketList);


//////////////
////// Lesson 3/7 Property Access

// Great work. Now, what if we want to select one item from an array?

// Luckily, each item in an array has a numbered position. 
// We can access an item using its number, just like we would in an ordinary list. 
// There’s one catch though!

// JavaScript counts starting from 0, not 1, so the first item in an array will be at position 0. 
// This is because JavaScript is zero-indexed.

// We can select the first item in an array like this:

var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];
var listItem = bucketList[0];
console.log(listItem);
// Output: 'Rappel into a cave'


// If we wanted the second item, we'd write:

var bucketList = ['Rappel into a cave', 'Take a falconry class', 'Learn to juggle'];
var listItem = bucketList[1];
console.log(listItem);
// Output: 'Take a falconry class'


//// Instructions:

// Create a variable named listItem and set it equal to the first item in your bucketList array.

// Then use console.log to print the listItem variable to the console.

var bucketList = ['Fly a wingsuit', 'Sail around the world', 'Lose all my teeth'];

var listItem = bucketList[0];

console.log(listItem);

// Now, set the listItem variable to the third item in the bucketList array.

var listItem = bucketList[2];

// Try to log the item at position [3] to the console.

var listItem = bucketList[3];

// Notice that you get undefined when you try to print position 3. 
// That's because the array does not have an item at position 3, which is the fourth slot.

// Fun fact: You can also access each individual character in a string 
// the same way you do with arrays. 

//For instance, you can write:
var hello = 'Hello World';
console.log(hello[6]);
// Output: W

// 'W' will be the output since it's the character in the 6th position. 
// This works because JavaScript internally stores strings in a similar way that it stores arrays.


//////////////
////// Lesson 4/7 length property

// It is often convenient to know how many items are inside of an array.

// nWe can find this out by using one of an array's built in properties, 
// called .length. 
// We can attach this to any variable holding an array and it will return the number of items inside.

// As an example:

var bucketList = ['Rappel into a cave', 'Take a falconry class'];

console.log(bucketList.length);
// Output: 2


//// Instructions:

// Find the .length of your bucketList array and log it to the console.

var bucketList = ['Fly a wingsuit', 'Sail around the world', 'Lose all my teeth'];

var listItem = bucketList.length;

console.log(listItem);

// Fun fact: .length is also a property for strings.

// For instance, you can write 'Hello World'.length, 
// and it will output 11 (the number of characters in "Hello World").


//////////////
////// Lesson 5/7 push Method

// JavaScript has a surprise for us: 
// it has built in functions for arrays that help us do common tasks! 
// Let's learn two of them.

// First, push() allows us to add items to the end of an array. 
// Here is an example of how this is used:

var bucketList = ['item 0', 'item 1', 'item 2'];

bucketList.push('item 3', 'item 4');

// The method push() would make the bucketList array look like:

['item 0', 'item 1', 'item 2', 'item 3', 'item 4'];

// Check out how push() works here:

	// It connects to bucketList with a period.
	// Then we call it like a function. 
		// That's because push() is a function 
		// and one that JavaScript allows us to use right on an array.

// Connecting a function like this is common in JavaScript. 
// Think: we've been connecting .log to console this whole time!


//// Instructions:

// Add two more items to your bucketList array using push.

var bucketList = ['Fly a wingsuit', 'Sail around the world', 'Lose all my teeth'];

var listItem = bucketList.length;
console.log(listItem);

bucketList.push('scientifically kill myself','burn a rose bush');

var listItem = bucketList.length;
console.log(listItem);

// Now, use console.log to print your bucketList array. to make sure your items were added.

console.log(bucketList);


//////////////
////// Lesson 6/7 pop Method

// Now that we can push() items into an array, let's pop one off, using pop().

// pop() is similar to push(), except that it deletes the last item of an array. 

// Here's an example:

var bucketList = ['item 0', 'item 1', 'item 2'];

bucketList.pop();

console.log(bucketList); 
// Output: [ 'item 0', 'item 1' ]

// Notice that 'item 2' was deleted from the end.


//// Instructions:

// Use the pop method to delete the last element from your array.

var bucketList = ['Fly a wingsuit', 'Sail around the world', 'Lose all my teeth'];

bucketList.push('scientifically kill myself','burn a rose bush');

var listItem = bucketList.length;
console.log(listItem);

bucketList.pop();

var listItem = bucketList.length;
console.log(listItem);

// Log bucketList to the console to make sure it worked.

console.log(bucketList);

// push and pop are just two of many methods we have for arrays. 
// You can learn more array methods here.

//  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


//////////////
////// Lesson 7/7 Review Arrays

// Nice work! In this lesson, we learned these concepts regarding arrays:

// Arrays are lists and are a way to store data in JavaScript. 
// Each item inside of an array is at a numbered position. 
// Arrays are created with brackets [].

// We can access one item in an array using it's numbered position, 
// with syntax like: myArray[0].

// Arrays have a length property, which allows you to see how many items are in an array.

// Arrays also have their own methods, including push and pop, 
// which add and subtract items from an array, respectively.

// In the next lesson we'll learn how to loop over our arrays, which can bring our lists to life!



//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// Loops
//////////////

// https://www.codecademy.com/en/courses/learn-javascript/lessons/loops/exercises/loops

//////////////
////// Lesson 1/7 Loops

// One of a computer's greatest abilities is to repeat a task over and over 
// so we don't have to. 
// Loops let us tell the computer to loop over a block of code 
// so that we don't have to write out the same process over and over.

// Loops are especially helpful when we have an array 
// where we'd like to do something to each item in the array, 
// like logging each item to the console.

// There are two kinds of loops we will learn in this lesson:

	// for loops, which let us loop a block of code a known amount of times.
	// while loops, which let us loop a block of code an unkown amount of times.

//////////////
////// Lesson 2/7 Loop by hand

// Before we jump into writing a loop, let's write the result of a loop, 
// so that we can better understand how loops work.


//// Instructions:

// Write an array and set it equal to a variable named vacationSpots. 
// Inside of this array, list three places you'd like to visit.

var vacationSpots = ['Paris', 'New York', 'LA'];

// Next, console.log each item in vacationSpots on a separate line. 
// To do this, list out each item using property access.

console.log(vacationSpots[0]);

console.log(vacationSpots[1]);

console.log(vacationSpots[2]);

// Nice work, that wasn't too hard, but imagine if our vacation list had 100 places on it. 
// This would be an extremely tedious task!

// Let's make this easier with a for loop.


//////////////
////// Lesson 3/7 for loops

// Instead of writing out the same code over and over, 
// let’s make the computer loop through our array for us. 
// We can do this with for loops.

// The syntax looks like this:

var animals = ["Grizzly Bear", "Sloth", "Sea Lion"];

for (var i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}

// Output:
// Grizzly Bear
// Sloth
// Sea Lion

// Since this syntax is a little complicated, let's break it into 4 parts:

// Within the for loop's parentheses, 
// the start condition is var i = 0, which means the loop will start counting at 0.
// The stop condition is i < animals.length, 
	// which means the loop will run as long as i is less than the length of the animals array. 
// When i is greater than the length of the animals array, the loop will stop looping.
// The iterator is i++. This means that each loop, i will have 1 added to it.
// And finally, the code block is inside the { ... }. The block will run each loop, until the loop stops.

// The secret to loops is that i, the variable we created inside the for loop's parentheses, 
// is always equal to a number. 
// To be more clear, the first loop, i will equal 0,
//  the second loop, i will equal 1, and the third loop, i will equal 2.

// This makes it possible to write animals[0], animals[1], animals[2] programmatically 
// instead of by hand. We can write a for loop, and replace the hard coded number with the variable i, 
// like this: animals[i].


//// Instructions:

// Let's replace your current code with a loop.

// Write a for loop that loops through your vacationSpots array.

// Inside the block of the for loop, use console.log to print each item in the vacationSpots array.

var vacationSpots = ['Paris', 'New York', 'LA'];

for (var i = 0;i < vacationSpots.length; i++){
  console.log(vacationSpots[i]);
}

// Way to go! Now, add more to each item. Inside the code block, 
// add some text to each item, like this:

console.log('I would love to visit ' + vacationSpots[i]);

var vacationSpots = ['Paris', 'New York', 'LA'];

for (var i = 0;i < vacationSpots.length; i++){
  console.log('I would love to visit ' + vacationSpots[i]);
}


//////////////
////// Lesson 4/7 for loop backwards

// If we can make a for loop run forwards through an array, 
// can we make it run backwards through it? Of course!

// We can make out loop run backwards by modifying the start, stop, and iterator conditions.

// To do this, we'll need to edit the code between the for loop's parentheses:

// The start condition should set i to the length of the array.
// The stop condition should end when i is 0.
// The iterator should subtract 1 each time, which is done with i--.


//// Instructions:

// We need to make three changes to our for loop:

// Edit the start condition (var i = 0), to set i equal to the length of the vacationSpots array.
// Set the stop condition ( i < vacationSpots.length) to stop when i is greater than or equal to 0.
// Change i++ to i-- to subtract 1 from i each loop.

var vacationSpots = ['Paris', 'New York', 'LA'];

for (var i = vacationSpots.length; i >= 0; i--){
  console.log('I would love to visit ' + vacationSpots[i]);
}

// can't hit return inside ()

// Nice work! Except we printed 'I would love to visit undefined'. 
// Why did this happen?

// It's because the length of vacationSpots is 3 
// and vacationSpots has items in its array at positions 0, 1, and 2.

// Since JavaScript starts from 0, 
// make the start condition the length of the vacationSpots array, minus 1.

var vacationSpots = ['Paris', 'New York', 'LA'];

for (var i = vacationSpots.length -1; i >= 0; i--){
  console.log('I would love to visit ' + vacationSpots[i]);
}

// Nice work! Remember, all for loops have three conditions, start, stop, and iterate, 
// and we can edit all three!


//////////////
////// Lesson 5/7 for loops inside of for loops

// Let's say that you and a friend would like to go on vacation together. 
// You've both made arrays of your favorite places 
// and you want to compare to see if any places match. 
// This is a job for loops!

// The big idea is that we can run a for loop inside another for loop 
// to compare the items in two arrays.

// Every time the outter for loop runs once, 
// the inner for loop will run completely.

// With two for loops, we can check to see if any of the your vacation spots 
// match your friend's spots.


//// Instructions:

// We are going to write this program from scratch. 
// Start out by writing an variable named myPlaces and set it equal to an array 
// with three places you'd like to visit.

var myPlaces = ['paris', 'berlin', 'la'];

// Now, make another variable named friendPlaces and set it equal to an array 
// with three places a friend might like to go.

// Make sure that at least one of the places is the same as in your myPlaces array.

var friendPlaces = ['paris', 'Berlin', 'LA'];

// Write a for loop that iterates through each item in myPlaces and logs out each place.

var myPlaces = ['paris', 'berlin', 'la'];
var friendPlaces = ['paris', 'Berlin', 'LA'];

for (var i = 0; i < myPlaces.length; i++){
  console.log(myPlaces[i]);
}

// You logged all of your places!

// Now, inside of the existing for loop's block, 
// write another for loop that loops over friendPlaces. 
// This time, instead of using the i as the variable name, use j, 
// so we don't overwrite any variables.

var myPlaces = ['paris', 'berlin', 'la'];

var friendPlaces = ['paris', 'Berlin', 'LA'];

for (var i = 0; i < myPlaces.length; i++){
  console.log(myPlaces[i]);
  for (var j = 0; j < friendPlaces.length; j++){
  	console.log(friendPlaces[j]);
  }
}

// Look what printed to the console. 
// Your first place printed, then all three of your friend's. 
// Then your second place, then your friend's places again. 
// And then one more time.

// This is because the inner for loop runs completely every time 
// the outer for loop runs once. 


// The purpose of the program is to see what you and your friend have in common. 
// Let's utilize the === comparison with an if/else statement.

// Inside the second for loop's block, 
// write an if/else statement that checks 
// if myPlaces[i] is equal to friendPlaces[j]. 
// If it is, log to the console the place you have in common.

var myPlaces = ['paris', 'berlin', 'la'];
var friendPlaces = ['paris', 'Berlin', 'LA'];

for (var i = 0; i < myPlaces.length; i++){
  for (var j = 0; j < friendPlaces.length; j++){
  	if (myPlaces[i] === friendPlaces[j]){
  		console.log(friendPlaces[j]);
  	}
  }
}


//////////////
////// Lesson 6/7 while loops

// Awesome job! for loops are great, but they have a limitation: 
// you have to know how many times you want the loop to run. 
// What if you want a loop to run an unknown or variable number of times instead?

// For example, if we have a deck of cards and we want to flip cards 
// (loop a card flipping function) until we get a 'Spade',
// how could we write that in JavaScript?

// That's the purpose of the while loop. It looks like similar to a for loop. 
// Check it out:

while (condition) {
  // code block that loops until condition is false
}

// The loop begins with the keyword while
// Inside the parentheses, we can insert a condition. 
// As long as the variable evaluates to true the block of code will loop.
// Inside the code block we can write any code we'd like to loop.


//// Instructions:

// Let's write a program that flips cards until we get a 'Spade.' 
// Start by creating a variable named cards and set it equal to this array:

	// ['Diamond', 'Spade', 'Heart', 'Club']

var cards = ['Diamond', 'Spade', 'Heart', 'Club'];


// Right under the array create a variable named currentCard and set it equal to 'Heart'.

// This variable will hold the name of the card we just flipped. 
// We are using 'Heart' as the first card.

var currentCard = 'Heart';

// Let's utilize a while loop to do two things:

// If the currentCard is not a 'Spade', 
// then add a console.log to print the value of currentCard.

// Then, create a random number between 0 and 3 and put it in a variable named randomNumber.
// Then use the randomNumber to reassign currentCard to a new card from the cards array.

// The while loop could like this:

while (currentCard !== 'Spade') {
  console.log(currentCard);
  var randomNumber = Math.floor(Math.random() * 4);
  currentCard = cards[randomNumber];
}

// Outside the while loop, on the last line of the program, 
// use console.log to log that the program found a spade.

// Run the code a few times to see the output changing. 
// You can see the while loop guessing a card, then seeing if it is a Spade, 
// over and over, until it finds one.

var cards = ['Diamond', 'Spade', 'Heart', 'Club'];
var currentCard = 'Heart';

while (currentCard !== 'Spade') {
  console.log(currentCard);
  var randomNumber = Math.floor(Math.random() * 4);
  currentCard = cards[randomNumber];
}

console.log('Found a Spade!');


//////////////
////// Lesson 7/7 Review loops

// Great job! 
// In this unit we learned how to write less repetitive code with loops.

// for loops allow us to repeat a block of code a known amount of times.
// We can use a for loop inside another for loop to compare two lists.
// while loops are for looping over a code block an unknown amount of times.

// At this point, you've learned the foundational concepts of JavaScript. 
// Now we are going to apply them to the web with a JavaScript library called jQuery.



//////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
//////////////
// JavaScript and the DOM
//////////////

// https://www.codecademy.com/en/courses/learn-javascript/lessons/javascript-dom/exercises/javascript-with-html-css

//////////////
////// Lesson 1/16 JavaScript with HTML and CSS

// At the beginning of this course we mentioned that JavaScript is 
// the most widely used language on the web. 
// So how can we use JavaScript on a website?

// So far, we've only used JavaScript in isolation – not alongside other technologies. 
// Javascript typically gets included with HTML and CSS 
// (which structure and style web pages). 

//  All modern browsers know how to run JavaScript if we include it in an HTML and CSS project.

// JavaScript also has some special functions to help us access the code inside HTML and CSS 
// so that we can write JavaScript to make that output interactive and dynamic.

// In this lesson, we will use the concepts we've learned throughout the course 
// to make an HTML and CSS website dynamic.


//// Instructions:

// If you're unfamiliar with HTML and CSS, 
// you can follow along with this lesson regardless. 
// If you'd like to get a primer before continuing, try our HTML and CSS course here.

	// https://www.codecademy.com/learn/web


//////////////
////// Lesson 2/16 Linking JavaScript

// We can link a JavaScript file to HTML by including it as the src of a <script> tag 
// inside of an HTML file, like this:

	// <script src='js/main.js'></script>

// This line of code will link the file located at js/main.js. 
// You can find this file in the file navigator by clicking the 
// file button located at the top left of the code editor. 
// Within the navigator, there's a folder named js, 
// and within that folder is the main.js file.

// By linking js/main.js in the index.html file, 
// we are asking the browser to run our JavaScript code each time index.html loads.

// We've provided you with a sample website (and the corresponding HTML and CSS code). 
// Our goal: use JavaScript to make this page more dynamic. 
// We will add interactive features to it as we go through the lesson.

// In the code editor, we've loaded the files for a static HTML and CSS website. 
// If you've never seen HTML before, don't worry, we'll walk through 
// how JavaScript is added to an existing HTML and CSS project in this lesson. 
// This lesson won't require you to greatly modify the HTML and CSS code itself. 
// (For a deeper dive, see our HTML & CSS course here.)


//// Instructions:

// Let's start by writing some JavaScript that we will soon link to our HTML document.

// Click the folder icon attached to the code editor, 
// and navigate inside the js folder and open main.js.

// Inside main.js, write:

alert('Hello JavaScript!');

// Note: alert is a JavaScript function that will create a pop-up window 
// with text inside it. 
// When we link the main.js file to the HTML file, 
// we will see a pop-up window that was generated by this code. 
// alert is not used by JavaScript developers in practice, 
// however it is useful here to demonstrate linking these two files. 
// We will use it over the next few exercises for demonstration purposes.


/// main.js
alert('Hello JavaScript!');


// Navigate back to index.html. 
// Before the closing </body> tag, 
// create a link to the main.js file using a <script> tag.

// Once you've add it, click 'Run'.

/// index.html
	// <script src='js/main.js'></script>
	// </body>
	// </html>

// Nice alert pop-up! We just connected JavaScript to an HTML file. 
// When the HTML document loaded, it ran the code inside main.js, 
// which created the alert pop-up.

// Now let's take this a step further.


//////////////
////// Lesson 3/16 Document Object Model

// The Document Object Model, commonly referred to as the DOM', 
// is the term for elements in an HTML file. 
// Elements are any HTML code denoted by HTML tags, like <div>, <a>, or <p>. 
// Let's use JavaScript to interact with the DOM.

// We can select an HTML element with JavaScript by selecting its class attribute,
// like this:

var header = document.getElementsByClassName('example-class-name');

// This would find an element like this in the HTML:

	// <div class='example-class-name'> ... </div>


//// Instructions:

// Let's see how JavaScript can select an HTML element.

// Inside index.html, 
// notice there's an <div> element with a class of skillset on line 10. 
// Let's select this element with JavaScript.

// Click on the folder icon to navigate to js/main.js.

// Inside main.js, delete the alert you wrote in the last exercise. 
// Then, create a variable named skillset and set it equal to 
// the HTML element with the class skillset.

/// main.js
var header = document.getElementsByClassName('skillset');


// Under the skillset variable, 
// use an alert to make the skillset variable's value into a pop-up.

alert(skillset);

// Way to go! 
// The pop up showed that you selected an [object HTMLCollection].

// This confirms that JavaScript can select HTML elements. 
// Since we can select HTML elements, we can manipulate them.

// Selecting and modifying HTML elements with plain JavaScript can be tricky. 
// Luckily, there's an easier way. Click 'Next' to learn more.


//////////////
////// Lesson 4/16 jQuery

// We've just covered how to select HTML elements using the syntax: 
// document.getElementsByClassName. 
// This is verbose and clunky, however. 
// If we were to select a lot of elements this way, 
// our code would get dense and difficult to read.

// Wouldn't it be nice if there was a simpler way to select DOM elements? 
// As you might have guessed, there is!

// To better interact with DOM elements, we can use a library. 
// A library is a set of code that contains useful pre-written functions 
// that help with certain tasks.

// A great library for interacting with the DOM is jQuery.

// jQuery is a library written in JavaScript. 
// The syntax and functions it contains will help us interact with DOM efficiently. 
// We'll walk through a few examples in the following exercises.

// In order to use jQuery, we need to:

// Include jQuery in our project. 
// jQuery is a library, which means it is a set of code in a file, 
// therefore we will need to link that file in our HTML in order to access it.

// Once we link it in our HTML file, 
// we can use its functions and syntax in our js/main.js file.
// Once linked, we'll need to make sure our HTML is loaded before we run our jQuery 
// and JavaScript code.

// This will prevent our jQuery and JavaScript code from running before 
// the elements they select are rendered.


//// Instructions:

// Since jQuery is a library of code, we need to include a link to it 
// in our index.html file before we can use it. 
// Before the closing </body> tag, right above your current <script> tag, 

// include this code:
	// <script src='https://code.jquery.com/jquery-3.1.0.min.js'></script>

// The link to jQuery needs to be above the link to the js/main.js file, 
// which will give main.js access to the jQuery library.

// Note: If you're curious, you can see all the code that makes up jQuery here. 
// You'll notice that jQuery is just JavaScript!

/// index.html
	// <script src='https://code.jquery.com/jquery-3.1.0.min.js'></script>
	// <script src='js/main.js'></script>
	// </body>
	// </html>


// Now that we've included jQuery, let's get it ready to run.

// Navigate to js/main.js.

// Delete or comment out your existing code in js/main.js. 
// Then, write a function named main. 
// The function should take no parameters and should have an empty block.

// main.js
function main(){}

// jQuery has a built in function to check if the page is ready before 
// it will run our code. 

// After the main function, write this code:
$(document).ready(main);

// Notice that we put main inside the parentheses of ready. 
// main here is a callback, which means that our code will wait until the document 
// (in other words, the DOM) is loaded, or ready.
// When it is, then it will execute the main function. 
// jQuery calls back to the main function, therefore it's a callback.

// In the event that our HTML and CSS took 5 minutes to load, 
// this code would wait until it loaded completely before running

// main.js
function main(){}

$(document).ready(main);


// Nice work! We are now ready to start using jQuery. 
// Let's try in the next exercise.


//////////////
////// Lesson 5/16 jQuery Selectors

// With plain JavaScript we selected an HTML element with this code:

document.getElementsByClassName('skillset');

// With jQuery we can select the same element with:

$('.skillset');

// We can wrap any CSS selector, like class, id, or tag, with 
// $('.example-class') to select it with jQuery.

// The selectors jQuery uses are the exact same as CSS selectors. 
// For instance, if there's an element with a class of supporting-text, 
// you could select it with $('.supporting-text'). 
// Another example, if an element had an id of 'header', 
// you could select it with $('#header').


//// Instructions:

// Let's select the element with the class of skillset, 
// but this time with jQuery.

// In js/main.js, inside the main function, 
// write a variable named $skillset. 

// Set $skillset equal to a jQuery selector for the skillset class.

// Note: It is a common convention to name variables 
// that hold jQuery selectors with a dollar sign $.

function main(){
  var $skillset = $('.skillset');
}

$(document).ready(main);

// On the line below the jQuery selector for skillset, 
// write an alert on $skillset.

function main(){
  var $skillset = $('.skillset');
}

alert($skillset);

$(document).ready(main);

// The alert shows [object Object]. 
// This is right and means that we successfully selected 
// the same HTML element as before, but this time using jQuery.

// Now let's see what we can do once we've selected an DOM element.

//////////////
////// Lesson 6/16 hide

// Now that we can select an element with jQuery, 
// we can use built-in jQuery functions to modify it. 
// From here on, we will start building features into our skills website.

// First off, it would be nice to make the page fade in when loaded.

// To make a page fade in, it must first be hidden. 
// We can hide elements with jQuery with a function named hide.

// We can hide elements with jQuery, like this:

$('.my-selector').hide();

// We attached the hide function directly to the jQuery selector.

// The hide function will add the CSS property 
// "display: none" 
// to the DOM element from the page, which will hide it.


//// Instructions:

// We want all of our skills to fade in, 
// so we need to hide the skills first. 

// In index.html, the element around all of our skills has the class skillset.

// Inside the main function, delete the $skillset variable and the alert 
// you wrote in the last exercise. 
// Then use jQuery to hide the skillset element. 
// Do this by writing a selector for skillset, 
// then attaching hide() to it with a period.

function main(){
	$('.skillset').hide();
}

$(document).ready(main);

// Notice that the skills have been hidden. 
// hide added a CSS property of 
// "display: none" to .skillset element, which hid the elements.

// Now, let's learn how to fade in the skillset when the page loads. 


//////////////
////// Lesson 7/16 fadeIn

// In order to fade in the skillset element, 
// we can use a the jQuery function named fadeIn.

// True to its name, fadeIn will fade an element in 
// over a period of time in milliseconds. It looks like this:

$('.example-class').fadeIn(400);

// We must start with an element that is not currently displayed on the page.
// Just like before, we can attach fadeIn directly to a jQuery selector.
// Within fadeIn's parentheses, we can specify how long we want the fade 
// to last in milliseconds. 400 is the default.
// The example code will fade in the '.example-class' element over 0.4 seconds.


//// Instructions:

// Under the line that hides the skillset element, 
// write another jQuery selector for skillset.

// Then, attach fadeIn to it. 
// Your fadeIn should last for 1 second/1000 milliseconds.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
}

$(document).ready(main);

// Now the whole page fades in when the page loads. Nice work!


//////////////
////// Lesson 8/16 click

// The next feature we'd like to build is making the '
// Recent Projects' clickable. 
// When clicked, the button should show the individual projects, 
// and when clicked again, it should hide the projects.

// In order to make an element clickable, 
// we need to write jQuery that listens to an element for a click event. 
// jQuery can do this with an event listener function named on('click').

// This function will wait for a click event, and when one occurs, 
// it will execute a provided function. 

// The syntax looks like this:

$('.example-class').on('click', function() {
  // execute the code here when .example-class is clicked.
});

// $('.example-class') selects an HTML element with the class example-class.
// .on('click', function() { ... }) adds a click listener to the selector. 
// When it's clicked the function will execute the code within its block.


//// Instructions:

// Our goal is to show our HTML projects when the 'Recent Projects' 
// button in each section is clicked, 
// and to hide them when we click it again.

// Let's start by hiding the projects that are currently there.

// Under your existing code in the main function, 
// use jQuery to hide the elements with a class of projects.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
}

// Our elements are now hidden. 
// The next step is to make the 'Recent Projects' button clickable.

// Under the hide you just wrote, 
// write a jQuery selector for the 'Recent Projects' button. 
// Its class is .projects-button.

// Then, attach on('click'), 
// and provide it an empty function as the second parameter to on.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {});
}

// Now that the click listener is set up on the 'Recent Projects' buttons, 
// let's make the projects appear when we click them.

//////////////
////// Lesson 9/16 show

// To make our projects visible when the 'Recent Projects' button is clicked, 
// jQuery provides a function named show, which is the opposite of hide.

// To show an element, the syntax looks as such:

$('.example-class').show();

// show is attached directly to the jQuery selector.
// show will change the CSS attribute 
// "display: none"
// to a visible display property, therefore showing the element.


//// Instructions:

// Inside the click function you wrote in the last exercise, 
// write a selector for the projects class.

// Then, call the show function on it.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$('.projects').show();
  });
}

// Click on the 'Recent Projects' buttons, 
// and notice that the projects now show when clicked.

// Notice that there are some problems though:

// The projects don't hide again when you click the button again.
// When you click one button, all the projects show in each section.

// It would also be nice if the button we clicked looked selected, 
// or changed appearance when clicked.

// We will solve these problems in the upcoming exercises.


//////////////
////// Lesson 10/16 toggle

// When we click on a 'Recent Projects' button, the projects show. 
// Next, let's hide the projects if we click the '
// Recent Projects' button again.

// jQuery provides a function named toggle that is helpful in this situation. 
// toggle will hide or show an element, each time it is triggered. 

// The syntax looks like this:

$('example-class').toggle();

// toggle can be called directly on an jQuery selector.
// When toggle is executed, 
// it will hide or show the element that the selector points to. 
// If the element is currently hidden, toggle will show the element, 
// and vice versa.


//// Instructions:

// Inside the click function, we wrote a selector for the projects class 
// and we called show on it.

// Replace the show function with toggle.

// Then 'Run' your code and click on the 'Recent Projects' buttons multiple times.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$('.projects').toggle();
  });
}

// Making progress!
// Now the projects toggle in and out when we click.
// Next, let's make our button change appearance when it is clicked.


//////////////
////// Lesson 11/16 toggleClass

// Let's add one more feature: 
// when we click the 'Recent Projects' button the background color 
// and text color should change.

// We can toggle a CSS class with a jQuery function named toggleClass. 
// The syntax looks like this:

$('.example-class').toggleClass('active')

// .toggleClass is a function that will toggle a CSS class 
// on the jQuery selector it's connected to. 
// If the element has the class applied to it, 
// toggleClass will remove it, and if the element does not have the class, 
// it will add it.

// 'active' is the class that we will toggle on and off. 
// Notice that toggleClass does not require us to include the period 
// before 'active' since it's already expecting a CSS class.


//// Instructions:

// In css/styles.css, there is this class:

// .active {
  background-color: #333333;
  color: whitesmoke;
}

// Inside the click function, 
// toggle this class on the elements with the projects-button class.

// The .active class will make the projects-button's background dark 
// and its text light.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$('.projects').toggle();
	$('.projects-button').toggleClass('active')
  });
}

// Click on the 'Recent Projects' buttons. 
// Now they change color when clicked, 
// and change back to their original state when clicked again.

// There's still one big issue: 
// we only want the element we clicked on to toggle its projects and class.

// Let's solve it in the next exercise. 


//////////////
////// Lesson 12/16 this

// In the last exercise, we were toggling every 'Recent Projects' button 
// instead of only the one we clicked on.

// We can select the specific element we clicked on 
// with the jQuery selector $(this).

// The syntax looks like this:

$('.example-class').on('click', function() {
  $(this).toggleClass('active');
});

// $(this) selects the clicked element. 
// If there are multiple elements with a class of .example-class, 
// this will only toggle the class of the one that is clicked on.

// Notice that $(this) does not require quotes around it, 
// since it is not a CSS class. 
// Instead, this is a JavaScript keyword.

// $(this) behaves just like our other selectors. 
// We can attach toggleClass or toggle to it in the same way.


//// Instructions:

// Let's begin by only changing the class of the element we clicked.

// Modify the toggleClass we wrote in the last exercise to use 
// $(this) as its selector.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$('.projects').toggle();
    $(this).toggleClass('active');
  });
}

// Now click on the 'Recent Project' buttons within each section 
// and see that only the button you click on will toggle its class.

// Next up, let's toggle the projects in the section we clicked on, 
// instead of toggling them all.


//////////////
////// Lesson 13/16 next

// In order to toggle the projects in each section, 
// we will need to use $(this) to select the button we clicked on. 
// The issue is that $(this) refers to the projects-button in our current code, 
// and not the projects themselves.

// We need a way to select the projects elements next to the button that we clicked.

// Luckily, jQuery can select elements logically. 
// In index.html, notice that the projects-button element 
// is directly followed by the projects list. 
// Therefore the projects element is next after it.

// jQuery has a function named next to help us select elements 
// that are next to another element. 

// If we have this in our HTML:
	// <div class='item-one'> ... </div>
	// <div class='item-two'> ... </div>

// If we wanted to hide item-two, we could write:

$('.item-one').next().hide();

// We can attach next to any jQuery selector 
// to select the next direct element.

// Then, we can attach any jQuery function to next(). 
// In this case, we attached hide, 
// which would hide the next element after the $('.item-one') element.


//// Instructions:

// Inside the click function, let's modify this line:

$('.projects').toggle();

// Instead of selecting all the projects elements, 
// use $(this) and next to select the projects, 
// then attach toggle on the end to toggle the projects on the page.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$(this).next().toggle();
    $(this).toggleClass('active');
  });
}

// When you click on the 'Recent Projects' buttons now, 
// only that section's buttons projects toggle.

// Nice work, this page is really coming together.

// Let's add two more features.


//////////////
////// Lesson 14/16 text

// Since we have a few areas to click on, 
// it may be helpful to show users which sections they have viewed 
// by changing the text inside the 'Recent Projects' buttons.

// When a user clicks on a button, we will permanently change the text 
// of the button to 'Projects Viewed'.

// We can change the text of an element with the jQuery function text. 
// It's syntax looks like this:

$('.my-selector').text('Hello world!');

// text attaches directly to a jQuery selector.
// Inside of text's parentheses, we can provide text that will become 
// the text of our DOM element. 
// The text we supply will replace any existing text, 
// and if the element has no pre-existing text, text will add it.


//// Instructions:

// Within the projects-button click function, under the toggleClass line, 
// write jQuery to change the text of the button that was clicked 
// to say 'Projects Viewed'.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	$(this).next().toggle();
    $(this).toggleClass('active');
    $(this).text('Projects Viewed');
  });
}

// Now click on the 'Recent Project' buttons 
// and notice that they now turn to 'Projects Viewed' after each click. 
// Very nice!


//////////////
////// Lesson 15/16 slideToggle

// The last feature we'd like to add is an aesthetic one. 
// Right now when we click the 'Recent Projects' buttons, 
// the projects appear instantly.

// Let's instead make the projects slide onto the page 
// when we click the 'Recent Projects' button and 
// then slide off the page when we click the button again.

// jQuery provides a method named slideToggle 
// that can animate an element's entrance and exit. 

// The syntax looks like this:
$('.example-class').slideToggle(400);

// slideToggle can be called directly on a jQuery selector.
// slideToggle also takes a parameter of milliseconds 
// that the animation should last. 
// The default is 400 milliseconds, or 0.4 seconds.


//// Instructions:

// Let's make our projects slide in and out when we click 
// on the 'Recent Projects' button.

// Inside the click function, delete or comment out 
// this line in your code:
$(this).next().toggle();

// This line can prevent the slideToggle from working properly, 
// since it is also affecting the showing and hiding behavior
// of the projects element.

// Then, select the projects element of the button that is clicked. 
// Use slideToggle on the selector to animate its appearance 
// and exit on the page. 
// The animation should last 400 milliseconds.

function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
  	// $(this).next().toggle();
    $(this).next().slideToggle(400);
    $(this).toggleClass('active');
    $(this).text('Projects Viewed');
  });
}

// Now the projects slide in and out of the page when 
// we click the 'Recent Projects' buttons.

// By using jQuery, we've made this page much better 
// by adding interactive elements.


//////////////
////// Lesson 16/16 Review jQuery

// Nice work!
// jQuery is a complete library, and we've only covered the basics. 

// If you're interested in adding animations to websites 
// and creating more dynamic elements, take our jQuery course here.



// In this lesson we learned:

// How to link a JavaScript file to an HTML file using a <script> tag.

// jQuery is a library to help JavaScript interact with HTML elements.

// We can make sure our page is ready to go with $(document).ready(). 
// Then, we can pass in a function to ready that will execute when the page is loaded.

// jQuery uses the same selector names as CSS.

// We can hide elements with hide, and show them with show.

// We can make elements appear with fadeIn.

// on('click') functions allow us to make HTML elements clickable. 
// When an element is clicked, the click function will execute the function we provide. 
// It's full sytnax looks like:
$('.example-class').on('click', function() {
  // Execute when .example-class is clicked
});

// toggle will toggle an element on and off the page.

// $(this) will select the specific element that was clicked 
// if placed inside a click function.

// toggleClass can toggle a class on and off.

// We can select elements next to each other with next.

// text will replace a DOM element's text with text we specify.

// slideToggle will make an element slide into and out of the page 
// with an animation.


// Impressive work on completing Learn JavaScript!

// The next Javascript course, Intermediate JavaScript, is coming soon! 
// In the course you'll learn how to write full-fledged programs in JavaScript.

// Until then, try out our jQuery course to make websites more dynamic, 
// or start building applications with JavaScript 
// with our AngularJS course and our React course. 

// AngularJS and React are two application frameworks written in JavaScript. 
// With them, you'll be able to create web applications.

// Congrats again on your progress in completing Learn JavaScript!  



////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



//////////////////////////////////////
// JavaScript  
// https://www.codecademy.com/learn/javascript
//////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// Introduction to JavaScript
///////////////////////////////////
///////////////////////////////////


//////////////
// Getting Started with Programming
//////////////


//////////////
////// Lesson 7/28 What am I learning?

// This is JavaScript (JS), a programming language. 
// There are many languages, but JS has many uses and is easy to learn.

// What can we use JavaScript for?

 // make websites respond to user interaction
 // build apps and games (e.g. blackjack)
 // access information on the Internet (e.g. find out the top trending words on Twitter)
 // organize and present data (e.g. automate spreadsheet work; data visualization)

// Example of how JS can be interactive
confirm('This is an example of using JS to create some interaction on a website. Click OK to continue!');


//////////////
////// Lesson 8/28 Interactive JavaScript

// What we just saw was a fun example of how JavaScript can be interactive. 
// Try it yourself!

// Examples:

confirm("I feel awesome!");
confirm("I am ready to go.");

// These boxes can be used on websites to confirm things with users. 
// You've probably seen them pop up when you try to delete important things 
// or leave a website with unsaved changes.


//// Instructions:

// Write your own message that you want the user to confirm.

// Also try the Q&A forum to get help
// The link is on the bottom left of the page!

confirm("fug")


//////////////
////// Lesson 9/28 What is programming?

// Programming is like writing a list of instructions 
// to the computer so it can do cool stuff with your information.

// Programs can't yet make your bed, but they can do math, 
// keep track of your bank account, or send a message to a friend.

// To do any of these actions, the program needs an input. 

// You can ask for input with a prompt.

// Examples:

prompt("What is your name?");
prompt("What is Ubuntu?");


//// Instructions:

// Use the prompt command to ask the user where they are from. Check out the examples above for how to do this!

prompt("Where are you from?");

// london


//////////////
////// Lesson 10/28 Data Types I & II: Numbers & Strings

// Data comes in various types. 
// You have used two already!

// a. numbers are quantities, 
	// just like you're used to. You can do math with them.

// b. strings are sequences of characters, 
	// like the letters a-z, spaces, and even numbers. 
	// These are all strings: "Ryan", "4" and "What is your name?" 
	// Strings are extremely useful as labels, names, 
	// and content for your programs.

// To make a number in your code, just write a number as numerals 
// without quotes: 42, 190.12334.

// To write a string, surround words with quotes: "What is your name?"


//// Instructions:

// Write a string with at least 3 words. 
// Check out the examples of strings above.
// Find the length of the string by writing a period (full stop) 
// and the word length, like this:

"string".length

// Length counts every character in the string - including spaces!

"string asdf asdf".length

// 16 


//////////////
////// Lesson 11/28 Data Type III: Booleans

// Nice job! Next let's look at booleans. 
// A boolean is either true or false.

// For example, comparing two numbers returns a true or false result:

// 23 > 10 is true
// 5 < 4 is false


//// Instructions:

// Let's compare two numbers to return a true result:

// First, write the string "I'm coding like a champ"
// Next, find the length of the string using .length
// Then, compare the string's length to see if it is greater than 10
// If you want to check your code, click "Stuck? Get a hint!" below.

"I'm coding like a champ".length > 10

// true 


//////////////
////// Lesson 12/28 Using console.log

// You may have noticed that the interpreter doesn't print out 
// every single thing it does. 
// So if we want to know what it's thinking, 
// we sometimes have to ask it to speak to us.

console.log() 
// will take whatever is inside the parentheses and log it to the console 
// below your code—that's why it's called console.log()!

// This is commonly called printing out.


//// Instructions:

// Please print the following two console.log statements at the same time. 
// Type one on line 1 and the other on line 2. Then press Save & Submit Code.

console.log(2 * 5)
console.log("Hello")


//////////////
////// Lesson 13/28 Comparisons

// So far we've learned about three data types:

	// strings (e.g. "dogs go woof!")
	// numbers (e.g. 4, 10)
	// booleans (e.g. false, 5 > 4)

// Now let's learn more about comparison operators.

// List of comparison operators:

	// > Greater than
	// < Less than
	// <= Less than or equal to
	// >= Greater than or equal to
	// === Equal to
	// !== Not equal to

//// Instructions:

// Try to use each of the operators above.

// Choose the correct comparison operator to make each 
// of the four statements print out true.


// Here is an example of using the greater than (>) operator.
console.log(15 > 4); // 15 > 4 evaluates to true, so true is printed.

// Fill in with >, <, === so that the following print out true:
console.log("Xiao Hui".length < 122);
console.log("Goody Donaldson".length > 8);
console.log(8*2 === 16);



//////////////
////// Lesson 14/28 Decisions, decisions

// Nice work on comparisons! 
// Now let's see how we can use comparisons to ask yes or no questions.

// Say we want to write a program that asks whether your name 
// is longer than 7 letters. 
// If the answer is yes, we can respond with "You have a long name!" 
// We can do this with an if statement:

if( "myName".length >= 7 ) {
    console.log("You have a long name!");
}

// An if statement is made up of the if keyword, 
// a condition like we've seen before, 
// and a pair of curly braces { }. 

// If the answer to the condition is yes, 
//the code inside the curly braces will run.


//// Instructions:

// Check out the if statement in the editor.

// On line 1, add a condition inside the parentheses ( ).
// If the answer to the condition is yes, 
// the code inside the curly braces will run. 
// So on line 2, use console.log to print out a string.

if (3 < 4 ) {
    console.log("3 is bigger than 4");
}


//////////////
////// Lesson 15/28 Computers are smart

// Great! We used an if statement to do something if the answer 
// to the condition was yes, or true as we say in JavaScript.

// In addition to doing something when the condition is true, 
// we can do something else if the condition is false. 

// For example, if your name is shorter than 7 letters, 
// we can respond with "You have a short name!" 
// We can do this using an if / else statement:

if( "myName".length >= 7 ) {
    console.log("You have a long name!");
}
else {
    console.log("You have a short name!");  
}

// Just like before, if the condition is true, 
// then only the code inside the first pair of curly braces will run. 
// Otherwise, the condition is false, so only the code inside the second pair 
// of curly braces after the else keyword will run.

// In the example above the condition "myName".length >= 7 
// evaluates to false since "myName" only has 6 letters. 
// Since the condition is false, only the code inside the curly braces 
// after the else keyword runs, and prints out You have a short name!.


//// Instructions:

// In line 1, fill in a condition that will evaluate to false

// Fill in some code to run in the else portion 
// (this will run if the condition is false). Use console.log for this part.

if (3 > 4) 
{
    console.log("Let's go down the first road!");
}
else 
{
    console.log("print some stuff")
    // What should we do if the condition is false? Fill in here:
    
}

// print some stuff


//////////////
////// Lesson 16/28 More practice with conditionals

// Now let's practice using if/else statements. 
// Do as much as you can by yourself, 
// but if you need a reminder, 
// click the "Stuck? Get a hint!" button below.


//// Instructions:

// Write an if/else statement, just like we did in the last exercise. 
// Here's what the outline of the code looked like:

if (condition) 
{
    // if condition is true
    // do this code
}
else // "otherwise"
{
    // do this code instead
}

// If your condition is true, use console.log to print 
// "The condition is true".

// Otherwise (else) when it is false, use console.log to print 
// "The condition is false".

// Make sure your condition evaluates to false, 
// so that your program prints out "The condition is false".


// Remember, the order and punctuation matter.
// If you get an error, check carefully, line by line.
// If you're really stuck, click "Stuck? Get a hint!"


if ("hello".length < ("goodbye".length/2)){
    console.log("The condition is true")
}
else{
    console.log("The condition is false")
}


//////////////
////// Lesson 17/28 Computers aren't that smart

// Well done! Now, computers are very literal. 
// Syntax needs to be in exactly the right place 
// for the computer to understand the code.

// As you get started with programming, 
// we will teach you many syntax rules. 
// This is sort of like the grammar of programming languages. 
// Grammar first, then programming poetry!


//// Instructions:

// There are many mistakes in this code. 
// Find them and fix them all.

// You are doing what's called "debugging," 
// a term popularized by Grace Hopper 
// when she literally removed a moth from her computer.

// The computer doesn't worry about extra spaces between words or brackets
// It just cares about the order of where things are placed
// and that you have used the right characters (){}[]"";

// For extra help, a program called a 'linter' is checking your code
// and will put a red 'x' next to the first line that contains errors

if (10 = 10); {
    console.log("You got a true!");
} else {
    console.log("You got a false!");
}


if (10 === 10) {
    console.log("You got a true!");
} 
else {
    console.log("You got a false!");
}

// You got a true!


//////////////
////// Lesson 18/28 Mid-lesson breather

// We've covered a lot of ground so far! 
// So many new terms, so much syntax. 
// Let's take a breather and review. 

// We have learned:

// 1. Confirm and prompt

// We can make pop-up boxes appear! 
confirm("I am ok");
prompt("Are you ok?");

// 2. Data types

	// a. numbers (e.g. 4.3, 134)
	// b. strings (e.g. "dogs go woof!", "JavaScript expert")
	// c. booleans (e.g. false, 5 > 4)

// 3. Conditionals

// If the first condition is met, 
// execute the first code block. 
// If it is not met, execute the code in the else block. 

// See the code on the right for another example.

//// Instructions:

// This is an example of an if / else statement.

if (12 / 4 === "Ari".length) {
    confirm("Will this run the first block?");
} else {
    confirm("Or the second block?");
}

// Hope this breather was helpful! Click 'Save and Submit' to continue.


//////////////
////// Lesson 19/28 Math

// We saw basic math before. 
// The basic math symbols we learned in school work here. 
// Even the order in which the computer understands 
// the math is the same as in school!

// Code:

	// ( ): control order of operations
	// * and /: multiplication and division
	// - and +: subtraction and addition

// Examples:
	// 100/10 evaluates to 10
	// "Jane".length + 5 evaluates to 9
	// 5*(3+1) evaluates to 20


//// Instructions:

// Complete the missing bits of code to construct the if / else statement.
// Make the condition evaluate to true.

// Finish the else statement by printing out the string 
// "Error Error Error" to the console.

 ("Jon".length * 2 / (2+1) === )
{
    console.log("The answer makes sense!");
} 
else 


if ("Jon".length * 2 / (2+1) === 2)
{
    console.log("The answer makes sense!");
} 
else {
    console.log("Error Error Error")
}

// The answer makes sense!


//////////////
////// Lesson 20/28 Math and the modulo

// Let's meet an interesting symbol called modulo. 
// When % is placed between two numbers, 
// the computer will divide the first number by the second, 
// and then return the remainder of that division.

// So if we do 23 % 10, we divide 23 by 10 which equals 2 with 3 left over. 
// So 23 % 10 evaluates to 3.

// More examples:
	// 17 % 5 evaluates to 2
	// 13 % 7 evaluates to 6


//// Instructions:

// Use console.log and modulo three times to print 
// the remainder of the following equations:

	// a. 14 / 3
	// b. 99 / 8
	// c. 11 / 3

// Below is an example of printing the remainder of 18/4 using modulo:
// console.log(18 % 4); 

console.log(14 % 3); 
console.log(99 % 8); 
console.log(11 % 3); 


//////////////
////// Lesson 21/28 Modulo and if / else

// So why learn modulo? 
// For one thing, it's good at testing divisibility. 
// Consider 30 % 10.
// What does it return? 
// There is nothing left over, so 0.

// How about 9 % 3? Also 0.

// We can use modulos in comparisons, like this:

// 10 % 2 === 0 evaluates to true
// 7 % 3 === 0 evaluates to false because there is 1 left over.


//// Instructions:

// Let's get the if/else" statement to display 
// "The first number is even".

// Edit line 5 by adding a comparison that evaluates to true.

// In the comparison, use a modulo and an even number, 
// like we did in the example above.

//An example of an if/else statement with modulo in the condition

if(  ) {
    console.log("The first number is even");
} else {
    console.log("The first number is odd");
}

if( 23%3 === 2 ) {
    console.log("The first number is even");
} else {
    console.log("The first number is odd");
}
// The first number is even


//////////////
////// Lesson 22/28 Substrings

// We've learned a few ways to manipulate numbers. 
// What about manipulating strings?

// Sometimes you don't want to display the entire string, 
// just a part of it. 

// For example, in your Gmail inbox, you can set it to display 
// the first 50 or so characters of each message so you can preview them. 

// This preview is a substring of the original string (the entire message).

// Code:

"some word".substring(x, y) 
// where x is where you start chopping 
// and y is where you finish chopping the original string.

// The number part is a little strange. 
// To select for the "he" in "hello", you would write this:

"hello". substring(0, 2);

// Each character in a string is numbered starting from 0, 
// like this:

// 0 1 2 3 4
// | | | | | 
// h e l l o

// The letter h is in position 0, the letter e is in position 1, and so on.

// Therefore if you start at position 0, and slice right up till position 2, 
// you are left with just he

// More examples:

// First 3 letters of "Batman" 
"Batman".substring(0,3);

// From 4th to 6th letter of "laptop" 
"laptop".substring(3,6);


//// Instructions:

// Find the 4th up to and including the 7th letter 
// of the string "wonderful day".

"wonderful day".substring(3,7);


//////////////
////// Lesson 23/28 More substring practice

// Getting the positioning of substring letter positions is tricky! 
// Let's make sure we really have it nailed down.

// Remember that each character in a string is numbered starting from 0. 
// So for the word "hello", 
// The letter h is in position 0, the letter e is in position 1, and so on.


//// Instructions:

// Using console.log, on three separate lines, 
// print out the substrings for the following strings.

// a. "Jan" in "January"
// b. "Melbourne is" in "Melbourne is great" (note the space!)
// c. "burgers" in "Hamburgers"


// Use console.log( ) to print out the substrings.
// Here is an example of the 1st to 4th letter of "JavaScript":
// console.log("JavaScript".substring(0,4));

console.log("January".substring(0,3));
console.log("Melbourne is great".substring(0,12));
console.log("Hamburgers".substring(3,10));


//////////////
////// Lesson 24/28 Variables

// We have learned how to do a few things now: 
// make strings, 
// find the length of strings, 
// find what character is in the nth position, 
// do basic math. 
// Not bad for a day's work!

// To do more complex coding, 
// we need a way to 'save' the values from our coding.

// We do this by defining a variable with a specific, case-sensitive name. 
// Once you create (or declare) a variable as having a particular name, 
// you can then call up that value by typing the variable name.

// Code:

var varName = data;

// Example:

	// a. var myName = "Leng";
	// b. var myAge = 30;
	// c. var isOdd = true;


//// Instructions:

// Create a variable called myAge and type in your age.

// To create a variable, we use only one equals sign
// But to check if two values are equal, we use 3 equal signs.

// declare your variable here:

var myAge = 18;

console.log(myAge);

// 18


//////////////
////// Lesson 25/28 More Variable Practice

// We have seen how to create a variable. 
// But how do we use it? 
// It is useful to think that any time you type the variable's name, 
// you are asking the computer to swap out the variable name 
// and swap in the value of the variable.

// For example:
var myName = "Steve Jobs";
myName.substring(0,5)

// Look at the second line above. 
// You have asked the computer to swap out myName and swap in Steve Jobs, so
myName.substring(0,5)

// becomes
"Steve Jobs".substring(0,5)

//which evaluates to Steve.

// Another example
var myAge = 120;

// What is
// myAge % 12 ? See the hint to check your answer.

// So the variable stores the value of the variable, 
// whether that is a number or a string. 
// As you will see soon, this makes writing long programs much easier!


//// Instructions:

// Follow the instructions in the comments in the code to continue.

// Declare a variable on line 3 called
// myCountry and give it a string value.
var myCountry = "UK"

// Use console.log to print out the length of the variable myCountry.
console.log(myCountry.length );

// Use console.log to print out the first three letters of myCountry.
console.log(myCountry.substring(0,2) );


//////////////
////// Lesson 26/28 Change variable values

// So far, we've seen
	// a. how to create a variable
	// b. how to use a variable

// Let's now see how to change a variable's value. 
// A variable's value is easily changed. 
// Just pretend you are creating a new variable 
// while using the same name of the existing variable!

// Example:

var myAge = "Thirty";
// Say I had a birthday and I want to change my age.
myAge = "Thirty-one";

// Now the value of myAge is "Thirty-one"!

//// Instructions:

// Follow the instructions on line 1, line 3, line 5 and line 8. 
// We're using this method to show you the order in 
// which you tell the computer what to do is very important.

// On line 2, declare a variable myName and give it your name.
var myName = "Christian"
// On line 4, use console.log to print out the myName variable.
console.log(myName)
// On line 7, change the value of myName to be just the first 2 
// letters of your name.
myName = myName.substring(0,2)
// On line 9, use console.log to print out the myName variable.
console.log(myName)


//////////////
////// Lesson 27/28 Conclusion: Part 1

// Let's do a quick review!

// Data types:
	// strings (e.g. "dogs go woof!")
	// numbers (e.g. 4, 10)
	// booleans (e.g. false, 5 > 4)

// Variables:
	// We store data values in variables. 
	// We can bring back the values of these variables 
	// by typing the variable name.

// Manipulating numbers & strings:
	// comparisons (e.g. >, <=)
	// modulo (e.g. %)
	// string length (e.g. "Emily".length;)
	// substrings (e.g. "hi".substring(0, 1);)

// console.log( ) :
	// Prints into the console whatever 
	// we put in the parentheses.


//// Instructions:

// On line 1, create a variable myColor and give it a string value.
// On line 2, print the length of myColor to the console.

myColor = "black"
console.log(myColor.length)


//////////////
////// Lesson 28/28 Conclusion: Part 2

// Congratulations on making it this far. 
// You have learned a lot! 
// Just one more exercise before a big pat on the back!

// The last tricky thing we learned was about if / else statements.

// If / else statements are conditional statements. 
// Under different conditions, the computer will output different things.

// Not sure where to begin? Check the Hint!

if (1 === 2/2){
    console.log("I finished my first course!")
}
else{
    console.log("it was shite")
}



///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// FUNCTIONS
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to Functions in JS
//////////////



//////////////
////// Lesson 1/13 Introduction

// Programming is simply a way to give instructions to the computer.

// In Getting Started, we learned about if / else statements.

// We want to keep learning ways to instruct the computer to perform 
// repeatable tasks efficiently.


//// Instructions:

// Let's briefly review! 
// Use an if / else to check how fast you're driving.

// If speed is greater than 80, 
// use console.log to print "Slow down"
// Otherwise (else), use console.log to print "Drive safe"

var speed = 65;

// Complete the condition in the ()s on line 4
if (speed > 80) {
	// Use console.log() to print "Slow down"
	console.log("Slow down")
} 
else {
	// Use console.log() to print "Drive safe"
    console.log("Drive safe")

}


//////////////
////// Lesson 2/13 Introducing Functions

// Programming is similar to baking cakes. 
// Seriously! 
// Imagine you are trying to teach your friend Jane 
// how to bake many different types of cakes.

// Each cake takes in different ingredients (ie. inputs). 
// But the 'bake' instructions are always the same. 

// For example:
	// Pre-heat the oven at 300 degrees
	// Mix all the ingredients in a bowl
	// Put contents into oven for 30 mins

// And the output will be a different cake each time.

// It is tedious to have to repeat to Jane the same 'bake' 
// instructions every time. 
// What if we could just say 'bake' 
// and Jane would know to execute those three steps? 
// That is exactly what a function is!


//// Instructions:

// Line 3 declares the function and gives it a name.

// Focus on line 4 and line 5. 
// The code within the curly brackets { } is the code 
// we want to use again and again. (i.e. the 'bake' instructions)

// Line 4 declares a variable called val. 
// Line 5 prints the value of that variable.

// On line 8-11, we explain what calling a function means.

// On line 12, replace the 6 with any number and press Save & Submit Code. 
// Do this a few times to see the beauty of functions!

// This is what a function looks like:

var divideByThree = function (number) {
    var val = number / 3;
    console.log(val);
};

// On line 12, we call the function by name
// Here, it is called 'dividebythree'
// We tell the computer what the number input is (i.e. 6)
// The computer then runs the code inside the function!
divideByThree(6);


//////////////
////// Lesson 3/13 Function syntax

// A function takes in inputs, does something with them, 
// and produces an output.

// Here's an example of a function:

var sayHello = function(name) {
    console.log('Hello ' + name);
};

// First we declare a function using var, 
// and then give it a name sayHello. 
// The name should begin with a lowercase letter 
// and the convention is to use lowerCamelCase 
// where each word (except the first) begins with a capital letter.

// Then we use the function keyword to tell the computer 
// that you are making a function

// The code in the parentheses is called a parameter. 
// It's a placeholder word that we give a specific 
// value when we call the function. 
// Click "Stuck? Get a hint!" for more.
// Then write your block of reusable code between { }. 
// Every line of code in this block must end with a ;.

// You can run this code by "calling" the function, like this:

sayHello("Emily");

// Calling this function will print out Hello Emily.


//// Instructions:

// On line 11, call the greeting function 
// and put in a name that you want the greeting function to include.

// Press "Save & Submit Code" and see the function get into action! 
// Saves you so much time.

// Below is the greeting function!
// See line 7
// We can join strings together using the plus sign (+)
// See the hint for more details about how this works.

var greeting = function (name) {
    console.log("Great to see you," + " " + name);
};

// On line 11, call the greeting function!
greeting("Emily")


//////////////
////// Lesson 4/13 How does a function work?

// Let's break down exactly how a computer thinks 
// when it sees the code for a function.

var functionName = function( ) {
    // code code code
    // code code code
    // (more lines of code)
};

// The var keyword declares a variable named functionName.

// The keyword function tells the computer that 
// functionName is a function and not something else.

// Parameters go in the parentheses. 
// The computer will look out for it in the code block.

// The code block is the reusable code that is between 
// the curly brackets { }. 
// Each line of code inside { } must end with a semi-colon.

// The entire function ends with a semi-colon.

// To use the function, we call the function by just typing 
// the function's name, and putting a parameter value inside 
// parentheses after it. 
// The computer will run the reusable code with the specific 
// parameter value substituted into the code.


//// Instructions:

// Let's make a function that tells the world what you want to eat.

// Declare your function and call it foodDemand.

// You can call the parameter anything you like. 
// But we'll call it food because that is the thing that is going 
// to change each time we call the function.

// Your reusable block of code follow this. 
// Surround it with the right brackets. 
// The code you want to repeat is: console.log("I want to eat" + " " + food);

// Call the function and put in a specific food you want!


// Write your foodDemand function below.
// Last hint: In your reusable block of code, end each line
// with a semicolon (;)

var foodDemand = function(food){
    console.log("I want to eat" + " " + food);
}

foodDemand("Cheese")

//////////////
////// Lesson 5/13 Tying it all together

// Why is the code organized like it is on lines 2-5?

// The computer can understand the code without such spacing. 
// But it makes editing a lot easier and is best practice.

// Do I have to put a semi-colon at the end of each line 
// of code in the reusable block? 
// And at the end of the entire function?
// Yes. At the end of each line of code (within the { }) 
// and after the entire function (after the { }), 
// please put a semi-colon. 
// The semi-colon acts like a period in a sentence. 
// It helps the computer know where there are stopping points 
// in the code.


//// Instructions:

// A big part of programming is debugging. 
// That just means figuring out what the heck went wrong
// with your code. Why didn't it run?

// Look at line 9. It has many syntax errors. 
// See how lack of spacing makes debugging hard?

// Fix the function on line 9. Make sure the syntax is right. 
// Make sure it looks nice.
// all the greeting function once it is fixed!
//  Don't forget to pass in a specific name.


// Nicely written function:
var calculate = function (number) {
    var val = number * 10;
    console.log(val);
};

// Badly written function with syntax errors!

var greeting = function(name){
    console.log(name);
};

greeting("Clare")


//////////////
////// Lesson 6/13 Don't Repeat Yourself (D.R.Y)

// The D.R.Y. principle is really important in programming. 
// No repeating!

// Any time you find yourself typing the same thing, 
// but modifying only one small part, 
// you can probably use a function.

// The 'small part' that you find yourself modifying 
// will be the parameter. 
// And the part that you keep repeating will be the code 
// in the reusable block - the code inside { }.


//// Instructions:

// You are a creature of habit. 
// Every week you buy 5 oranges. 
// But orange prices keep changing!

// You want to declare a function that calculates the cost 
// of buying 5 oranges.

// You then want to calculate the cost of the 5 all together.

// Write a function that does this called orangeCost().

//  It should take a parameter that is the cost of an orange, 
// and multiply it by 5.

// It should log the result of the multiplication to the console.

// Call the function where oranges each cost 5 dollars.
 
var orangeCost = function(price){
    total = price * 5;
    console.log(total);
};
orangeCost(5)


//////////////
////// Lesson 7/13 Return keyword

// Nice job! Now, when we call a function, 
// we don't always want to just print stuff. 
// Sometimes, we just want it to return a value. 
// We can then use that value (ie. the output from the function) 
// in other code. 

// Let's learn about the return keyword, 
// then we'll see how to use functions with an 
// if / else statement in the next exercise!

// The return keyword simply gives the programmer back the value 
// that comes out of the function. 
// So the function runs, and when the return keyword is used, 
// the function will immediately stop running and return the value.


//// Instructions:

// In our example we have a function called timesTwo() 
// that takes in a number and returns the number multiplied by two.

// On line 7, after the equals sign, 
// call the function timesTwo with any parameter you want
// Line 8 prints out newNumber. 
// Notice how the value we return from timesTwo() 
// is automatically assigned into newNumber.

// Parameter is a number, and we do math with that parameter

var timesTwo = function(number) {
    return number * 2;
};

// Call timesTwo here!
var newNumber = timesTwo(234)
console.log(newNumber);


//////////////
////// Lesson 8/13 Functions, return and if / else

// When we call a function, its return value is 
// just the result from running the function. 
// That value can then be used just like any other value in JavaScript!

// Look at the if statement starting on line 7. 
// The if statement is checking whether the result of calling 
// the function named quarter is divisible by 3.


//// Instructions:

//  Define a function called quarter which has a parameter called number.

// This function returns a value equal to one quarter of the parameter. 
// (i.e. number / 4;)

// Call the function inside the if statement's condition 
// (and put in a parameter value!) such that 
// "The statement is true" is printed to the console.

// Define quarter here.
var quarter = function(number) {
    return number / 4;
};

if (quarter(12) % 3 === 0 ) {
  console.log("The statement is true");
} else {
  console.log("The statement is false");
}



//////////////
////// Lesson 9/13 Functions, Functions with two parameters

// So far we've only looked at functions with one parameter. 
// But often it is useful to write functions with more than one parameter. 

// For example, we can have the following function:

var areaBox = function(length, width) {
    return length * width;
};

// With more than one parameter, we can create more useful functions

// To call a function with more than one parameter, 
// just enter a value for each parameter in the parentheses. 
// For example, areaBox(3,9); would return the area of a box 
// with a length of 3 and a width of 9.


//// Instructions:

// Write a function called perimeterBox that returns the 
// perimeter of a rectangle.

// It should have two parameters.

// One formula for perimeter is length + length + width + width;

// Call the function and pass in any value for length and width you like.

var perimeterBox = function(length, width) {
	return length + length + width + width;
};

console.log(perimeterBox(4,5))


//////////////
////// Lesson 10/13 Global vs Local Variables

// Let's talk about an important concept: scope. 
// Scope can be global or local.

// Variables defined outside a function are accessible anywhere 
// once they have been declared. 
// They are called global variables and their scope is global.

// For example:

var globalVar = "hello";

var foo = function() {
    console.log(globalVar);  // prints "hello"
}

// The variable globalVar can be accessed anywhere, 
// even inside the function foo.

// Variables defined inside a function are local variables. 
// They cannot be accessed outside of that function.

// For example:

var bar = function() {
    var localVar = "howdy";
}

console.log(localVar);  // error
T
// The variable localVar only exists inside the function bar. 
// Trying to print localVar outside the function gives a error.

// Check out the code in the editor. 
// Until now you've been using the var keyword without really understanding why. 
// The var keyword creates a new variable in the current scope. 
// That means if var is used outside a function, 
// that variable has a global scope. 
// If var is used inside a function, that variable has a local scope.

// On line 4 we have not used the var keyword, 
// so when we log my_number to the console outside of the function, 
// it will be 14.


//// Instructions:

// Change line 4 to use the var keyword. 
// Notice that the value of my_number in the function is now 14 
// and outside the function is 7.

// Using my_number without the var keyword refers to the global variable 
// that has already been declared outside the function in line 1. 
// However, if you use the var keyword inside a function, 
// it declares a new local variable that only exists within that function.

var my_number = 7; //this has global scope

var timesTwo = function(number) {
    var my_number = number * 2;
    console.log("Inside the function my_number is: ");
    console.log(my_number);
}; 

timesTwo(7);

console.log("Outside the function my_number is: ")
console.log(my_number);

// Inside the function my_number is: 
// 14
// Outside the function my_number is: 
// 7


var my_number = 7; //this has global scope

var timesTwo = function(number) {
    my_number = number * 2;
    console.log("Inside the function my_number is: ");
    console.log(my_number);
}; 

timesTwo(7);

console.log("Outside the function my_number is: ")
console.log(my_number);

// Inside the function my_number is: 
// 14
// Outside the function my_number is: 
// 14


//////////////
////// Lesson 11/13 Functions recap

// Okay let's review. 
// You have learned a lot about functions today. 
// We better not forget it all!

// We first discovered how to use functions 
// to perform the same piece of logic repeatedly, 
// without having to type the same code again. 
// This saves you time!


//// Instructions:

// Write a function called nameString()
// It should take name as a parameter.
// The function returns a string equal to "Hi, I am" + " " + name.
// Call nameString() by passing it your name, 
// and use console.log to print the output.


var nameString = function(name) {
	return "Hi, I am" + " " + name;
};

console.log(nameString("chris"))


//////////////
////// Lesson 12/13 Functions & if / else

// An especially useful application of reusable code is if/else statements. 
// These can be very wordy, and a pain to type repeatedly.

// We are going to write a function that checks 
// how many hours of sleep a night you're getting. 
// Inside the function will be an if/else statement. 
// We want the function to check many different numbers of hours 
// to see whether a person is getting enough sleep.


//// Instructions:

// Write a function named sleepCheck that takes the parameter numHours
// Inside the function, write an if statement 
// where if the number of hours of sleep is greater than or equal to 8, 
// the computer will return 
// "You're getting plenty of sleep! Maybe even too much!";.

// Otherwise (else) if the number of hours of sleep is less than 8, 
// have the computer return "Get some more shut eye!";

// Then call the function with different hours of sleep

// Call the function with 10 hours of sleep, like this: sleepCheck(10);
// Call the function with 5 hours of sleep.
// Call the function with 8 hours of sleep.


var sleepCheck = function(numHours) {
	if (numHours >= 8) {
		return "You're getting plenty of sleep! Maybe even too much!";
	} 
	else {
		return "Get some more shut eye!";
	}
};

sleepCheck(10);
sleepCheck(5);
sleepCheck(8);



//////////////
////// Lesson 13/13 Conclusion

// Congratulations on finishing this functions course! 
// Hopefully you can see how powerful functions are, 
// and how they can be used in so many contexts.


///////////////////////////////////
///////////////////////////////////

//////////////
// Build "Rock, Paper, Scissors"
//////////////


//////////////
////// Lesson 1/13 The Game






///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// 'FOR' Loops in JavaScipt
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to 'For' Loops in JS
//////////////


//////////////	For loops: The Basics
////// Lesson 1/13 Why use for loops?

// We are learning how to program because we don't want to 
// do boring, repetitive work! The computer should do that.

// This first exercise is a good example of exactly why you want to learn for loops.


//// Instructions:

// Use five console.log statements to print out the numbers 1 to 5.
// Try not getting angry at me for this annoying exercise.
// Head over to the next exercise to see how we can 
// use for loops to do this task more efficiently.

console.log("1")
console.log("2")
console.log("3")
console.log("4")
console.log("5")


//////////////
////// Lesson 2/13 Fist for loop

// Instead of manually typing in console.log five times, 
// we can use a for loop to do this. 
// The aim of this exercise is just to show you how a for loop looks, 
// and demonstrate how useful it is. 

// Subsequent exercises will
// a. walk you through the syntax bit by bit
// b. explain how the computer thinks as it executes a for loop.

// We initially focus on using for loops just to count numbers to keep things simple. 
// But by section 3, we will show you how to do more fancy things!


//// Instructions:

// The for loop in the code will print out 1 to 5 
// and use far less code than you used in the previous exercise.

// Change the 6 to 11 and press Save & Submit Code. 
// This will see the computer print out 1 to 10!

for (var counter = 1; counter < 11; counter++) {
	console.log(counter);
}



//////////////
////// Lesson 3/13 Starting the for loop

// Congratulations! You've just run your first for loop. 
// But what you're probably really keen to do is write your own for loop. 
// Below is the general syntax of the for loop. 
// We want to focus on the first line in the next few exercises.

// Syntax

for (var i = 1; i < 11; i = i + 1) {
    /* your code here */;
}

// Every for loop makes use of a counting variable. 
// Here, our variable is called i (but it can have any name). 
// The variable has many roles. 

// The first part of the for loop tells the computer 
// to start with a value of 1 for i. 
// It does this by declaring the variable called i and giving it a value of 1.

// When the for loop executes the code in the code block—the bit between { }—
// it does so by starting off where i = 1.


//// Instructions:

// This for loop starts off at 1 and will end at 10.
// Change the for loop such that it will start off at 5!

for (var i = 5; i < 11; i = i + 1){
	console.log(i);
}



//////////////
////// Lesson 4/13 Ending the for loop

// We know how to control where the for loop starts. 
// How do we control where it ends? 
// Well, the second part of the for loop determines that.

// Syntax

    for (var i = 1; i < 11; i = i + 1) {
        code code code; 
    }

// Here, this for loop will keep running until i = 10 
// ( i.e. while i < 11). 
// So when i = 2, or i = 9, the for loop will run. 
// But once i is no longer less than 11, the loop will stop.


//// Instructions:

// We know this for loop counts from 1 to 10.
// Change this for loop such that it starts at 4.
// Change this for loop such that it counts up to and including 23. 
// ( i.e. we do NOT want 24 to be printed out!)
// Run your for loop and see it count from 4 to 23!

for (var i = 4; i < 24; i = i + 1) {
	console.log(i);
}



//////////////
////// Lesson 5/13 Controlling the for loop

// We can now control where the for loop starts and ends. 
// What about controlling what happens in between?

// The examples we've looked at have used i = i + 1. 
//  This has meant we have incremented (increased) 
// the variable i by 1 each time.

// Rules to learn

// a. A more efficient way to code to increment up by 1 is to write i++.
// b. We decrement down by 1 by writing i--.
// c. We can increment up by any value by writing i += x, 
	// where x is how much we want to increment up by. 
	// e.g., i += 3 counts up by 3s.
// d. We can decrement down by any value by writing i -= x.
// e. Be very careful with your syntax—
	// if you write a loop that can't properly end, 
	// it's called an infinite loop.
	// It will crash your browser!


//// Instructions:

// This code counts every number from 0 to 35.
// Make it start counting from 5. Please!
// Stop the counting when it prints out 50.
// Only count every fifth number. So we want to increment i by 5.

for (var i = 5; i < 51; i = i + 5) {
	console.log(i);
}


////////////// Practicing loops
////// Lesson 6/13 How does it work?

// We've gone through the three bits of syntax for a for loop. 
// But how exactly does it work? 
// Let's imagine the steps the computer takes to run the for loop on the right.

for (var i = 2 ; i < 13; i++) {
	console.log(i);
}

// 1. It starts off with i = 2
// 2. It then asks: Is i currently less than 13? 
	// Because i = 2, this is true and we continue.
// 3. We do NOT increment now. 
	// Instead, if the condition is met, we run the code block.
// 4. Here, the code block prints out the value of i. 
	// It is currently 2 so 2 will be printed out.
// 5. Once the code block is finished, the for loop then increments / decrements. 
	// Here, we add 1.
// 6. Now i = 3. We check if it is less than 13. 
	// If it is true, we run the code block.
// 7. The code block runs, and then we increment.
// 8. We repeat these steps until the condition i < 13 is no longer true.


//// Instructions:

// Make the computer start counting at 8.
// Keep counting while i < 120.
// Count up by increments of 12.

for (var i = 8 ; i < 120; i=i+12) {
	console.log(i);
}


////////////// 
////// Lesson 7/13 Practice counting down

// for loops only run when the condition is true.

// It is important that there is a way for the for loop to end. 
// If the for loop is always going to be true, 
// then you will be stuck in an infinite loop 
// and your browser will crash! 
// Look at the code. It is bad.

for (var i = 1; i >= 1; i++) {
	console.log(i);
}

// a. It begins at i = 1. 
// b. It will keep going as long as i >= 1.
// c. Because now i = 1, the code will run.
// d. We increment i by 1 and now i = 2. 
	// This satisfies the condition. We run the code. 
// e. Increment i by 1 and now i = 3. 
	// This satisfies the condition that i >= 1. We run the code.
// f. We will keep incrementing the code up by 1. 
	// It will always satisfy the condition. 
	// The loop NEVER ends. 
	// This will crash your computer!


//// Instructions:

// Change this code such that it starts counting from 10.
// We want it to stop once it gets to 0.
// We want it to count down by 1.
// In the end, the numbers 10..0 inclusive, should be printed.

for (var i = 10; i >= 0; i--) {
	console.log(i);
}


////////////// 
////// Lesson 8/13 Last practice for loop

// You have a great handle on for loops now! 
// This will be the last practice one before we look at cool ways to use them.

// The next exercise introduces you to arrays. 
// So instead of just counting numbers up and down, 
// we can make the computer do many more interesting things with loops.


//// Instructions:
// Once more, for practice: write a for loop that gets the computer 
// to count down from 100 until 0 by 5. 
// This time, make sure not to print 0.

for (var i = 100; i >= 0; i=i-5){
    if (i > 0){
        console.log(i);
    }
}


//////////////  Arrays and Loops
////// Lesson 9/13 Meet arrays

// Variables can store numbers or strings. 
// But so far, we've only been able to store ONE number or ONE string. 
// Good thing we have arrays. 

// Arrays:
	// a. store lists of data
	// b. can store different data types at the same time
	// c. are ordered so the position of each piece of data is fixed

// Example:
var names = ["Mao","Gandhi","Mandela"];

var sizes = [4, 6, 3, 2, 1, 9];

var mixed = [34, "candy", "blue", 11];
Syntax:

var arrayName = [data, data, data];

// Any time you see data surrounded by [ ], it is an array.

//// Instructions:

// Make your own array called junk. 
// Put 4 bits of data in it (first 2 strings, then 2 numbers).

// Declare it using var.
// Put [ ] around your data.
// Separate each bit of data with a comma.
// End it with a semi-colon.
// Use console.log to print out jun

var junk = ["shoes", "gloves", 2, 16];

console.log(junk)


////////////// 
////// Lesson 10/13 Array positions

// It's nice that we can put a list of data into an array. 
// But now we need to learn how to get access to the data inside the array.

// The position of things in arrays is fixed. 
// So we just need to know the array name (here, it is junkData), 
// and the position of the data we want, and we're done.

var junkData = ["Eddie Murphy", 49, "peanuts", 31];

// Small complication: 
// the position (or the index) of each bit of data is counted starting from 0, not 1.

// First element in the array: junkData[0]
// Third element in the array: junkData[2]

// Arrays have 0-based indexing, so we start counting the positions from 0.

//// Instructions:

// Print out the fourth element of the array.

// Start with figuring out how to express what the fourth element in the array is.
// Then use console.log() to print things out!

console.log(junkData[3])


////////////// 
////// Lesson 11/13 Loops and arrays I

// Awesome job! 
// You've now learned about arrays, and how to access one element of the array. 
// But what if there were 100 elements in the array?

// For arrays, a useful way to systematically access every element 
// in the array is to use a for loop!

var cities = ["Melbourne", "Amman", "Helsinki", "NYC"];

for (var i = 0; i < cities.length; i++) {
    console.log("I would like to visit " + cities[i]);
}

// How does it work?
	// 1. the var name = [] declares the array. It has 4 elements.
	// 2. We then start the for loop on line 5.
	// 3. We see i starts off at value 0.
	// 4. The for loop runs until i < 4 (because cities.length equals 4. 
		// The array cities has 4 elements in it; see the Hint for more.)
	// 5. We will increment i by 1 each time we loop over.
	// 6. We print out cities[0], which is "Melbourne".
	// 7. We then start the loop again. Except now i = 1.
	// 8. It will print out cities[1], which is "Amman".
	// 9. This continues until i is no longer less than cities.length.


//// Instructions:

// Change the elements in the cities array. 
// You can put in as many elements as you like.
// Run the for loop and see them all printed out!

var cities = ["Melbourne", "Amman", "Helsinki", "NYC", "Brysbane", "The Moon", "Atlantis", 6];

for (var i = 0; i < cities.length; i++) {
    console.log("I would like to visit " + cities[i]);
}



////////////// 
////// Lesson 12/13 Loops and arrays II

// It's time for you to write your own array and loop over the array. 

// Remember to:
	// Put commas between each element in the array.
	// Put semi-colons between each bit of the for loop.
	// We suggest you use i as the iterator.
	// Beware of infinite loops!
	// Enjoy yourself while smashing through this coding!


//// Instructions:

// Create an array called names filled with 5 names.
// Write a for loop that prints "I know someone called " followed by names[i]. 
// Make sure there's a space between "called" and the name!
// Run your code and the five sentences should print out.

var names = ["A","B","C","D","E"];

for (var i = 0; i <names.length; i++) {
    console.log("I know someone called " + names[i]);
};


////////////// 
////// Lesson 13/13 Conclusion

// You've done an awesome job! 
// Loops are always a little tricky when you first meet them. 
// But they are worth learning because they are really useful.

// What now? You have so many useful tricks up your sleeve:
	// a. if / else statements
	// b. functions
	// c. for loops
	// d. booleans, arrays, variables, etc.

//// Instructions:

// The best way to get better at programming 
// is to use what you have learned to build something! 
// Click Save & Submit Code to finish.


///////////////////////////////////
///////////////////////////////////

//////////////
// Build a Name finder
//////////////


//////////////
////// Lesson 1/13 The Game





///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// 'While' Loops in JavaScript
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to 'While' Loops in JS
//////////////


//////////////	While loops: The Basics
////// Lesson 1/11 While we're at it

// Great work with for loops! 
// As a reminder, for loop syntax looks like this:

for (var i = start; i < end; i++) {
  // do something
}

// The counter variable i starts at "start", and stops looping when it reaches "end."

// But what if you didn't know ahead of time when to stop looping? 
// Say, for example, 
// you wanted to keep choosing playing cards from a deck until you get a spade. 
// You don't know how many cards you'll need to choose, so a for loop won't work.

// In situations like these where you don't know in advance when to stop looping,
// we can use a while loop.


//// Instructions:

// Check out the while loop in the editor. 
// Can you guess what it will do? 
// Hit "Save & Submit Code" when you think you know! (The answer is in the Hint.)

var coinFace = Math.floor(Math.random() * 2);

while(coinFace === 0){
	console.log("Heads! Flipping again...");
	var coinFace = Math.floor(Math.random() * 2);
}
console.log("Tails! Done flipping.");

// Don't worry about the Math.floor bit for now—we'll explain it soon!

// The code in the editor keeps flipping a coin until it is tails. 

// Here's how it works:

// 1. In line 1, we create a variable named coinFace, 
	// which is a random number that is either 0 (heads) or 1 (tails).

// 2. Then in lines 3-5 we keep flipping the coin as long as the coin turns up heads. 
	// If coinFace is 0 (heads), then the condition in the while loop will evaluate to true, 
	// and we flip the coin again.

// 3. If coinFace is 1 (tails), then the condition will be false, 
	// so we break out of the while loop and print Tails! Done flipping.



//////////////
////// Lesson 2/11 While syntax

// The while loop is ideal when you want to use a loop, 
// but you don't know how many times you'll have to execute that loop.

// In the example you just saw, 
// the computer was randomly flipping a coin: 
// while the coin came up heads (when coinFace equalled 0), 
// it would flip again, 
// and it would stop flipping once it got tails (when coinFace was 1). 
// Since the flip was random, we didn't know ahead of time how many loops we'd need.

// The syntax looks like this:

while(condition){
    // Do something!
}

// As long as the condition evaluates to true, 
// the loop will continue to run. 
// As soon as it's false, it'll stop. 
// (When you use a number in a condition, as we did earlier, 
// JavaScript understands 1 to mean true and 0 to mean false.)

// Since you've already mastered for loops, 
// this simpler syntax should be a breeze for you.


//// Instructions:

// Try it yourself—complete the while loop in the editor 
// so it will print out "I'm learning while loops!". 
// Do this by adding the condition between the parentheses—don't change line 5, 
// or you could get an infinite loop!

var understand = true;

while( understand === true ){
	console.log("I'm learning while loops!");
	understand = false;
}



//////////////
////// Lesson 3/11 A fellow of infinite loops

// Great work!

// We mentioned infinite loops in the previous exercise. 
// If you give a while loop a condition that is true 
// and you don't build in a way for that condition to possibly become false, 
// the loop will go on forever and your program will crash. 
// No good!

// To prevent this from happening, 
// you always need a way to ensure the condition between your while parentheses can change.

// You'll see the same code from the last exercise in the editor to the right, 
// only we've taken out the part that changes the loop's condition.


//// Instructions:

// DON'T run the code the way it is—you'll have to reload the window 
// to stop the infinite loop! 
// Instead, change the value of understand to something other than true (such as false) 
// on line 6 so the loop will exit.


understand = true;

while(understand){
	console.log("I'm learning while loops!");
	//Change the value of 'understand' here!
	understand = false
}



//////////////
////// Lesson 4/11 Brevity is the soul of programming

// You may have noticed that when we give a variable the boolean value true, 
// we check that variable directly—we don't bother with ===. 

// For instance,

var bool = true;
while(bool){
    //Do something
}
// is the same thing as

var bool = true;
while(bool === true){
    //Do something
}
// but the first one is faster to type. 
// Get in the habit of typing exactly as much as you need to, and no more!

// If you happen to be using numbers, as we did earlier, you could even do:

var myNumber = 1;
while(myNumber) {
    // Do something!
}

//// Instructions:

// We've written the less succinct version in the editor. 

var bool = true;

while(bool === true){
    console.log("Less is more!");
    bool = false;
}

// Correct it to the more elegant version!

var bool = true;

while(bool){
    console.log("Less is more!");
    bool = false;
}


//////////////
////// Lesson 5/11 Practice makes perfect

// Okay. Time for you to create a while loop from scratch!

// We've set up a function, loop, for you to write your while loop in, 
// as well as created the empty loop.

// Remember to set up the condition you're checking outside the loop—
// if you do it in the loop, 
// it will keep resetting and the loop could go on forever!


//// Instructions:

// Write a while loop that logs "I'm looping!" to the console three times. 
// You can do this however you like, but NOT with three console.log calls. 
// Check the Hint if you need help!


var loop = function(){
    var i = 0
	while(i < 3){
		//Your code goes here!
		console.log("I'm looping!");
		i = i + 1;
	}
};

loop();


//////////////
////// Lesson 6/11 Solo flight

// Great work! Let's try another. 
// This time, no help at all! (Well, some help—check the Hint if you get stuck.)


//// Instructions:

// Inside the soloLoop function, 
// write a while loop that takes an initial condition that's true. 

// Your loop should log "Looped once!" to the console, 
// then change that initial condition to false.

// MAKE SURE to set your condition to false in the body of your loop. 
// Otherwise, you'll loop forever!

//Remember to make your condition true outside the loop!

var soloLoop = function(){
  //Your code goes here!
  var i = true
  while(i){
      console.log("Looped once!");
      i=false;
  }
};

soloLoop();


//////////////
////// Lesson 7/11 Mid-lesson breather

// Great work so far! You've learned:
	// What while loops are
	// while loop syntax
	// How to avoid infinite loops

// Next up, we'll cover the do/while loop, 
// when to use while and when to use for, 
// and then put it all together in a loop-the-loop review.


//////////////
////// Lesson 8/11 When to 'while' and when to 'for'

// As we mentioned, for loops are great for doing the same task 
// over and over when you know ahead of time how many times 
// you'll have to repeat the loop. 

// On the other hand, while loops are ideal when you have to loop, 
// but you don't know ahead of time how many times you'll need to loop.

// As you saw, however, you can combine a while loop with a counter variable 
// to do the same kind of work a for loop does. 
// In these cases, it's often a matter of preference.


//// Instructions:

// Write two loops in the editor: 
// one while, one for. 

// No restrictions on this one; 
// just make sure your loops are syntactically correct, 
// and be careful to avoid infinite loops!

var i = 0
while(i < 10){
    console.log("stuff");
    i=i+1;
}

for(var i = 0; i < 10; i++){
	console.log("stuff");
}


//////////////
////// Lesson 9/11 The 'do' / 'while' loop

// Sometimes you want to make sure your loop runs at least one time no matter what. 
// When this is the case, you want a modified while loop called a do/while loop.

// This loop says: "Hey! Do this thing one time, 
// then check the condition to see if we should keep looping." 

// After that, it's just like a normal while: the loop will continue 
// so long as the condition being evaluated is true.

//// Instructions:

// Click Save & Submit Code to see the loop in action. 
// It runs once because do tells it to, 
// but then never again because loopCondition is false!


var loopCondition = false;

do {
	console.log("I'm gonna stop looping 'cause my condition is " + loopCondition + "!");	
} while (loopCondition);


//////////////
////// Lesson 10/11 To learn it, you gotta 'do' it

// Your turn! Now that you've seen how do/while loops work, 
// you can easily write your own. 
// (Check the Hint if you need a syntax refresher!)

// Your loop should print a string of your choice to the editor one time. 
// Remember: make sure you give your while condition a way to become false, 
// or it'll loop forever!


//// Instructions:

// Write a do/while loop inside the function we've created for you, getToDaChoppa. 
// The function should log a string of your choice to the console. do it now!

var getToDaChoppa = function(){
  // Write your do/while loop here!
  var i = true;
  do {
      console.log("hi");
      i = false;
  } while (i);
};

getToDaChoppa();


//////////////
////// Lesson 11/11 Review

// Awesome work! 
// You've now learned about all the loops there are: for, while, and do.


//// Instructions:

// To finish up and prove your loop mastery, 
// write three syntactically correct loops in the editor: 
// one for, 
// one while, 
// and one do. 

// Beware of infinite loops!

// comma where a semi colon should be
for (var i=0;i<10,i++) {
	console.log("stuff");
};

var i = true;
while (i) {
	console.log("stuff");
	i=false;
};

var j = false;
do {
	console.log("stuff");
} while (j);

////// OR

var i = false;
do {
      console.log("hi");
} while (i);


var i = 0;
while(i < 10){
    console.log("stuff");
    i=i+1;
}

for(var i = 0; i < 10; i++){
	console.log("stuff");
}

/////


///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// Control Flow
///////////////////////////////////
///////////////////////////////////


//////////////
// More on Control Flow in JS
//////////////


//////////////	The Story So Far: If, Else, and Loops
////// Lesson 1/14 If / else

// If / else
// You've learned about if and else, and how they control what your program does. 
// Here's a quick refresher on the syntax:

if (/* Some condition */) {
    // Do something
} else if (/* Some other condition */) {
    // Do something else
} else {    // Otherwise
    // Do a third thing
}


//// Instructions:

// Write an if / else statement inside the isEven function. 
// It should return true; if the number it receives is evenly divisible by 2. 
// Otherwise (else), it should return false;.

// Make sure to return - don't use console.log()!

var isEven = function(number) {
  // Your code goes here!
  if (number%2 === 0) {
      return true;
  } else {
      return false;
  }
};

console.log(isEven(10))


//////////////
////// Lesson 2/14 If / else if / else

// Good! Let's also get some practice in with else if, 
// as well as learn about a fancy new function: isNaN.

// If you call isNaN on something, it checks to see if that thing is not a number. 

// So:
isNaN('berry'); // => true
isNaN(NaN); // => true
isNaN(undefined); // => true
isNaN(42);  // => false

// Be careful: if you call isNaN on a string that looks like a number,
// like '42', JavaScript will try to help by automatically converting the string '42' 
// to the number 42 and return false (since 42 is a number).

// Note that you can't just do
isNaN(unicorns);

// unless you've already defined the variable unicorns. 
// You can, however, do
isNaN("unicorns"); // => true


//// Instructions:

// Add an else if branch to your existing if/else statement. 
// If the number put into the function is not a number at all, 
// instead of return true; or return false;, 
// the function should return a string that tells the user that their input isn't a number. 
// (This string can say whatever you like.)

var isEven = function(number) {
  // Your code goes here!
  if (number%2 === 0) {
      return true;
  } else if (isNaN(number)) {
  	  return 'number is a NaN';
  } else {
      return false;
  }
};

console.log(isEven(10))
console.log(isEven('1th'))


//////////////
////// Lesson 3/14 For or while

// Great! Just one more bit of review and we'll move on to the new stuff.


//// Instructions:

// Create a for or while loop in the editor. 
// It can do anything you like! 
// (Just be careful—if you accidentally create an infinite loop, you'll crash your browser.) 
// Check the Hint if you need a syntax review.

for(var i = 0; i < 10; i++){
	console.log("stuff");
}



//////////////
////// Lesson 4/14 Sneak preview: the switch statement

// As you might imagine, 
// if you have a lot of choices you want to cover in a program, 
// it might be annoying to type else if () ten times. 
// That's why JavaScript has the switch statement!

// switch allows you to preset a number of options (called cases), 
// then check an expression to see if it matches any of them. 
// If there's a match, the program will perform the action for the matching case; 
// if there's no match, it can execute a default option.

var lunch = prompt("What do you want for lunch?","Type your lunch choice here");

switch(lunch){
  case 'sandwich':
    console.log("Sure thing! One sandwich, coming up.");
    break;
  case 'soup':
    console.log("Got it! Tomato's my favorite.");
    break;
  case 'salad':
    console.log("Sounds good! How about a caesar salad?");
    break;
  case 'pie':
    console.log("Pie's not a meal!");
    break;
  default:
    console.log("Huh! I'm not sure what " + lunch + " is. How does a sandwich sound?");
}


//// Instructions:

// Take a look at the code in the editor. 
// Can you see how the switch statement works?

// Prompts the user for a lunch choice.
// Returns a reply based on that choice.



////////////// Introducing the Switch statement
////// Lesson 5/14 Adding to an existing switch

// The switch statement is put together like this:

switch (/*Some expression*/) {
    case 'option1':
        // Do something
        break;
    case 'option2':
        // Do something else
        break;
    case 'option3':
        // Do a third thing
        break;
    default:
       // Do yet another thing
}

// JavaScript will try to match the expression between the switch() parentheses to each case. 
// It will run the code below each case if it finds a match, 
// and will execute the default code if no match is found.


//// Instructions:

// Our switch statement needs a case for 'yellow'. 
// Add it in and make it log a string of your choice to the console 
// (it should be different from the default string).

// Don't forget to end your case with a break statement—otherwise, 
// it will go on and execute the code for default, too! 
// We don't want that.

var color = prompt("What's your favorite primary color?","Type your favorite color here");

switch(color) {
  case 'red':
    console.log("Red's a good color!");
    break;
  case 'blue':
    console.log("That's my favorite color, too!");
    break;
  //Add your case here!
  case 'yellow':
  	console.log("That's the color of the sun.");
  	break;
  default:
    console.log("I don't think that's a primary color!");
}


//////////////
////// Lesson 6/14 Practice with switch

// Now that you've added cases to an existing switch, 
// let's practice adding a default block.


//// Instructions:

// Add the default block at the bottom of the switch statement, 
// then run the code a few times with different inputs. 
// switch: super useful!

var candy = prompt("What's your favorite candy?","Type your favorite candy here.");

switch(candy) {
  case 'licorice':
    console.log("Gross!");
    break;
  case 'gum':
    console.log("I like gum!");
    break;
  case 'beets':
    console.log("...is that even a candy?");
    break;
  // Add your code here!
  default:
  	console.log("that is not a candy");
}


//////////////
////// Lesson 7/14 More practice with switch

// You know what they say: practice makes perfect!


//// Instructions:

// We've given you the empty skeleton of a switch statement. 
// Complete the existing case, then add at least one additional case 
// and a default behavior with whatever console.log() calls you like.

var answer = prompt("Add your question here!");

switch(answer) {
  case '':
    console.log();
    break;
  // Add your code here!
  case 'What is this?':
  	console.log("Good question.");
  	break;
  case 'who are you?':
  	console.log("Good question.");
  	break;
  default:
  	console.log("That is not a question.");
}


//////////////
////// Lesson 8/14 All on your own

// Great work! 
// Now it's time to put a switch statement together all on your lonesome.


//// Instructions:

// Create your own switch statement in the editor. 
// It can do anything you like! 
// Make sure to include at least three cases and a default.

var answer = prompt("Stuff please");

switch(answer) {
	case 'Hello!':
		console.log(answer);
		break;
	case 'Good Bye!':
		console.log("I'm not done yet, sit down!");
		break;
	case 'letters':
		console.log("Don't know about them");
		break;
	default:
		console.log("End");
}



//////////////
////// Lesson 9/14 Mid-lesson breather

// Well done! Even though we've been focusing on switch, we've covered a lot so far. 

// You've:
	// Reviewed if/else if/else
	// Reviewed for and while
	// Learned about the switch statement and how to use it instead of multiple if/elses
	// Covered switch syntax
	// Written your own switch!


//// Instructions:

// When you're ready, click Save & Submit Code to move on to the last section 
// of this lesson: logical operators like 'and', 'or', and 'not'.




////////////// Logical Operators
////// Lesson 10/14 Overview

// So far we've seen how to control our programs given a single condition: 
// whether one variable is equal to a certain value, for instance. 
// But what if we want to check more than one variable?

// For this, we'll need logical operators. 
// JavaScript has three: 
	// and (&&), 
	// or (||), 
	// and not (!).

// Using these, we can check several variables at once! 
// Check out the code in the editor.

// Complete lines 3 and 4!

var iLoveJavaScript = ;
var iLoveLearning = ;

if(iLoveJavaScript && iLoveLearning) {
  // if iLoveJavaScript AND iLoveLearning:
  console.log("Awesome! Let's keep learning!");
} else if(!(iLoveJavaScript || iLoveLearning)) {
  // if NOT iLoveJavaScript OR iLoveLearning:
  console.log("Let's see if we can change your mind.");
} else {
  console.log("You only like one but not the other? We'll work on it.");
}


//// Instructions:

// Starting to make sense? 
// Set both variables in the editor to true and hit Save & Submit Code to see what happens!

var iLoveJavaScript = true;
var iLoveLearning = true;



////////////// Logical Operators
////// Lesson 11/14 AND

// The logical operator 'and' is written in JavaScript like this: &&. 
// It evaluates to true when both expressions are true; 
// if they're not, it evaluates to false.

true && true;    // => true
true && false;   // => false
false && true;   // => false
false && false;  // => false


//// Instructions:

// Create two variables, hungry and foodHere, 
// and set them both equal to true. 
// Inside the eat function, 
// create an if statement that returns true only if both hungry and foodHere are true, 
// and false otherwise. 
// The function eat should take no input and hungry and foodHere should both be globals.


// Declare your variables here!
var hungry = true;
var foodHere = true;

var eat = function() {
  // Add your if/else statement here!
  if(hungry && foodHere){
  	return true;
  } else {
  	return false;
  }
};
console.log(eat());


////////////// Logical Operators
////// Lesson 12/14 Or

// The logical operator or is written in JavaScript like this: ||. 
// It evaluates to true when one or the other or both expressions are true; 
// if they're not, it evaluates to false.

true || true;     // => true
true || false;    // => true
false || true;    // => true
false || false;   // => false

// The or operator is written with two vertical bars ||. 
// The vertical bar character is located right above the Enter key on your keyboard.


//// Instructions:

// Create two variables, 'tired' and 'bored', and set one equal to true and the other equal to false. 
// (It doesn't matter which is which.) 
// Inside the nap function, 
// create an if statement that returns true if either tired or bored (or both!) are true, 
// and false otherwise.

// Declare your variables here!
var tired = true;
var bored = false;

var nap = function() {
  // Add your if/else statement here!
  if (tired || bored){
      return true
  } else {
      return flase
  }
};


////////////// Logical Operators
////// Lesson 13/14 Not

// The logical operator not is written in JavaScript like this: !. 
// It makes true expressions false, and vice-versa.

!true;   // => false
!false;  // => true


//// Instructions:

// Declare a variable called 'programming' and set it to false. 
// Then, write an if/else statement inside happy so that happy returns true 
// if programming is false and false otherwise.


// Declare your variables here!
var programming = false;

var happy = function() {
  // Add your if/else statement here!
  if(!programming){
  	return true;
  } else {
  	return false;
  }
};

console.log(happy());


//////////////
////// Lesson 14/14 Review

// Well done! That last one was particularly tricky.

// In this lesson you:

// Reviewed control flow syntax
// Learned about the switch statement
// Learned about the logical operators and (&&), or (||), and not (!)


//// Instructions:

// When you're ready, click Save & Submit Code to finish this lesson 
// and move onto the next JavaScript project!



///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// Data Structures
///////////////////////////////////
///////////////////////////////////


//////////////
// Arrays and Objects in JS
//////////////


//////////////	Reviewing Arrays
////// Lesson 1/17 You know this!

// You know this!
// You already know about arrays, so we won't spend a lot of time going over them. 
// Go ahead and check out the past exercises on arrays if you need a refresher.


//// Instructions:

// Create an array called list in the editor. 
// It can contain any data you want! 
// Make sure it has at least three elements.

var list = ['1','2','3','4'];
console.log(typeof list)

	// object



//////////////	Reviewing Arrays
////// Lesson 2/17 Access by offset

// Good! Do you remember how to access an element of an array by offset 
// (with the [] notation)? Check the Hint if you need help.


//// Instructions:

// Log the third element of the languages array to the console. 
// Make sure to do this by accessing the third element's index.

var languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"];

console.log(languages[2])


//////////////	Reviewing Arrays
////// Lesson 3/17 Array properties

// Good work! 
// If you remember, arrays have a property in common with strings: they can both use .length. 
// When you call .length on an array, it returns the number of elements that array has.

//// Instructions:

// Under your existing code, log the number of elements in languages to the console.

var languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"];

console.log(languages[2])
console.log(languages.length)


//////////////	Reviewing Arrays
////// Lesson 4/17 Iterating over an array

// By combining all these ideas with a for loop, 
// you can iterate over the languages array and print out each element in turn!

//// Instructions:

// Go ahead and use a for loop to log each element of the languages array to the console.

var languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"];

for(var i=0;i<languages.length;i++){
	console.log(languages[i]);
};


//////////////	More with Arrays
////// Lesson 5/17 Heterogeneous arrays

// Now that we've reviewed some array basics, it's time to cover a little new ground.

// First, it's not necessary for you to put the same type of data in an array! 
// For instance, you don't have to have

var pronouns = ["I", "you", "we"];
var numbers = [1, 2, 3];

// You can have a heterogeneous array, which means a mixture of data types, like so:

var mix = [42, true, "towel"];


//// Instructions:

// Create a heterogeneous array called myArray with at least three elements. 
// The first element should be a number, 
// the second should be a boolean (true or false), 
// and the third should be a string. 
// Feel free to add more elements of any type if you like!

var myArray = [1,true,'a','abc',123,true,'def',456,false];


//////////////	More with Arrays
////// Lesson 6/17 Arrays of arrays

// Good! The next thing to know is that not only can you put a mixture of types in an array, 
// you can even put other arrays inside arrays. 
// You can make a two-dimensional array by nesting arrays one layer deep, 

// like so:

var twoDimensional = [[1, 1], [1, 1]];

// This array is two-dimensional because it has two rows that each contain two items. 
// If you were to put a new line between the two rows, 
// you could log a 2D object—a square—to the console, 
// like so:
[1, 1]
[1, 1]


//// Instructions:

// Create a two-dimensional array called newArray in the editor. 
// It should have three rows and three columns containing any data you like.

var newArray = [[1,1,1],[1,1,2],[1,2,3]];


//////////////	More with Arrays
////// Lesson 7/17 Jagged arrays

// Great work! That's a fine-looking multidimensional array you've got there. 
// (Yours is nested once, so it's a two-dimensional array, 
// but if you really wanted, 
// you could put arrays inside arrays inside arrays for even more dimensions.)

// Sometimes you want arrays that aren't as nice and even as your 3 x 3 two-dimensional array: 
// you may have three elements in the first row, 
// one element in the second row, 
// and two elements in the third row. 
// JavaScript allows those, and they're called jagged arrays.


//// Instructions:

// Create a jagged array called jagged. 
// You can place whatever you like in it! 
// The only requirement is that it have at least two rows 
// (that is, the first two elements need to be arrays), 
// and those rows cannot be the same length.

var jagged = [[1,2,3,4,5],['hello','good bye'],[true,false]];


//////////////	More with Arrays
////// Lesson 8/17 Mid-lesson breather

// Well done! So far you've:

	// Reviewed arrays, how to access an array by offset, array properties, and iterating over arrays
	// Learned about heterogenous arrays
	// Learned about multidimensional arrays
	// Learned about jagged arrays


//// Instructions:

// Take a minute to reflect on what we've done so far. 
// Then, when you're ready, click Save & Submit Code to learn about our last 
// (and most powerful) data type: objects!


//////////////	Introduction to Objects
////// Lesson 9/17 Nouns and verbs together

// Let's go back to the analogy of computer languages being like regular spoken languages. 
// In English, you have nouns (which you can think of as "things") 
// and verbs (which you can think of as "actions"). 
// Until now, our nouns (data, such as numbers, strings, or variables) 
// and verbs (functions) have been separate.

// No longer!

// Using objects, we can put our information 
// and the functions that use that information in the same place.

// You can also think of objects as combinations of key-value pairs (like arrays), 
// only their keys don't have to be numbers like 0, 1, or 2: 
// they can be strings and variables.

//// Instructions:

// We've put an example of how objects can be used in the editor. 
// Click Save & Submit Code to see objects in action!

var phonebookEntry = {};

phonebookEntry.name = 'Oxnard Montalvo';
phonebookEntry.number = '(555) 555-5555';
phonebookEntry.phone = function() {
  console.log('Calling ' + this.name + ' at ' + this.number + '...');
};

phonebookEntry.phone();


//////////////	Introduction to Objects
////// Lesson 10/17 Object syntax

// Did you see that? 
// The phonebookEntry object handled data (a name and a telephone number) 
// as well as a procedure (the function that printed who it was calling).

// In that example, 
// we gave the key name the value 'Oxnard Montalvo' 
// and the key number the value '(555) 555-5555'. 

// An object is like an array in this way, 
// except its keys can be variables and strings, not just numbers.

// Objects are just collections of information (keys and values) between curly braces, 
// like this:

var myObject = {
    key: value,
    key: value,
    key: value
};

//// Instructions:

// Using the above syntax as a guide, create an object, me, in the editor. 
// It should have a name key with the value of your name (as a string) 
// and an age key with the value of your age (as a number).


var me = {
    name: 'christian',
    age: 28
};

console.log('hello ' + me.name + '. You are '+ me.age + '!');



//////////////	Introduction to Objects
////// Lesson 11/17 Creating a new object

// Great work! You just created your very first object.

// There are two ways to create an object: 
	// using object literal notation (which is what you just did) 
	// and using the object constructor.

// Literal notation is just creating an object with curly braces, like this:

var myObj = {
    type: 'fancy',
    disposition: 'sunny'
};

var emptyObj = {};

// When you use the constructor, the syntax looks like this:

var myObj = new Object();

// This tells JavaScript: 
// "I want you to make me a new thing, and I want that thing to be an Object.

// You can add keys to your object after you've created it in two ways:

myObj["name"] = "Charlie";
myObj.name = "Charlie";

// Both are correct, and the second is shorthand for the first. 
// See how this is sort of similar to arrays?

//// Instructions:

// Recreate your me object in the editor, but this time, use the object constructor.
// Once you make it, use either the [] notation or the . notation to give it a name property 
// with a string value (your name) 
// and an age property with a number value (your age).

var me = new Object();

me["name"] = "christian";
me.age = 28;

console.log('hello ' + me.name + '. You are '+ me.age + '!');


//////////////	Introduction to Objects
////// Lesson 12/17 Practice makes perfect

// Great work! Let's make a few more objects, just for practice.

//// Instructions:

// Create three objects called object1, object2, and object3 in the editor. 
// Use either literal notation or the object constructor, 
// and give your objects any properties you like!


var object1 = {
	name:'ca',
	age:28,
	height:184,
	mood:'grumpy'
};

var object2 = {
	name:'jf',
	age:60,
	height:180,
	mood:'happy'
};

var object3 = new Object();

object3["name"] = 'pw';
object3["age"] = '43';
object3.height = 174;
object3.mood = 'helpful';


console.log('hello ' + object1.name + '. You are '+ object1.age + '!');
console.log('I am ' + object1.height + '. I feel'+ object1.mood + '!');

console.log('hello ' + object2.name + '. You are '+ object2.age + '!');
console.log('I am ' + object2.height + '. I feel'+ object2.mood + '!');

console.log('hello ' + object3.name + '. You are '+ object3.age + '!');
console.log('I am ' + object3.height + '. I feel'+ object3.mood + '!');

// > hello ca. You are 28!
// > I am 184. I feelgrumpy!
// > hello jf. You are 60!
// > I am 180. I feelhappy!
// > hello pw. You are 43!
// > I am 174. I feelhelpful!


//////////////	Introduction to Objects
////// Lesson 13/17 Review

// Awesome! We've thrown a lot at you, but now you know:

	// What objects are
	// Object syntax
	// How to create your own objects


//////////////	Review
////// Lesson 14/17 Heterogeneous arrays

// Let's warm up with some arrays! 
// Let's make an array that's a veritable potpourri of data types.

//// Instructions:

// Create an array, myArray. 
// Its first element should be a number, 
// its second should be a boolean, 
// its third should be a string, 
// and its fourth should be... an object! 
// You can add as many elements of any type as you like after these first four.

var object = {
	name:'jf',
	age:60,
	height:180,
	mood:'happy'
};

var myArray = [132, true, 'wtf', object]



//////////////	Review
////// Lesson 15/17 Multidimensional arrays

// Good! Now let's create a 2D array. 
// Not only that, but a 2D array that's jagged. 
// Remember, that means it's an array of arrays, 
// and its nested arrays aren't all the same length! 

// For example:

var aList = [ [1, 4, 2], [7] ];

//// Instructions:

// Make an array called newArray. 
// It should be 2D (that is, it should contain two elements that, in turn, are arrays) 
// and jagged (those two arrays should be of different lengths, like in the example above).
// Make sure at least one of the elements in one of your rows is an object.

var object = {
	name:'jf',
	age:60,
	height:180,
	mood:'happy'
};

var newArray = [[1,2], [object]]


//////////////	Review
////// Lesson 16/17 Editing an existing object

// Nice work! Now let's do a little work with objects. 
// We'll start by modifying an existing one.

//// Instructions:

// Add a key called interests to myObject. 
// Give this key an array value (the array can contain whatever you like).

var myObject = {
  name: 'Eduardo',
  type: 'Most excellent',
  // Add your code here!
  interests: ['football',1234,true,this.name]
};

console.log(myObject.interests)
// > [ 'football', 1234, true, '' ]


//////////////	Review
////// Lesson 17/17 Creating your own objects

// You're almost there! 
// Last step: forge your very own object in the fires of Mount JavaScript.

//// Instructions:

// Create your own object called myOwnObject.
// Give it whatever properties you like! 
// (Be sure to give it at least one.) 
// You can use either literal notation or the object constructor.

var myOwnObject = {
    name:'ca',
    runs:10,
    sees:100
};
myOwnObject.swims = 5;
myOwnObject["flies"] = 13000;

console.log(myOwnObject.flies);


///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////


///////////////////////////////////
///////////////////////////////////
// Objects I
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to Objects I
//////////////


//////////////	Review: The story so far...
////// Lesson 1/33 We've come a long, long...

// If yellow triangle warnings appear in the editor next to any code 
// we provide in any exercise, it is fine to ignore them.

// The very basic building block of JavaScript are primitive data types. 
// We know of three primitives:

strings (e.g. "dogs go woof!")
numbers (e.g. 4, 10)
booleans (e.g. false, 5 > 4)

// We learned about the use of comparators (eg. >, <=, !==, etc.). 
// One really important thing to note is that any time comparisons are made, 
// a Boolean value is returned.


//// Instructions:

// There is a long and ugly expression in the editor. 
// Overall, it evaluates to a Boolean 
// (i.e., either the entire statement is true, or it is false).

// What does this expression in the editor evaluate to?

(((3 * 90) === 270) || !(false && (!false)) || "bex".toUpperCase() === "BEX");

// Declare a variable named answer. 
// Assign to it the Boolean value that the expression evaluates to. 
// Delete the default code in the editor and run your code.

// (3 * 90) === 270) is true and the rest are OR Logical Operators so it must be true.

var answer = true;


//////////////	Review: The story so far...
////// Lesson 2/33 Through the hard times...

// We know two ways of storing data types. 
// We can use variables or arrays. 
// We use variables to store data (like strings or numbers) that we’d later want to access.

// An array is exactly the same as a variable in that it stores data. 
// The difference is that an array can store many more values while a variable can only store one.

// To access arrays, we use bracket notation and remember that arrays use 0-based indexing 
// (i.e., the first value in an array is at position 0).


//// Instructions:

// Look at the array multiplesOfEight, and find the one that doesn't fit.

// Replace X in line 6 such that the variable answer is assigned the Boolean value of true.


// Here is an array of multiples of 8. But is it correct?
var multiplesOfEight = [8,16,24,32,40,58];

// Test to see if a number from the array is NOT a true
// multiple of eight. Real multiples will return false.
var answer = multiplesOfEight[5] % 8 !== 0;


//////////////	Review: The story so far...
////// Lesson 3/33 ...And the good!

// We're going to play a game of FizzBuzz. 
// The rules are simple. 
// We want to count from 1 to 20. 
// But if the number is divisible by 3, we're going to print "Fizz". 
// And if the number is divisible by 5 we're going to print "Buzz".

// What will we print if the number is divisible by 3 AND 5? 
// That's right! "FizzBuzz"!

// There are many ways to do this, 
// but we'd like you to use a nested conditional in this exercise.

//// Instructions:

// 1. Print out the numbers from 1 - 20.
// 2. The rules:
	// For numbers divisible by 3, print out "Fizz".
	// For numbers divisible by 5, print out "Buzz".
	// For numbers divisible by both 3 and 5, print out "FizzBuzz" in the console.
	// Otherwise, just print out the number.

for(var i = 1; i < 21 ; i++){
    if((i%3===0)&&(i%5===0)){
    	console.log("FizzBuzz");
    } else if ((i%3===0)&&(i%5!==0)){
    	console.log("Fizz");
    } else if ((i%3!==0)&&(i%5===0)){
    	console.log("Buzz");
    } else {
    	console.log(i);
    };
};


//////////////	Review: The story so far...
////// Lesson 4/33 I have to celebrate you baby

// This exercise has lots of movies and reviews to type in. 
// You might wonder, "Is this teaching coding or typing?!"

// But there's a reason why there are so many cases to deal with. 
// We want to show that if we used if-else statements, it would be inefficient. 
// What alternative to if / else can we use?

//// Instructions:

// Imagine you have a movie collection, 
// and you want to write code that returns your review for each one. 

// Here are the movies and your reviews:

"Toy Story 2" - "Great story. Mean prospector."
"Finding Nemo" - "Cool animation, and funny turtles."
"The Lion King" - "Great songs."

// Write a function named getReview that takes in a movie name 
// and returns its review based on the information above. 
// If given a movie name not found just return "I don't know!". 
// Use a structure learned in an earlier lesson (NOT if/else statements) to write this function.

var getReview = function (movie) {
	switch (movie){
		case "Toy Story 2":
			return ("Great story. Mean prospector.");
			break;
		case "Finding Nemo":
			return ("Cool animation, and funny turtles.");
			break;
		case "The Lion King":
			return ("Great songs.");
			break;	
		default:
			return ("I don't know!");
	};
};

console.log(getReview("The Lion King"));


//////////////	Review: The story so far...
////// Lesson 5/33 I have to praise you like I should!

// Congratulations for making it this far! 
// We hope you're enjoying the courses and feel more comfortable programming in JavaScript.

// We have a number of exciting things in store for you and can't wait to roll them out!

//// Instructions:

// If you're ready to start learning about objects, print in the console: "I'm ready for Objects!"

console.log("I'm ready for Objects!")


//////////////	What's an Object
////// Lesson 6/33 Intro

// We have discussed four data types: numbers, strings, booleans and arrays.

// In this lesson, we focus on a fifth data type: objects. 
// This data type is a little bit more complex. 
// Objects allow us to represent in code real world things and entities 
// (such as a person or bank account). 
// We do this by storing all relevant information in one place—an object.

// How do we create an object? 
// Like declaring a variable, or defining a function, we use var, 
// followed by the name of the object and an equals sign. 
// Each object then:
	// starts with {
	// has information inside
	// ends with };

//// Instructions:

// Create an object called bob that has no information inside the brackets.

var bob = {
    // no info
};

//////////////	What's an Object
////// Lesson 7/33 Properties

// Let's review what we previously covered. 
// Each piece of information we include in an object is known as a property. 
// Think of a property like a category label that belongs to some object. 
// When creating an object, each property has a name, 
// followed by : and then the value of that property.
// For example, if we want Bob's object to show he is 34, we'd type in age: 34.

// age is the property, and 34 is the value of this property. 
// When we have more than one property, they are separated by commas. 
// The last property does not end with a comma.

//// Instructions:

// See the console for the object I have created about myself. 
// Can you create an object called me that describes your age and which country you live in?

var Spencer = {
  age: 22,
  country: "United States"
};

// make your own object here called me

var me = {
	age: 28,
	country: "UK"
};

//////////////	What's an Object
////// Lesson 8/33 Accessing Properties

// Now that we know how to make objects with properties, 
// let's look at how we actually use them!

// Notice our example objects bob and susan. 
// In this case both bob and susan each have two properties, name and age.

var bob = {
  name: "Bob Smith",
  age: 30
};
var susan = {
  name: "Susan Jordan",
  age: 25
};
// here we save Bob's information
var name1 = bob.name;
var age1 = bob.age;
// finish this code by saving Susan's information
var name2 =
var age2 =

// After creating our objects we have added code to access these properties. 
// Notice that we save bob's name, "Bob Smith", into the global variable name1. 

//// Instructions:

// Finish the exercise by filling in the code to access the name and age for susan 
// and save those into the given global variables.

var name2 = susan.name;
var age2 = susan.age;


//////////////	What's an Object
////// Lesson 9/33 Accessing Properties, Part 2

// In the last exercise, we accessed properties using what is known as dot notation. 
// Good name, right? 
// So to access a property, we use ObjectName.PropertyName (e.g., bob.name)

// In addition to dot notation, we can also access properties using bracket notation. 
// In this case we use ObjectName["PropertyName"] to access the desired property. 
// Note, we need " " around the property's name.

// Take a look at our next example object called dog. 
// Notice how we save the dog's species into a variable by accessing the species 
// property of dog using bracket notation.

// Take a look at our next example object, a dog
var dog = {
  species: "greyhound",
  weight: 60,
  age: 4
};

var species = dog["species"];
// fill in the code to save the weight and age using bracket notation
var weight =
var age =

//// Instructions:

// Use bracket notation to save the dog's weight and age into variables as well.

var weight = dog["weight"]
var age = dog["age"]


//////////////	What's an Object
////// Lesson 10/33 Another Way to Create

// The method we've used to create objects uses object literal notation—that is, 
// creating a new object with { } and defining properties within the brackets.

// Another way of creating objects without using the curly brackets { } 
// is to use the keyword new. 
// This is known as creating an object using a constructor.

// The new keyword creates an empty object when followed by Object(). 
// The general syntax is: 

var objectName = new Object();

// We then have to fill this object with properties and labels. 
// How do we do that? 
// Check out the creation of the object bob to see what we do. 
// We create the name property for the object bob by using bob.name 
// and assigning that to a value. 

// Contrast this to how we define properties for the susan1 object.

// Our bob object again, but made using a constructor this time 
var bob = new Object();
bob.name = "Bob Smith";
bob.age = 30;
// Here is susan1, in literal notation
var susan1 = {
  name: "Susan Jordan",
  age: 24
};
// Make a new susan2 object, using a constructor instead

//// Instructions:

// Inspect the susan1 object carefully 
// and note the use of object literal notation.

// Use constructor notation to create susan2, 
// which should have the same properties and values as susan1.

var susan2 = new Object();
susan2.name = "Susan Jordan";
susan2.age = 24;


//////////////	What's an Object
////// Lesson 11/33 Putting it all together

// We've learned how to make objects in two different ways. 
// Both are valid, and you can use which one you prefer.

// Let's practice how to use both one more time.

//// Instructions:

// Use literal notation to finish the snoopy object. 
// Remember literal notation is the one where we fill in { } with separate properties 
// and values with colons. 
// Each property is separated by a comma.

// snoopy should have two properties, a species of "beagle" and age of 10.

// Then make buddy, a 5 year-old golden retriever, using constructor notation.
// This notation involves using the key word new to create an empty object. 
// Then we fill it in using dot notation.

// help us make snoopy using literal notation
// Remember snoopy is a "beagle" and is 10 years old.
var snoopy = {
	species: "beagle",
	age: 10
};

// help make buddy using constructor notation
// buddy is a "golden retriever" and is 5 years old
var buddy = Object();
buddy.species = "golden retriever";
buddy.age = 5;


//////////////	What's an Object
////// Lesson 12/33 More Practice Making Objects

// Nice job! 
// Let's do one more example to get the hang of making objects with desired properties.

//// Instructions:

// Create an object named 'bicycle' that has 3 properties:

	// a speed of 0
	// a gear of 1
	// a frame_material of "carbon fiber"

var bicycle = Object();
bicycle.speed = 0;
bicycle["gear"] = 1;
bicycle.frame_material = "carbon fiber";


//////////////	A Method to the Madness
////// Lesson 13/33 Function Review

// In this lesson we are going to focus on methods. 
// Methods are an important part of object oriented programming (OOP). 
// OOP is an important part of programming which we'll dive into later.

// Methods are similar to functions. 
// To prepare for methods, let's do a quick refresher on functions.
// Functions are defined using the function keyword followed by:

// A pair of parentheses ( ) with optional parameters inside.
// A pair of curly braces with the function's code inside { }.
// A semicolon ;.
// And when we call the function, we can put inputs (arguments) for the parameters.

// For example, the square function takes x as its parameter 
// and returns that parameter squared.

// Accepts a number x as input and returns its square
var square = function (x) {
  return x * x;
};

//// Instructions:

// Define the function multiply. 
// It should take two parameters, x and y, and return the product.
// Then call your function, passing in any two arguments.

var multiply = function(x,y) {
	return x * y;
};

console.log(multiply(3,4))


//////////////	A Method to the Madness
////// Lesson 14/33 So What's a Method?

// In the last section, we discussed properties. 
// We can think of properties as variables associated with an object. 
// Similarly, a method is just like a function associated with an object.

// Let's look at bob, our same person object from the last lesson. 
// Instead of just having the properties name and age, 
// bob also has a method called setAge. 
// As you can probably guess, 
// this method sets bob's age to whatever argument you give it.

// here is bob again, with his usual properties
var bob = new Object();
bob.name = "Bob Smith";
bob.age = 30;
// this time we have added a method, setAge
bob.setAge = function (newAge){
  bob.age = newAge;
};
// here we set bob's age to 40
bob.setAge(40);
// bob's feeling old.  Use our method to set bob's age to 20

// Notice how we define setAge kind of like we define a property. 
// The big difference is that we put in a function after the equals sign 
// instead of a string or number.

// We call a method like a function, but we use ObjectName.methodName(). 
// Look at where we use the method to change bob's age to 40. 
// We did this by calling bob.setAge(40);.

//// Instructions:

// Try it yourself! Use the method setAge to set bob's age to 20.

bob.setAge(20);


//////////////	A Method to the Madness
////// Lesson 15/33 Why Are Methods Important?

// Methods serve several important purposes when it comes to objects.

// They can be used to change object property values. 
// The method setAge allows us to update bob.age.

// They can be used to make calculations based on object properties. 
// Functions can only use parameters as an input, 
// but methods can make calculations with object properties. 
// For example, we can calculate the year bob was born based on his age 
// with our getYearOfBirth method.

var bob = new Object();
bob.age = 17;
// this time we have added a method, setAge
bob.setAge = function (newAge){
  bob.age = newAge;
};

bob.getYearOfBirth = function () {
  return 2016 - bob.age;
};
console.log(bob.getYearOfBirth());

//// Instructions:

// Click Save & Submit Code to find out what year bob was born in 
// and move onto the next exercise, 
// where we will learn more about how to make methods.


//////////////	A Method to the Madness
////// Lesson 16/33 The "this" Keyword

// Our setAge method works great for bob because it updates bob.age, 
// but what if we want to use it for other people?

// It turns out we can make a method work for many objects using a new keyword, 
// 'this'. 
// The keyword 'this' acts as a placeholder, 
// and will refer to whichever object called that method when the method is actually used.

// Let's look at the method setAge to see how 'this' works. 
// By using the keyword 'this', setAge will change the age property of any object that calls it. 
// Previously, we had a specific object bob instead of the keyword 'this'. 
// But that limited the use of the method to just bob.

// Then when we say bob.setAge = setAge;, 
// it means whenever we type bob.setAge( ), 
// this.age in the setAge method will refer to bob.age.

// here we define our method using "this", before we even introduce bob
var setAge = function (newAge) {
  this.age = newAge;
};
// now we make bob
var bob = new Object();
bob.age = 30;
// and down here we just use the method we already made
bob.setAge = setAge;

//// Instructions:

// To show this way of making setAge works just like the one in exercise 2, 
// use bob's setAge method to change his age to 50.

// change bob's age to 50 here
bob.setAge(50);

//////////////	A Method to the Madness
////// Lesson 17/33 "This" Works for Everyone

// Great! Now we can take advantage of the fact that the method setAge 
// is not limited to a single object bob—
// we can reuse the same method for different objects! 
// This allows us to avoid typing out a custom method each time. 
// All because we used the placeholder 'this'.

// In the editor, we have the same code as last time, 
// where we define setAge using 'this'. 
// We then set bob.setAge = setAge;. 
// But this time we will reuse the setAge method for susan as well.

// here we define our method using "this", before we even introduce bob
var setAge = function (newAge) {
  this.age = newAge;
};
// now we make bob
var bob = new Object();
bob.age = 30;
bob.setAge = setAge;

//// Instructions:

// Make susan who should initially have an age of 25 and a susan.setAge method 
// also equal to setAge.

// Then use susan.setAge(35); to set susan's age to 35.

// make susan here, and first give her an age of 25
var susan = new Object();
susan.age = 25;
susan.setAge = setAge;


// here, update Susan's age to 35 using the method
susan.setAge(35);


//////////////	A Method to the Madness
////// Lesson 18/33 Make Your Own Method

// Let's look at a new example and get practice writing methods.

// Here we have defined an object rectangle. 
// It has two properties, height and width, 
// which represents the height and width of the shape.

// We have written a setHeight method which will update 
// rectangle's height to the given parameter. 
// This is very similar to setAge from our person example.

var rectangle = new Object();
rectangle.height = 3;
rectangle.width = 4;
// here is our method to set the height
rectangle.setHeight = function (newHeight) {
  this.height = newHeight;
};

// Note we have used the keyword 'this'. 
// 'this' is still a placeholder, 
// but in this scenario, 
// 'this' can only ever refer to rectangle because we defined setHeight 
// to be explicitly part of rectangle by defining it as rectangle.setHeight.

//// Instructions:

// Finish the method setWidth. 
// It should take a parameter newWidth. 
// It will change the property width to the given parameter.

// Then use the two methods setHeight and setWidth 
// to change rectangle's height to 6 and width to 8.

// help by finishing this method
rectangle.setWidth = function (newWidth) {
	this.width = newWidth;
};
  
// here change the width to 8 and height to 6 using our new methods
rectangle.setWidth(8);
rectangle.setHeight(6);

//////////////	A Method to the Madness
////// Lesson 19/33 More Kinds of Methods

// Let's look at another method that calculates useful information about an object.

// Here we have an object 'square' with a sideLength property to represent the length 
// of the square's side. This time, we have added a new method, calcPerimeter, 
// which computes the perimeter of the square. 
// Notice we make use of the keyword 'return' (in the same way we use it in functions!).

var square = new Object();
square.sideLength = 6;
square.calcPerimeter = function() {
  return this.sideLength * 4;
};

//// Instructions:

// Add another method called calcArea, 
// which returns the area of square in terms of sideLength. 
// Use the calcPerimeter function as a guide.

// help us define an area method here

square.calcArea = function() {
	return this.sideLength * this.sideLength;
};

var p = square.calcPerimeter();
var a = square.calcArea();

console.log(p)
console.log(a)

//////////////	Construction Junction
////// Lesson 20/33 The Object Constructor

// We mentioned the term constructor back in section one, 
// when we talked about making an object using the keyword new. 
// A constructor is a way to create an object.

// When we write bob = new Object( ); we are using a built-in constructor called Object. 
// This constructor is already defined by the JavaScript language 
// and just makes an object with no properties or methods.

// This means we have to add our properties one at a time, 
// just like we've been doing. 
// To review,
// we've created bob using the constructor and defined the name property for you.

// here we make bob using the Object constructor
var bob = new Object();
bob.name = "Bob Smith";

//// Instructions:

// Finish making bob by defining the age property and setting it equal to 20

// add bob's age here and set it equal to 20
bob.age = 20;


//////////////	Construction Junction
////// Lesson 21/33 Custom Constructors

// But this approach of adding in properties one at a time for every object is tedious! 
// Instead of always using the boring Object constructor, we can make our own constructors.

// This way we can set the properties for an object right when it is created. 
// So instead of using the Object constructor which is empty and has no properties, 
// we can make our own constructors which have properties.

// To see how this works, look at our Person constructor. 
// This constructor is used to make Person objects. 
// Notice it uses the keyword this to define the name and age properties 
// and set them equal to the parameters given.

function Person(name,age) {
  this.name = name;
  this.age = age;
}

// Let's make bob and susan again, using our constructor
var bob = new Person("Bob Smith", 30);
var susan = new Person("Susan Jordan", 25);

// Now we can use this constructor to make our good friends 
// bob and susan in only one line each! 
// Once we have the constructor, it's way easier to make people 
// because we can include their name and age as arguments 
// to their respective constructors.

//// Instructions:

// Practice using the constructor to make a new Person called george, 
// whose full name is "George Washington" and age is 275.

var george = new Person("George Washington", 275);


//////////////	Construction Junction
////// Lesson 22/33 Try it Out!

// Let's look at another example and practice coding constructors. 
// Here we have made a Cat constructor for you, with age and color properties.

// Why is this Cat constructor so cool? 
// It means if we have many cats and wanted to create an object for each cat, 
// we could just use this constructor with the properties already defined.

// This is much better than using the Object constructor 
// which just gives us an empty object 
// and needs us to define every property 
// and value for each cat object we would create.

function Cat(age, color) {
  this.age = age;
  this.color = color;
}

//// Instructions:

// Finish the Dog constructor we have started. 
// You can include whatever parameters and properties you want 
// (age, name, breed, whatever you can think of!) 
// Use the Cat constructor as an example.

// make a Dog constructor here
function Dog(age, breed, name) {
	this.name = name;
	this.age = age;
	this.breed = breed;
};

//////////////	Construction Junction
////// Lesson 23/33 More Options

// In a constructor, we don't have to define all the properties using parameters. 
// Look at our new Person example, and see how we set the species 
// to be "Homo Sapiens". 
// This means that when we create any Person, their species will be "Homo Sapiens". 
// In this way, the values associated with name and age are not yet assigned, 
// but species will always have the same value.

// In this case, both sally and holden will have the same species of "Homo Sapiens", 
// which makes sense because that is the same across all people.

function Person(name,age) {
  this.name = name;
  this.age = age;
  this.species = "Homo Sapiens";
}

//// Instructions:

// Create a new object called sally using the Person constructor. 
// Her name is "Sally Bowles" and she is 39. 
// Create another object called holden. His name is "Holden Caulfield" and he is 16.

// Edit the sentence printed out such that it includes 
// the age of sally and holden respectively.

var sally = new Person("Sally Bowles", 39);
var holden = new Person("Holden Caulfield", 16);

console.log("sally's species is " + sally.species + " and she is " + sally.age);
console.log("holden's species is " + holden.species + " and he is " + holden.age);


//////////////	Construction Junction
////// Lesson 24/33 Constructors With Methods

// In addition to setting properties, constructors can also define methods. 
// This way, as soon as the object is created it will have its own methods as well.

// Here we have a Rectangle constructor, 
// which sets the height and width properties equal to the arguments, 
// just like our Person did with name and age.

// Notice we have added a calcArea method. 
// This calculates the area of the rectangle in terms of its height and width.

function Rectangle(height, width) {
  this.height = height;
  this.width = width;
  this.calcArea = function() {
      return this.height * this.width;
  };

// the following line creates a new object rex which makes use of the constructor. 
var rex = new Rectangle(7,3);
var area = rex.calcArea();
var perimeter = rex.calcPerimeter();
// You can see how rex calls the calcArea method and saves the result in a variable, area.

//// Instructions:

// Define a new method on line 8, calcPerimeter, 
// which calculates and returns the perimeter for a Rectangle in terms of height and width.
function Rectangle(height, width) {
  this.height = height;
  this.width = width;
  this.calcArea = function() {
      return this.height * this.width;
  };
  // put our perimeter function here!
  this.calcPerimeter = function() {
	return this.height * 2 + this.width * 2;
  };
}

var rex = new Rectangle(7,3);
var area = rex.calcArea();
var perimeter = rex.calcPerimeter();
console.log(perimeter);


//////////////	Construction Junction
////// Lesson 25/33 Constructors in Review

// Constructors are a way to make objects with the keyword new.
// The most basic constructor is the Object constructor, 
// which will make an object with no methods or properties.

// For more complicated objects we can make our own constructors 
// and put in whatever properties and methods we want.

// Check out our example to the right to see objects in action. 
// Our Rabbit constructor defines an adjective property and a describeMyself method.

// Recall how these kind of custom constructors are important 
// because they allow us to easily make many similar objects.

function Rabbit(adjective) {
    this.adjective = adjective;
    this.describeMyself = function() {
        console.log("I am a " + this.adjective + " rabbit");
    };
}

//// Instructions:

// Create a new object rabbit1 with the adjective "fluffy", 
// a new object rabbit2 with the adjective "happy", 
// and a new object rabbit3 with the adjective "sleepy".

// Use the method describeMyself to print out in the console a sentence 
// about each object you just created!

var rabbit1 = new Rabbit("fluffy");
var rabbit2 = new Rabbit("happy");
var rabbit3 = new Rabbit("sleepy");

rabbit1.describeMyself()
rabbit2.describeMyself()
rabbit3.describeMyself()


//////////////	Combining Objects with Our Other Tools
////// Lesson 26/33 Arrays of Objects

// Remember that an object is just another type, 
// like a string or number but more complex. 
// This means that just as we can make arrays of numbers and strings, 
// we can also make arrays of objects.

// Here we have our Person constructor which should look familiar. 
// We can use this constructor to make an array of Person objects, 
// similar to how we might make an array of numbers but filling in people instead.

// Our person constructor
function Person (name, age) {
    this.name = name;
    this.age = age;
}

// Now we can make an array of people
var family = new Array();
family[0] = new Person("alice", 40);
family[1] = new Person("bob", 42);
family[2] = new Person("michelle", 8);
// add the last family member, "timmy", who is 6 years old

//// Instructions:

// Add one more Person to the family array, "timmy", who is 6 years old.

family[3] = new Person("timmy",6);


//////////////	Combining Objects with Our Other Tools
////// Lesson 27/33 Loop the loop

// Arrays filled with objects will work just like arrays filled with numbers and strings.

// In the same way we may loop through an array of numbers to print them out 
// or calculate a sum, we can loop through an array of objects 
// and access properties or methods.

//// Instructions:

// Write a person constructor called Person that has two properties (name and age).
// Create an empty array called family.
// There will be four objects in the array. 
// Using your Person constructor, 
// create the four objects and put them in the array. 
// The order of the objects are:

	// "alice" who is 40
	// "bob" who is 42
	// "michelle" who is 8
	// "timmy" who is 6

// Create a for-loop that loops through the family array 
// and prints out the name property for each family member 
// in order of creation.

// Our Person constructor
function Person (name, age) {
	this.name = name;
	this.age = age;
};

// Now we can make an array of people
var family = new Array();
family[0] = new Person("alice", 40);
family[1] = new Person("bob", 42);
family[2] = new Person("michelle", 8);
family[3] = new Person("timmy", 6);

// loop through our new array
for(var i = 0; i < family.length; i++){
	console.log(family[i]);
};


//////////////	Combining Objects with Our Other Tools
////// Lesson 28/33 Passing Objects into Functions

// In addition to making arrays of Objects, 
// we can use objects as parameters for functions as well. 
// That way, these functions can take advantage of the methods  
// and properties that a certain object type provides.

// To see an example, take a look at the console. 
// In addition to our Person constructor we have introduced a new function, ageDifference. 
// This function takes two Person objects as parameters, 
// and returns the difference in age between the two people.

// Notice we would be in trouble here if we tried to call ageDifference 
// and passed in strings instead of people, because strings don't have an age property. 
// But because we know from our constructor that all Person objects will have an age property, 
// we can pass any Person into ageDifference. 
// We must be careful not to pass anything but Person objects into ageDifference.

// Our person constructor
function Person (name, age) {
    this.name = name;
    this.age = age;
}

// We can make a function which takes persons as arguments
// This one computes the difference in ages between two people
var ageDifference = function(person1, person2) {
    return person1.age - person2.age;
}

var alice = new Person("Alice", 30);
var billy = new Person("Billy", 25);

//// Instructions:

// We have created two example people, alice and billy. 
// Complete line 17 by calling ageDifference 
// and saving the result in our global diff variable.

// get the difference in age between alice and billy using our function
var diff = ageDifference(alice, billy)
console.log(diff)


//////////////	Combining Objects with Our Other Tools
////// Lesson 29/33 Try it Out!

// This time try making your own function that takes objects as parameters!

// Here we have given you the Person constructor again, 
// along with the ageDifference function as an example.

// Now create a new function, olderAge. 
// It should take two Person objects as parameters, 
// and return the age of whatever Person is older. 

// For example, with 30 year-old alice and 25 year-old bob, olderAge(alice, bob); 
// should return 30, because that is alice's age and she is older than bob. 
// If the two people have the same age then you can return that age.

// Our person constructor
function Person (name, age) {
    this.name = name;
    this.age = age;
}

// We can make a function which takes persons as arguments
// This one computes the difference in ages between two people
var ageDifference = function(person1, person2) {
    return person1.age - person2.age;
};

// Make a new function, olderAge, to return the age of
// the older of two people


// Let's bring back alice and billy to test our new function
var alice = new Person("Alice", 30);
var billy = new Person("Billy", 25);

console.log("The older person is " + olderAge(alice, billy));


//// Instructions:

// Define a function called olderAge. 
// We want the function to return the age of the person who is older.

// Our person constructor
function Person (name, age) {
    this.name = name;
    this.age = age;
}

// We can make a function which takes persons as arguments
// This one computes the difference in ages between two people
var ageDifference = function(person1, person2) {
    return person1.age - person2.age;
};

// Make a new function, olderAge, to return the age of
// the older of two people
var olderAge = function(person1, person2) {
	if (person1.age > person2.age) {
		return person1.age;
	} else if (person1.age < person2.age) {
		return person2.age;
	} else {
		return person2.age;
	};
};


// Let's bring back alice and billy to test our new function
var alice = new Person("Alice", 30);
var billy = new Person("Billy", 25);

console.log("The older person is " + olderAge(alice, billy));



//////////////	Objects in Review
////// Lesson 30/33 What Are Objects For?

// Objects provide us with a way to represent real-world or virtual things. 
// We can do this by storing information inside the object's properties. 
// There are two basic ways to make objects:

// Literal Notation, where we use - var Name = { };

// Constructor Notation, where we use the keyword - 'new'.

// We've given an example in literal notation to refresh your memory.

var spencer = {
  age: 22,
  country: "United States"
};

//// Instructions:

// Make a new object, spencer2, with the same properties 
// but using constructor notation and the Object constructor.

var spencer2 = new Object();
spencer2.age = 22;
spencer2["country"] = "United States";


//////////////	Objects in Review
////// Lesson 31/33 Properties

// Properties are like variables that belong to an object, 
// and are used to hold pieces of information. 

// Properties can be accessed in two ways:
	// Dot notation, with ObjectName.PropertyName
	// Bracket notation, with ObjectName["PropertyName"] (don't forget the quotes!)

// In the editor, we have brought back our snoopy object, with a species and age property.

//// Instructions:

// Set the global variable species to be snoopy's species 
// and the variable age to be snoopy's age. 
// For one use dot notation and the other use bracket notation!

var snoopy = new Object();
snoopy.species = "beagle";
snoopy.age = 10;

// save Snoopy's age and species into variables
// use dot notation for snoopy's species
var species = snoopy.species
    
// use bracket notation for snoopy's age
var age = snoopy["age"]



//////////////	Objects in Review
////// Lesson 32/33 Customizing Constructors

// In addition to the basic Object constructor, 
// we can define our own custom constructors. 

// These are helpful for two reasons:
	// 1. We can assign our objects properties through parameters 
		// we pass in when the object is created.
	// 2. We can give our objects methods automatically.

// These both work to save us time and lines of code when we make objects.

//// Instructions:

// Notice that without the constructor, it takes us 3 lines of code to make harry_potter, 
// an object that represents Harry Potter book 1.

// Then in line 7 we introduce a constructor for a Book object, 
// where we pass in the pages and author properties as parameters.

// Use this constructor to make the_hobbit, a book with 320 pages by "J.R.R. Tolkien". 
// Notice by using the constructor you can do this in only one line instead of three!

// 3 lines required to make harry_potter
var harry_potter = new Object();
harry_potter.pages = 350;
harry_potter.author = "J.K. Rowling";

// A custom constructor for book
function Book (pages, author) {
    this.pages = pages;
    this.author = author;
}

// Use our new constructor to make the_hobbit in one line
var the_hobbit = new Book(320, "J.R.R. Tolkien")


//////////////	Objects in Review
////// Lesson 33/33 Methods

// Methods are like functions that are associated with a particular object.

// They are especially helpful when you want to either:
	// Update the object properties
	// Calculate something based on an object's properties.

// Here, we have included a Circle object, 
// with a radius property representing the circle's radius. 
// We have implemented an area function which calculates the circle's area. 
// Notice we have used Math.PI to get the π value.

//// Instructions:

// Define a method perimeter that calculates the perimeter of a circle.

function Circle (radius) {
    this.radius = radius;
    this.area = function () {
        return Math.PI * this.radius * this.radius;
        
    };
    // define a perimeter method here
    this.perimeter = function () {
    	return 2 * Math.PI * this.radius;
    };
};

var rad_5 = new Circle(5);
console.log(rad_5.perimeter())



///////////////////////////////////
///////////////////////////////////
// Objects II
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to Objects II
//////////////


//////////////	Review: The story so far...
////// Lesson 1/30 An Objective Review

// Let's review the basics of objects covered in our previous lesson on objects. 
// Recall we can create objects using either literal notation or constructor notation.

// Literal notation 
	// creates a single object. 
	// Literal notation uses curly brackets { } 
	// and the object's default properties are defined 
	// within the brackets using property:value notation.

// Constructor notation 
	// involves defining an object constructor. 
	// And like defining a function, we use the function keyword. 
	// You can think of this constructor as a "template" 
	// from which you can create multiple objects. 
	// To create a new object from a constructor, we use the 'new' keyword.

//// Instructions:

// Finish the james object by adding properties to it. 
// His job should be "programmer" and should have a married property set to false.

// Create a new gabby object using the Person constructor. 
// She should have a job of "student" and her married property should be true.


var james = {
    // add properties to this object!
    job: "programmer",
    married: false
};

function Person(job, married) {
    this.job = job;
    this.married = married;
}

// create a "gabby" object using the Person constructor!
gabby = new Person("student", true);


//////////////	Review: The story so far...
////// Lesson 2/30 Fun with Functions

// Recall that we can add methods 
// (i.e., functions associated with objects) to a constructor:

function someObject() {
  this.someMethod = function() {
  };
}

// Suppose we said var someObj = new someObject();. 
// When we call someObj.someMethod(), 
// the code between the curly brackets { } above will run.

//// Instructions:

// Add a speak method to the Person constructor. 
// Whenever speak is called, it should print "Hello!" to the console.

function Person(job, married) {
    this.job = job;
    this.married = married;
    // add a "speak" method to Person!
	this.speak = function() {
		console.log("Hello!");
	}    
}

var user = new Person("Codecademy Student",false);
user.speak();


//////////////	Review: The story so far...
////// Lesson 3/30 Literally Speaking

// In the last exercise, we added methods to objects via constructor notation. 
// We can also add methods to objects in literal notation:

var someObj = {
	aProperty: value,
	someMethod: function(some, params) { }
};

// When we call someObj.someMethod(some, values);, 
// the code between the curly brackets { } will run.

// Note here we see a method that takes parameters. 
// Methods defined in both constructors and literal notation can take parameters, 
// just like normal functions.

//// Instructions:

// Take a look at the partially-defined james object. 
// Complete the speak method such that the last two lines in the editor 
// will cause "Hello, I am feeling great" and "Hello, I am feeling just okay" 
// to be printed to the console.

var james = {
    job: "programmer",
    married: false,
    speak: function(mood) {
        if (mood === "great") {
        	console.log("Hello, I am feeling great");
        } else if (mood === "just okay") {
        	console.log("Hello, I am feeling just okay");
        } else {
        	console.log("not in any mood")
        }
    }
};

james.speak("great");
james.speak("just okay");


//////////////	Review: The story so far...
////// Lesson 4/30 Can I See Your References?

// Remember when defining a method for an object, 
// it's easy to reference other properties in that object: 
// just use this.propertyName!

// When that method is called, this.propertyName will always 
// refer to the most recent value of propertyName.

//// Instructions:

// Take a look at the james object. 
// Complete the sayJob method so that it will print to the console 
// "Hi, I work as a [job]", where [job] is the value of the job property.

// Then in line 14, change the job for james to "super programmer". 
// Although the method calls in lines 11 and 17 are exactly the same, 
// their output should be different because James' job changed!

var james = {
    job: "programmer",
    married: false,
    sayJob: function() {
        // complete this method
        console.log("Hi, I work as a " + this.job);
    }
};

// james' first job
james.sayJob();

// change james' job to "super programmer" here
james.job = "super programmer";

// james' second job
james.sayJob();


//////////////	Review: The story so far...
////// Lesson 4/30 Who's in Your Bracket?

// And finally, let's go over retrieving property values. 
// Throughout this section, we've been using dot notation 
// to get the value of an object's property:
someObj.propName;

// However, remember that we can also use bracket notation:
someObj["propName"];

// An advantage of bracket notation is that we are not restricted 
// to just using strings in the brackets. 
// We can also use variables whose values are property names:
var someObj = {propName: someValue};
var myProperty = "propName";
someObj[myProperty];

// The last line is exactly the same as using someObj["propName"];.

//// Instructions:

// Take advantage of the ability to use variables with bracket notation.

// In line 7, set aProperty to a string of the first property in james 
// (ie. the job property).

// Then print james's job using bracket notation and aProperty.

var james = {
    job: "programmer",
    married: false
};

// set to the first property name of "james"
var aProperty = "job";

// print the value of the first property of "james" 
// using the variable "aProperty"
console.log(james[aProperty]);


//////////////	Objects, Objects Everywhere
////// Lesson 6/30 I.D., Please

// Alright! Let's get our hands dirty and start exploring some really cool stuff 
// about objects in JavaScript. 
// But before we can do that, how can we even tell if something is an object 
// (as opposed to, say, a number or string)?
// It would be great if we could tell what type something is in JavaScript. 
// Good thing there's a handy built-in operator to do this!

// Say we have a variable thing and we don't know what type thing is.
// We can call typeof thing to figure this out. 
// Generally, the most useful types are 
// "number," "string," "function," and of course, "object."

// As an example, the following example will print "object":

var someObject = {someProperty: someValue};
console.log( typeof someObject );

//// Instructions:

// In lines 3-6, we have an object, a number, and a string (in that order). 
// Complete lines 7-9 so they will print the appropriate types of these variables.

// complete these definitions so that they will have
// the appropriate types
var anObj = { job: "I'm an object!" };
var aNumber = 42;
var aString = "I'm a string!";

console.log( typeof anObj ); // should print "object"
console.log( typeof aNumber ); // should print "number"
console.log( typeof aString ); // should print "string"


//////////////	Objects, Objects Everywhere
////// Lesson 7/30 Know Thyself

// In the last exercise, we used typeof to figure out what type a variable in JavaScript is. 
// Since we know how to tell objects apart from everything else now, let's focus on them.

// You wouldn't know it, but every object in JavaScript comes with some baggage 
// (stay tuned for more on this!). 
// Part of this baggage includes a method called hasOwnProperty. 
// This lets us know if an object has a particular property.

var myObj = {
    // finish myObj
    
};

console.log( myObj.hasOwnProperty('name') ); // should print true
console.log( myObj.hasOwnProperty('nickname') ); // should print false

// We show how to use hasOwnProperty in the last two lines. 
// It returns true or false, based on whether an object has a certain property.

//// Instructions:

// You should finish myObj by giving it a name property. 
// Make sure that myObj does not have a nickname property 
// so that the last line will print false.

var myObj = {
    // finish myObj
    name: function() {
        console.log("Printing name:" + "myObj");
    }
    
};

console.log( myObj.hasOwnProperty('name') ); // should print true
console.log( myObj.hasOwnProperty('nickname') ); // should print false


//////////////	Objects, Objects Everywhere
////// Lesson 8/30 Dressed to Impress

// Let's get some practice working with hasOwnProperty. 
// It is an invaluable tool when working with objects!

// Try to run the code in the editor as it is. 
// You should get an error because shorts is not a property of the suitcase object.

// Let's write some code to test for this so we can avoid this nasty error later.

//// Instructions:

// Remove the console.log statement.

// Write an if statement that checks to see if suitcase has the shorts property.

// If your if statement evaluates to true, print the value of the shorts property.

// If your if statement evaluates to false, 
// set the shorts property to any value you wish using dot notation. 
// Then print the value of the shorts property.

var suitcase = {
    shirt: "Hawaiian"
};


if (suitcase.hasOwnProperty("shorts")) {
	console.log(suitcase.shorts);
} else {
	suitcase.shorts = "Surfer";
	console.log(suitcase.shorts);
}


//////////////	Objects, Objects Everywhere
////// Lesson 9/30 Getting IN-timate

// Now let's learn how to work with all the properties that belong to an object. 

// First, let's define an object:

var dog = {
species: "bulldog",
age: 3,
color: brown
};

// To print out all elements, we can use a for/in loop, like this:

for(var property in dog) {
  console.log(property);
}

// In the loop we use console.log to print out each key. 
// Remember the "property" bit can be any placeholder name you like.

var nyc = {
    fullName: "New York City",
    mayor: "Bill de Blasio",
    population: 8000000,
    boroughs: 5
};


//// Instructions:

// Use a for-in loop to print out all the properties of nyc.

for(var stuff in nyc) {
	console.log(stuff);
}



//////////////	Objects, Objects Everywhere
////// Lesson 10/30 List ALL the Properties!

// We've just seen how to print all of an object's property names with a for-in loop. 
// But how do we print out all the values associated with every property? Surprise! 
// The for-in loop will be our friend again! 
// Let's get there slowly.
//  Our dog object can help us.

var dog = {
	species: "bulldog",
	age: 3,
	color: brown
};

// First, remember that
dog.species = dog["species"] = "bulldog";

// And if we say:
var x = "species";

// then
dog[x] = "bulldog";

// We see that by assigning the property name to a variable, 
// we can then use the variable name in bracket notation 
// to get the property's value. 
// So to get all the values from the dog object, 
// we would use the for-in loop and the bracket notation we just saw above. 
// See the hint to see the code to print the property values for dog.

var nyc = {
    fullName: "New York City",
    mayor: "Bill de Blasio",
    population: 8000000,
    boroughs: 5
};


//// Instructions:

// Write another for-in loop,
// but this time print the value of each property in nyc.

for (var property in nyc) {
	console.log(nyc[property]);
}


//////////////	You down with OOP?
////// Lesson 11/30 Class is in Session

// Alright, it's time to learn the basics of object-oriented programming! 
// Often abbreviated OOP, 
// this is a very important programming paradigm that is widely used in the industry today.

// Let's start by introducing classes. 
// We learned in the last course that constructors are a way to make objects, 
// but they actually do even more than that.

// When you make a constructor, you are in fact defining a new class. 
// A class can be thought of as a type, or a category of objects—kind of like how Number 
// and String are types in JavaScript.

// Take a look at our Person example taken from Introduction to Objects I. 
// In this case bob and susan are two separate objects, 
// but both belong to the class Person.

function Person(name,age) {
  this.name = name;
  this.age = age;
}

// Let's make bob again, using our constructor
var bob = new Person("Bob Smith", 30);
var susan = new Person("Susan Jordan", 35);

//// Instructions:

// Make your own class, Circle, by building a constructor for it. 
// The constructor for Circle should have one property, radius, 
// and take one argument for the initial radius.

// make your own class here
function Circle(radius) {
	this.radius = radius;
}


//////////////	You down with OOP?
////// Lesson 12/30 Teach Snoopy

// So we know that a class will have certain properties and methods, 
// but what keeps track of what a given class can or can't do? 
// What a class has or doesn't have? That is the job of the prototype.

// JavaScript automatically defines the prototype for class with a constructor. 
// For example, our Dog constructor ensures that the Dog prototype has a breed property. 
// Remember, the Dog prototype keeps track of what Dog has, doesn't have, can, or can't do.

// We know we can add methods to objects, and in line 7 we add the bark method to buddy. 
// Hit run and you will see one "Woof" printed when buddy barks. 
// Notice what happens when we try to get snoopy to bark in line 17 though. 
// Even though snoopy is of the class Dog, he doesn't know how to bark 
// because only buddy had bark added as a method.

function Dog (breed) {
  this.breed = breed;
}

// here we make buddy and teach him how to bark
var buddy = new Dog("Golden Retriever");
buddy.bark = function() {
  console.log("Woof");
};
buddy.bark();

// here we make snoopy
var snoopy = new Dog("Beagle");
// we need you to teach snoopy how to bark here

// this causes an error, because snoopy doesn't know how to bark!
snoopy.bark();

//// Instructions:

// To fix this, start at line 15 add a bark method for the snoopy object. 
// You can make it just like the bark method for buddy, 
// or type in whatever barking noise you want instead of "Woof".


snoopy.bark = function() {
	console.log("woorf");
};



//////////////	You down with OOP?
////// Lesson 13/30 How do Classes Help Us?

// Classes are very important in object-oriented programming. 
// This is because a class tells us helpful information about objects, 
// and you can think of an object as a particular instance of a class.

// For example, look at our Person class again in the console. 
// We know that any Person will have a name and age, 
// because they are in the constructor. 

// This allows us to create a function like printPersonName, 
// which will take a Person as an argument and print out their name. 
// We know the function will work on any Person, 
// because name is a valid property for that class.

function Person(name,age) {
  this.name = name;
  this.age = age;
}
// a function that prints the name of any given person
var printPersonName = function (p) {
  console.log(p.name);
};

var bob = new Person("Bob Smith", 30);
printPersonName(bob);

//// Instructions:

// Make a Person called me with your own name and age, 
// and print your name using printPersonName.

var me = new Person("CA", 28);
printPersonName(me);


//////////////	You down with OOP?
////// Lesson 14/30 Prototype to the Rescue

// Here we have very similar code as last time, 
// but there is an important difference. 
// Instead of using buddy.bark to add the bark method to just the buddy object, 
// we use Dog.prototype.bark.

// Click run this time, and both buddy and snoopy can bark just fine! 
// Snoopy can bark too even though we haven't added a bark method to that object. 
// How is this so? Because we have now changed the prototype for the class Dog. 
// This immediately teaches all Dogs the new method.

// In general, if you want to add a method to a class 
// such that all members of the class can use it, 
// we use the following syntax to extend the prototype:

className.prototype.newMethod =

function() {
statements;
};


// code:
function Dog (breed) {
  this.breed = breed;
};

// here we make buddy and teach him how to bark
var buddy = new Dog("golden Retriever");
Dog.prototype.bark = function() {
  console.log("Woof");
};
buddy.bark();

// here we make snoopy
var snoopy = new Dog("Beagle");
/// this time it works!
snoopy.bark();

//// Instructions:

// Click Save & Submit Code to move onto the next exercise, 
// for practice manipulating prototypes.


//////////////	You down with OOP?
////// Lesson 15/30 Prototype Practice

// Here we have created a new class, Cat, and its constructor. 
// We also have two cats that would like to meow, but currently Cats have no meow method.

//// Instructions:

// Add a meow method to the Cat prototype so that all cats can now meow. 
// This method should print to the console "Meow!". 
// Then call this method for each cat.

function Cat(name, breed) {
    this.name = name;
    this.breed = breed;
}

// let's make some cats!
var cheshire = new Cat("Cheshire Cat", "British Shorthair");
var gary = new Cat("Gary", "Domestic Shorthair");

// add a method "meow" to the Cat class that will allow
// all cats to print "Meow!" to the console
Cat.prototype.meow = function() {
  console.log("Meow!");
};

// add code here to make the cats meow!
cheshire.meow();
gary.meow();

function Cat(name, breed) {
    this.name = name;
    this.breed = breed;
    this.meow = "Meow!"
}


//////////////	Inheriting a Fortune
////// Lesson 16/30 It's All in the Genes

// In object-oriented programming, 
// inheritance allows one class to see and use the methods and properties of another class. 

// You can think of it as a child being able to use his or her parent's money 
// because the child inherits the money.

// We will learn more about inheritance as we continue this lesson, 
// but for now let's just refresh our memories about how classes and objects work.

//// Instructions:

// Create a class named Animal with two properties, name and numLegs. 
// The Animal constructor should have two arguments 
// whose values are assigned to name and numLegs.

// Next, change the prototype of Animal
// and add a method sayName that prints to the console "Hi my name is [name]",
// where [name] is the value of name.

// Click "Stuck? Get a hint!" for examples of how to create a class 
// and how to add a method to an object's prototype.

// Finally, we have provided the last two lines to test your constructor and sayName method.
// Don't change these!


// create your Animal class here
function Animal(name, numLegs){
	this.name = name;
	this.numLegs = numLegs;
}

// create the sayName method for Animal
Animal.prototype.sayName = function() {
	console.log("Hi my name is " + this.name);
}


// provided code to test above constructor and method
var penguin = new Animal("Captain Cook", 2);
penguin.sayName();


//////////////	Inheriting a Fortune
////// Lesson 17/30 Marching Penguins

// Let's say we're dealing with a lot of Penguins. 
// It sure would be nice to create a Penguin class so that perhaps later 
// we can give it some methods unique to a penguin 
// and not confuse it with the Animal class.

//// Instructions:

// Create a brand new Penguin class constructor starting in line 11. 
// A penguin is an animal so it should also have the name and numLegs properties 
// as well as a sayName method that prints the same thing as Animal's sayName method.

// We're not done with animals yet, 
// so we have still included the Animal constructor and its sayName method. 
// The last two lines test your Penguin code.

 
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
}
Animal.prototype.sayName = function() {
    console.log("Hi my name is " + this.name);
};


// create a Penguin constructor here
function Penguin(name, numLegs) {
	this.name = name;
	this.numLegs = numLegs;
}

// create a sayName method for Penguins here
Penguin.prototype.sayName = function () {
	console.log("Hi my name is " + this.name);
}

// our test code
var theCaptain = new Penguin("Captain Cook", 2);
theCaptain.sayName();


//////////////	Inheriting a Fortune
////// Lesson 18/30 DRY Penguins

// Creating a brand new Penguin was nice, 
// but we did end up reusing a lot of the same code as the Animal class. 
// This goes against the "DRY" principle of programming: Don't Repeat Yourself.

// Inheritance can help us here! 
// A Penguin is an Animal, so they should have all the same properties and methods as Animal. 
// Whenever this X is-a Y relationship exists, 
// there's a good chance that we should be using inheritance.

// Remember, inheritance lets us see and use properties 
// and methods from another class. 
// To say that Penguin inherits from Animal, 
// we need to set Penguin's prototype to be Animal.

//// Instructions:

// Create a new Penguin class. 
// The Penguin constructor can be more unique than the generic Animal one 
// because all penguins have 2 legs. 
// Your constructor should only take a name parameter, 
// and within the constructor itself, set this.numLegs to 2.

// Set the Penguin class's prototype to a new instance of Animal 
// by adding this line after you make the constructor:

Penguin.prototype = new Animal();

// This means that Penguin inherits properties and methods from Animal.

// the original Animal class and sayName method
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
}
Animal.prototype.sayName = function() {
    console.log("Hi my name is " + this.name);
};

// define a Penguin class
function Penguin(name) {
    this.name = name;
	this.numLegs = 2;
}

// set its prototype to be a new instance of Animal
Penguin.prototype = new Animal();


//////////////	Inheriting a Fortune
////// Lesson 19/30 Black (and White) Penguin Magic

// Now for some black magic and to see the power of inheritance!

// We never defined a sayName method for Penguin, 
// but what happens when we try to call it?

//// Instructions:

// Create a Penguin object with the variable name penguin 
// and any name you'd like.

// Then call penguin.sayName();.

// Then be amazed.

// the original Animal class and sayName method
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
}
Animal.prototype.sayName = function() {
    console.log("Hi my name is " + this.name);
};

// define a Penguin class
function Penguin(name) {
    this.name = name;
	this.numLegs = 2;
}

// set its prototype to be a new instance of Animal
Penguin.prototype = new Animal();

// create penguin object and call sayName.
var penguin = new Penguin("igo");
penguin.sayName();



//////////////	Inheriting a Fortune
////// Lesson 20/30 Penguins, Properties, and the Prototype

// We saw in the last exercise how Penguin inherited 
// the sayName method from Animal. 

// We now explore how classes can inherit properties as well.

// For simplicity, we've defined a new Penguin class 
// that doesn't inherit anything from Animal.

//// Instructions:

// Create an Emperor class that takes a single name parameter 
// and sets its name property to be this value. 
// Don't set a numLegs property in the constructor.

// Similar to what we did in the previous exercise, 
// make Emperor inherit from Penguin 
// by setting the prototype of Emperor to be Penguin.

// Create a new emperor object that is an instance of the Emperor class 
// with any name you'd like. 
// Then use console.log to print the number of legs emperor has—
// this should have been inherited from Penguin!


function Penguin(name) {
    this.name = name;
    this.numLegs = 2;
}

// create your Emperor class here and make it inherit from Penguin
function Emperor(name) {
	this.name = name;
}
Emperor.prototype = new Penguin();


// create an "emperor" object and print the number of legs it has

var emperor = new Emperor("igo2");
console.log(emperor.numLegs);


//////////////	Inheriting a Fortune
////// Lesson 21/30 Up the Food-I-mean-Prototype Chain

// A penguin is an animal and an emperor penguin is a penguin.
// Are emperor penguins animals too? Of course!

// The "prototype chain" in JavaScript knows this as well. 
// If JavaScript encounters something it can't find in 
// the current class's methods or properties, 
// it looks up the prototype chain to see if it's defined 
// in a class that it inherits from. 

// This keeps going upwards until it stops all the way at the top: 
// the mighty Object.prototype (more on this later). 
// By default, all classes inherit directly from Object, 
// unless we change the class's prototype, 
// like we've been doing for Penguin and Emperor.

//// Instructions:

// Let's see how going up the prototype chain works! 
// We've defined some classes and inheritance patterns: 
// Emperor inherits from Penguin which inherits from Animal.
// We've also created an instance of the Emperor class.

// Without modifying anything other than lines 22-24, 
// complete the console.log statements to print the appropriate responses.

// Remember how the prototype chain works: 
// if a property is not defined for a class, 
// this class's prototype chain will be traversed upwards until one is found 
// (or not) in a parent (higher) class.


// original classes
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
    this.isAlive = true;
}
function Penguin(name) {
    this.name = name;
    this.numLegs = 2;
}
function Emperor(name) {
    this.name = name;
    this.saying = "Waddle waddle";
}

// set up the prototype chain
Penguin.prototype = new Animal();
Emperor.prototype = new Penguin();

var myEmperor = new Emperor("Jules");

console.log( myEmperor.saying ); // should print "Waddle waddle"
console.log( myEmperor.numLegs ); // should print 2
console.log( myEmperor.isAlive ); // should print true


//////////////	Privacy Please!
////// Lesson 22/30 Open to the Public

// In JavaScript all properties of an object are automatically public. 
// Public means that they can be accessed outside the class. 
// Think of these properties as the information a class is willing to share.

// Look at the Person class. 
// It has 3 public properties: firstName, lastName, and age. 
// On lines 8 and 9, we access the firstName and lastName properties of john 
// and assign them to myFirst and myLast.

function Person(first,last,age) {
   this.firstName = first;
   this.lastName = last;
   this.age = age;
}

var john = new Person('John','Smith',30);
var myFirst = john.firstName;
var myLast = john.lastName;

//// Instructions:

// Declare a third variable called myAge 
// and use it to store the age property of the john object.

var myAge = john.age;


//////////////	Privacy Please!
////// Lesson 23/30 Private Variables

// Good! 
// But what if an object wants to keep some information hidden?

// Just as functions can have local variables
// which can only be accessed from within that function, 
// objects can have private variables. 

// Private variables are pieces of information you 
// do not want to publicly share, 
// and they can only be directly accessed from within the class.

// The Person class has been modified to have a private variable 
// called bankBalance. 
// Notice that it looks just like a normal variable, 
// but it is defined inside the constructor for Person without using 'this', 
// but instead using 'var'. 
// This makes bankBalance a private variable.

//// Instructions:

// Create an object john using the Person constructor. 
// He can have any name and age you wish.

// Next, try to print his bankBalance. What happens?

function Person(first,last,age) {
   this.firstname = first;
   this.lastname = last;
   this.age = age;
   var bankBalance = 7500;
}

// create your Person 
var john = new Person("john","smith",16)

// try to print his bankBalance
console.log(john.age);
console.log(john.bankbalance);

//	prints > undefined



//////////////	Privacy Please!
////// Lesson 24/30 Accessing Private Variables

// Although we cannot directly access private variables from outside the class, 
// there is a way to get around this. 
// We can define a public method that returns the value of a private variable.

//// Instructions:

// Here we have included similar code from last time, 
// but here we have added a method getBalance. 
// Modify getBalance so that it returns bankBalance.

// Then on line 17, create a new variable named myBalance 
// and set its value to John's bank balance. 
// You can do this by calling your newly-defined getBalance method for john. 
// Then print myBalance.

// Line 14 should still print undefined!

function Person(first,last,age) {
   this.firstname = first;
   this.lastname = last;
   this.age = age;
   var bankBalance = 7500;
  
   this.getBalance = function() {
      // your code should return the bankBalance
      return bankBalance;
   };
}

var john = new Person('John','Smith',30);
console.log(john.bankBalance);

// create a new variable myBalance that calls getBalance()

var myBalance = john.getBalance();
console.log(myBalance);


//////////////	Privacy Please!
////// Lesson 25/30 Private Methods

// Why did that code work?
// An object's private variables can only be accessed by other 
// methods that are part of that same object. 
// So, we just used an object's public method to access a private variable!

// Methods can also be private within a class and inaccessible outside of the class. 
// Changing this.returnBalance from the last exercise to var returnBalance 
// makes this method private. 
// If you run the program trying to access the method you get an undefined error this time.

// The way to access a private method is similar to accessing a private variable. 
// You must create a public method for the class that returns the private method.

//// Instructions:

// Create a method called askTeller within the Person class 
// that returns the returnBalance method. 
// This means that it returns the method itself and NOT the result of calling that method. 
// So you should NOT have parentheses after returnBalance.

// Because askTeller returns a method, we need to call it to make it any use. 
// This is what var myBalance = myBalanceMethod(); does.

function Person(first,last,age) {
   this.firstname = first;
   this.lastname = last;
   this.age = age;
   var bankBalance = 7500;
  
   var returnBalance = function() {
      return bankBalance;
   };
       
   // create the new function here
   this.askTeller = function() {
   		return returnBalance;
   };
}

var john = new Person('John','Smith',30);
console.log(john.returnBalance);
var myBalanceMethod = john.askTeller();
var myBalance = myBalanceMethod();
console.log(myBalance);


//////////////	Privacy Please!
////// Lesson 26/30 Passing Arguments

// The askTeller function has been modified within the Person class 
// to directly give you your balance. 
// However, it now needs the account password in order to return the bankBalance.

//// Instructions:

// Create a new variable called myBalance that calls the askTeller function 
// with a password argument, 1234.

function Person(first,last,age) {
   this.firstname = first;
   this.lastname = last;
   this.age = age;
   var bankBalance = 7500;
  
   this.askTeller = function(pass) {
     if (pass == 1234) return bankBalance;
     else return "Wrong password.";
   };
}

var john = new Person('John','Smith',30);
/* the variable myBalance should access askTeller()
   with a password as an argument  */
john.askTeller(1234);


//////////////	Objects in Review Are Closer Than They Appear
////// Lesson 27/30 Looks For-In To Me

// Objects aren't so foreign if you really think about it!

// Remember you can figure out the type of a variable 
// by using typeof myVariable;. 
// Types we are concerned with for now are "object", "string", and "number".

// Recall the for-in loop:

for(var x in obj) {
executeSomething();
}

// This will go through all the properties of obj one by one 
// and assign the property name to x on each run of the loop.

// Let's combine our knowledge of these two concepts.

var languages = {
    english: "Hello!",
    french: "Bonjour!",
    notALanguage: 4,
    spanish: "Hola!"
};

// print hello in the 3 different languages


//// Instructions:

// Examine the languages object. 
// Three properties are strings, whereas one is a number.

// Use a for-in loop to print out the three ways to say hello. 
// In the loop, you should check to see if the property value 
// is a string so you don't accidentally print a number.

for (var key in languages) {
	var value = languages[key];
	if (typeof value === "string") {
		console.log(value);
	};
};


//////////////	Objects in Review Are Closer Than They Appear
////// Lesson 28/30 Hello? Yes, This is Dog

// We should all know by now what's so cool about 
// using prototype: we can define a method for a class, 
// and any instance of the class 
// (i.e., object created using that class's constructor) 
// can use that method.

// Remember that classes and the prototype are important to OOP!


//// Instructions:

// Add the sayHello method to the Dog class by extending its prototype.

// sayHello should print to the console: 
// "Hello this is a [breed] dog"
// , where [breed] is the dog's breed.

function Dog (breed) {
    this.breed = breed;
};

// add the sayHello method to the Dog class 
// so all dogs now can say hello

Dog.prototype.sayHello = function() {
	console.log("Hello this is a " + this.breed + " dog");
}


var yourDog = new Dog("golden retriever");
yourDog.sayHello();

var myDog = new Dog("dachshund");
myDog.sayHello();




//////////////	Objects in Review Are Closer Than They Appear
////// Lesson 29/30 So Meta I Can't Take It!

// Do you remember how we said every JavaScript object 
// has some baggage associated with it? 
// Part of this baggage was the hasOwnProperty 
// method available to all objects. 
// Now let's see where this came from...

// If we have just a plain object 
// (i.e., not created from a class constructor), 
// recall that it automatically inherits from Object.prototype. 
// Could this be where we get hasOwnProperty from? How can we check?


//// Instructions:

// Let's first see what type Object.prototype is. 
// Do this in line 2 and save it into prototypeType.

// If all goes well, you should realize that Object.prototype itself is an object! 
// And since all objects have the hasOwnProperty method, 
// it's pretty easy to check if hasOwnProperty comes from Object.prototype. 
// Do this in line 6 and the result may be surprising.

// what is this "Object.prototype" anyway...?
var prototypeType = typeof Object.prototype
console.log(prototypeType);

// now let's examine it!
var hasOwn = Object.prototype.hasOwnProperty("hasOwnProperty");
console.log(hasOwn);



//////////////	Objects in Review Are Closer Than They Appear
////// Lesson 29/30 Private Eye

// Recall that:

// Public properties can be accessed from outside the class
// Private properties can only be accessed from within the class

// Using constructor notation, a property declared as 
this.property = "someValue;" 
// will be public, 
// whereas a property declared with 
var property = "hiddenValue;" 
// will be private.

// In this exercise, hit run and you'll see that all your grades are exposed! 
// You really just want people to know your overall GPA.

//// Instructions:

// Modify the StudentReport class so that no grades will be printed 
// to the console in the for-in loop.

// However, getGPA should still function properly in the last line.

function StudentReport() {
    this.grade1 = 4;
    this.grade2 = 2;
    this.grade3 = 1;
    this.getGPA = function() {
        return (this.grade1 + this.grade2 + this.grade3) / 3;
    };
}

var myStudentReport = new StudentReport();

for(var x in myStudentReport) {
    if(typeof myStudentReport[x] !== "function") {
        console.log("Muahaha! " + myStudentReport[x]);
    }
}

console.log("Your overall GPA is " + myStudentReport.getGPA());


// to:

function StudentReport() {
    var grade1 = 4;
    var grade2 = 2;
    var grade3 = 1;
    this.getGPA = function() {
        return (grade1 + grade2 + grade3) / 3;
    };
}






///////////////////////////////////
///////////////////////////////////
// Objects II
///////////////////////////////////
///////////////////////////////////


//////////////
// Introduction to Objects II
//////////////


//////////////	Review: The story so far...
////// Lesson 1/30 An Objective Review










