// Guide

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






//////////////////////////////////////
// JavaScript  
// https://www.codecademy.com/learn/javascript
//////////////////////////////////////


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
////// Lesson 7/28 What am I learning?



//// Instructions:


//////////////
////// Lesson 7/28 What am I learning?

//////////////
////// Lesson 7/28 What am I learning?

//////////////
////// Lesson 7/28 What am I learning?

//////////////
////// Lesson 7/28 What am I learning?

//////////////
////// Lesson 7/28 What am I learning?

//////////////
////// Lesson 7/28 What am I learning?


