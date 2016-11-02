// Guide

///////////////////////////
//        Codecademy
///////////////////////////


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



//////////////
////// Lesson 2/7 Functions

//////////////
////// Lesson 3/7 Parameters

//////////////
////// Lesson 4/7 Parameters II

//////////////
////// Lesson 5/7 return

//////////////
////// Lesson 6/7 return II

//////////////
////// Lesson 1/7 Review Functions

