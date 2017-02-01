// Guide_AngularJS.js


///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////

//// Learn AngularJS 1.X
// Take your understanding of HTML, CSS, and JavaScript 
// and apply them in learning how to build single-page 
// web applications with this popular JavaScript framework. 
// You'll be introduced to the Model-View-Controller 
// (MVC) programming pattern and get a chance to build 
// your own application from scratch by the end.

///////////////////////////////////
///////////////////////////////////
// Your First App
///////////////////////////////////
///////////////////////////////////


//////////////
// Exercises
//////////////

//////////////
////// Lesson 1/11 Hello AngularJS I

// AngularJS is a JavaScript web framework aimed to make web apps 
// simple to build and easy to maintain.

// We'll start by building a simple AngularJS app. 
// After making this app, we'll generalize a few steps 
// that can be used to build more complex apps. 
// By the end of this course, you'll be able to use this 
// sequence of steps to jumpstart your own AngularJS apps.

//// Instructions:

//// 1.
// Let's get started by making a simple AngularJS app.
// We'll explain each step in the next exercise.

// In app.js, type in the contents exactly as you see here:

var app = angular.module("myApp", []);


//// 2.
// Open up index.html. 
// Modify the <body> tag so it looks like this:

	// <body ng-app="myApp">


//// 3.
// Open up js/controllers/MainController.js. 
// Type in the contents exactly as you see here:

app.controller('MainController', ['$scope', function($scope) { 
  $scope.title = 'Top Sellers in Books'; 
}]);


//// 4.
// Go to index.html. 
// Modify the <div class="main"> tag so it looks like this:

	// <div class="main" ng-controller="MainController">


//// 5.
// In index.html inside <div class="main">, 
// modify the <h1> element so it looks like this:

	// <h1>{{ title }}</h1>

// View the AngularJS app in the browser 
// by visiting http://localhost:8000. 
// The "Top Sellers in Books" content appears as the heading of the page.


//////////////
////// Lesson 2/11 Hello AngularJS II

// Awesome! You built an AngularJS app. How does it work?

// In app.js, we created a new module named myApp. 
// A module contains the different components of an AngularJS app.

// Then, in index.html we added <body ng-app="myApp">. 
// The ng-app is called a directive. 
// It tells AngularJS that the myApp module will live within the <body> element, 
// termed the application's scope. 
// In other words, we used the ng-app directive to define the application scope.

// In MainController.js we created a new controller named MainController. 
// A controller manages the app's data. 
// Here we use the property title to store a string, and attach it to $scope.

// Then, in index.html, we added <div class="main" ng-controller="MainController">. 
// Like ng-app, ng-controller is a directive that defines the controller scope. 
// This means that properties attached to $scope in MainController 
// become available to use within <div class="main">.

// Inside <div class="main"> we accessed $scope.title using {{ title }}. 
// This is called an expression. 
// Expressions are used to display values on the page.

// The value of title showed up when we viewed the app in the browser.


//// Instructions:

//// 1.
// Both the controller MainController and the view index.html have access to $scope. 
// This means we can use $scope to communicate between the controller and the view. 
// In the controller, change the value of title to your own string.

app.controller('MainController',['$scope',function($scope) {
  $scope.title = 'MyTitle';
}]);

//// 2.
// Likewise, any new properties attached to $scope will become available 
// to use in the view. 
// In the controller, attach promo to $scope, and set its value to your own string.



//////////////
////// Lesson 3/11 Workflow

// So far this is our typical workflow when making an AngularJS app:

// Create a module, and use ng-app in the view to define the application scope.

// Create a controller, and use ng-controller in the view to define the controller scope.

// Add data to $scope in the controller so they can be displayed with expressions in the view.


//// Instructions:

//// 1.
// Let's add more data to the controller and display them in the view. 
// In the controller, attach another property to $scope named product. 
// Set it equal to an object with the following properties:

{ 
  name: 'The Book of Trees', 
  price: 19 
}

//// 2.
// Then, in index.html inside <p class="title">, 
// access the product's name with product.name and display it using an expression.

            // <p class="title"> {{ product.name }} </p>

//// 3.
In <p class="price">, access and display the product's price.


//////////////
////// Lesson 4/11 Filters I

// Well done! 
// In the controller, you used an object to group together related data about a product. 
// Then in the view, you used dot notation to display the values.

//// Instructions:

//// 1.
// Currently the product price shows up as a number. 
// It would be better to format it as a currency. 
// Rather than change the data in the controller, 
// let's use an AngularJS filter to format the data in the view.

// In index.html in <p class="price">, change the expression to look like this:

	// {{ product.price | currency }}

// We'll explain how this works in the next exercise.


//////////////
////// Lesson 5/11 Filters II

// Great! The product price changed from a number to a formatted currency. 
// How does it work?

// AngularJS gets the value of product.price.
// It sends this number into the currency filter. 
// The pipe symbol (|) takes the output on the left and "pipes" it to the right.
// The filter outputs a formatted currency with the dollar sign 
// and the correct decimal places.

// In this way, filters help to separate the content in the controller 
// from its presentation in the view.

//// Instructions:

//// 1.
// AngularJS comes with a few more built-in filters. Let's use two more.
// In MainController.js inside $scope.product, add a third property named pubdate:

// pubdate: new Date('2014', '03', '08')

//// 2.
// In index.html inside <p class="date">, display the product's pubdate.

//// 3.
// Format the product's pubdate by piping it to the date filter.

//// 4.
// Format the product's name by piping it to the uppercase filter.

//// MainController:
// app.controller('MainController',['$scope',function($scope) {
//   $scope.title = 'MyTitle';
//   $scope.promo = '2-4-1 Deal';
//   $scope.product = { 
// 	  name: 'The Book of Trees', 
// 	  price: 19,
// 	  pubdate: new Date('2014', '03', '08')
// 	};
// }]);


//// index.html:
//    <div class="main" ng-controller="MainController">
//      <div class="container">
//
//        <h1>{{ title }}</h1>
//        <h2>{{ promo }}</h2>
//
//        <div class="col-md-6">
//          <div class="thumbnail">
//            <img src="img/the-book-of-trees.jpg">
//            <p class="title"> {{ product.name | uppercase }} </p>
//            <p class="price"> {{ product.price | currency }} </p>
//            <p class="date"> {{ product.pubdate | date }} </p>
//          </div>
//        </div>
//
//      </div>
//    </div>


//////////////
////// Lesson 6/11 ng-repeat I

// Let's do a quick review:

// A module contains the different components of an AngularJS app
// A controller manages the app's data
// An expression displays values on the page
// A filter formats the value of an expression

//// Instructions:

//// 1.
// Let's add more data to the controller and display them in the view.

// In the controller, delete the $scope.product object.

//// 2.
// Attach a new property to $scope named products. 
// Set it equal to an array of objects. 
// Type in the contents exactly as you see here:

[ 
  { 
    name: 'The Book of Trees', 
    price: 19, 
    pubdate: new Date('2014', '03', '08'), 
    cover: 'img/the-book-of-trees.jpg' 
  }, 
  { 
    name: 'Program or be Programmed', 
    price: 8, 
    pubdate: new Date('2013', '08', '01'), 
    cover: 'img/program-or-be-programmed.jpg' 
  } 
]

//// 3.
// In the view inside <div class="main">, 
// delete the <div class="col-md-6"> element.
	// CA_20170201: from <div class="col-md-6"> to it's </div>.

// Replace it with this HTML. 
// Type in the contents exactly as you see here:

	// <div ng-repeat="product in products" class="col-md-6"> 
	//   <div class="thumbnail"> 
	//     <img src="img/the-book-of-trees.jpg"> 
	//     <p class="title">{{ product.name }}</p> 
	//     <p class="price">{{ product.price | currency }}</p> 
	//     <p class="date">{{ product.pubdate | date }}</p> 
	//   </div> 
	// </div>
// You'll see that both products have the same cover image. 
// Let's fix this bug in the next exercise. 
// Click Next to continue.


//////////////
////// Lesson 7/11 ng-repeat II

// Well done! You got both books in $scope.products to show up in the view. 
// How does it work?

// In the controller, we used products to store an array containing two objects.
// Then in the view, we added <div ng-repeat="product in products">. 
// Like ng-app and ng-controller, the ng-repeat is a directive. 
// It loops through an array and displays each element. 
// Here, the ng-repeat repeats all the HTML inside <div class="col-md-6"> 
// for each element in the products array.

// In this way, ng-repeat shows both products in the $scope.products array. 
// Instead of writing the same HTML twice as before, 
// we just use ng-repeat to generate the HTML twice.

//// Instructions:

//// 1.
// The problem now is that both products have the same image. Let's fix this.

// In the view inside <div class="col-md-6">, replace

// <img src="img/the-book-of-trees.jpg">
// with

// <img ng-src="{{ product.cover }}">
// The ng-src is a directive that sets the <img> element's src to a property in the controller.


//////////////
////// Lesson 8/11 Directives

// We've used a few directives so far - ng-app, ng-controller, ng-repeat, and ng-src. 
// What can we generalize about directives?

// Directives bind behavior to HTML elements. 
// When the app runs, AngularJS walks through each HTML element looking for directives. 
// When it finds one, AngularJS triggers that behavior 
// (like attaching a scope or looping through an array).

//// Instructions:

/// 1.
// In the controller, add two of your favorite books to the $scope.products array.
// The view will update as the ng-repeat loops the new elements in the $scope.products array.

//// MainController:
// app.controller('MainController',['$scope',function($scope) {
//   $scope.title = 'MyTitle';
//   $scope.promo = '2-4-1 Deal';
//   $scope.products = [ 
//   { 
//     name: 'The Book of Trees', 
//     price: 19, 
//     pubdate: new Date('2014', '03', '08'), 
//     cover: 'img/the-book-of-trees.jpg' 
//   }, 
//   { 
//     name: 'Program or be Programmed', 
//     price: 8, 
//     pubdate: new Date('2013', '08', '01'), 
//     cover: 'img/program-or-be-programmed.jpg' 
//   },
//   { 
//     name: 'Dune', 
//     price: 6, 
//     pubdate: new Date('1965', '08', '01'), 
//     cover: 'img/dune.jpg' 
//   },
//   { 
//     name: 'Stuff Matters', 
//     price: 14, 
//     pubdate: new Date('2014', '05', '27'), 
//     cover: 'img/stuff-matter.jpg' 
//   }
// ];
// }]);


//////////////
////// Lesson 9/11 ng-click I

// So far we've made a static AngularJS app by adding properties in the controller 
// and displaying them in the view. 
// AngularJS is a framework for building dynamic web apps, 
// so let's start to make this app interactive.

//// Instructions:

//// 1.
// In the controller in the $scope.products array, 
// add a new property named likes to each element. 
// Set all likes properties to 0.

//// 2.
// In the view under <p class="date">, type in a rating element:

// <div class="rating"> 
//   <p class="likes">+ </p> 
// </div>
// Inside <p class="likes">, display a product's likes using an expression.

//// 3.
// Back in the controller after $scope.products, 
// attach a new property to $scope named plusOne. 
// Set it equal to function. Type in the contents exactly as you see here:

function(index) { 
  $scope.products[index].likes += 1; 
};

//// 4.
// In the view modify <p class="likes"> to look like this:
	// <p class="likes" ng-click="plusOne($index)">

// View the AngularJS app in the browser. 
// Click on the +0 in each product tile.

//// index.html:
//        <div ng-repeat="product in products" class="col-md-6">
//          <div class="thumbnail">
//            <img ng-src="{{ product.cover }}">
//            <p class="title"> {{ product.name |uppercase }} </p>
//            <p class="price"> {{ product.price | currency }} </p>
//            <p class="date"> {{ product.pubdate | date }} </p>
//            <div class="rating"> 
//              <p class="likes" ng-click="plusOne($index)">+ {{ product.likes }} </p> 
//            </div>
//          </div>
//        </div>


//////////////
////// Lesson 10/11 ng-click II

// Great! Each time you click on the number of likes, the number goes up. 
// How does it work?

// The ng-click is a directive. 
// When <p class="likes"> is clicked, 
// ng-click tells AngularJS to run the plusOne() function in the controller.

// The plusOne() function gets the index of the product that was clicked, 
// and then adds one to that product's likes property.

// Notice that the plusOne() doesn't interact with the view at all; 
// it just updates the controller. 
// Any change made to the controller shows up in the view.

//// Instructions:

//// 1.
// In the controller in the $scope.products array, 
// add a new property named dislikes to each element. Set dislikes to 0.

//// 2.
// In the view under <p class="likes">, add an element for <p class="dislikes">. 
// Then display a product's dislikes using an expression.

	// <p class="dislikes">+ {{ product.dislikes }} </p> 

//// 3.
// Back in the controller after $scope.products, 
// attach a new property to $scope named minusOne. 
// Set it equal to a function that adds one to a product's dislikes property. 
// Adapt the code from the plusOne() function to do this.

  $scope.minusOne = function(index) { 
    $scope.products[index].dislikes += 1; 
  };

//// 4.
// In the view, use ng-click to trigger the minusOne() function 
// when <p class="dislikes"> is clicked.

// View the AngularJS app in the browser. 
// Click on the -0 in each product tile.

//// index.html:
//        <div ng-repeat="product in products" class="col-md-6">
//          <div class="thumbnail">
//            <img ng-src="{{ product.cover }}">
//            <p class="title"> {{ product.name |uppercase }} </p>
//            <p class="price"> {{ product.price | currency }} </p>
//            <p class="date"> {{ product.pubdate | date }} </p>
//            <div class="rating"> 
//              <p class="likes" ng-click="plusOne($index)">+ {{ product.likes }} </p> 
//              <p class="dislikes" ng-click="minusOne($index)">- {{ product.dislikes }} </p>
//            </div>
//          </div>
//        </div>


//////////////
////// Lesson 11/11 Generalizations

// Congratulations! 
// You built an AngularJS app from scratch. What can we generalize so far?

// A user visits the AngularJS app.
// The view presents the app's data through the use of expressions, filters, and directives. 
// Directives bind new behavior HTML elements.
// A user clicks an element in the view. If the element has a directive, AngularJS runs the function.
// The function in the controller updates the state of the data.

// The view automatically changes and displays the updated data. 
// The page doesn't need to reload at any point.



///////////////////////////////////
///////////////////////////////////
// Directives
///////////////////////////////////
///////////////////////////////////

//////////////
// Exercises
//////////////

//////////////
////// Lesson 1/8 Directives I

// Here's an AngularJS app for a mobile app store:

// In the controller MainController.js, there are three objects 
// $scope.move, $scope.shutterbugg, and $scope.gameboard 
// that each contain info about an app, like its title and price.

// In the view index.html in the .main section, each app is displayed inside a .card div.

// But looking at the view, the same code is written over and over again to display each app. 
// This is repetitive and error-prone. Let's fix this.

//// Instructions:

//// 1.
// In the new file js/directives/appInfo.js, type in this code:

app.directive('appInfo', function() { 
  return { 
    restrict: 'E', 
    scope: { 
      info: '=' 
    }, 
    templateUrl: 'js/directives/appInfo.html' 
  }; 
});

//// 2.
//Include this new JavaScript file in index.html in line 48 as a <script> element.
	// <script src="js/directives/appInfo.js"></script>

//// 3.
// In the new file js/directives/appInfo.html. Type in this HTML to display an app's info:

// <img class="icon" ng-src="{{ info.icon }}"> 
// <h2 class="title">{{ info.title }}</h2> 
// <p class="developer">{{ info.developer }}</p> 
// <p class="price">{{ info.price | currency }}</p>

//// 4.
// In index.html, replace the contents of the first .card div with the new <app-info> element:

// <div class="card"> 
//   <app-info info="move"></app-info> 
// </div>

//	CA_20170201: replaces the following for each item.
//
//	<div class="card">
//          <img class="icon" ng-src="{{ shutterbugg.icon }}">
//          <h2 class="title">{{ shutterbugg.title }}</h2>
//          <p class="developer">{{ shutterbugg.developer }}</p>
//          <p class="price">{{ shutterbugg.price | currency }}</p>
//        </div>

//// 5.
// Do the same for the second and third .card divs. 
// Replace their contents with <app-info info="shutterbugg"></app-info> and <app-info info="gameboard"></app-info>

// View the AngularJS app in the browser by typing http://localhost:8000.

//////////////
////// Lesson 2/8 Directives II

// What did we just do? We wrote code to teach the browser a new HTML element <app-info>, 
// and used it in the view to display each app's details.

// First in js/directives/appInfo.js, we made a new directive. 
// We used app.directive to create a new directive named 'appInfo'. 
// It returns an object with three options:

	// 1. restrict specifies how the directive will be used in the view. 
		// The 'E' means it will be used as a new HTML element.
	// 2. scope specifies that we will pass information into this directive through an attribute named info. 
		// The = tells the directive to look for an attribute named info in the <app-info> element, like this:
 		// <app-info info="shutterbugg"></app-info>
		// The data in info becomes available to use in the template given by templateURL.
	// 3. templateUrl specifies the HTML to use in order to display the data in scope.info. 
		// Here we use the HTML in js/directives/appInfo.html.

// Looking at js/directives/appInfo.html, we define the HTML to display details about an app, like its title and price. 
// We use expressions and filters to display the data.

// Then in index.html we use the new directive as the HTML element <app-info>. 
// We pass in objects from the controller's scope ($scope.shutterbugg) into 
// the <app-info> element's info attribute so that it displays.




//////////////
////// Lesson 3/8 Directives III

Why is creating your own directives useful?

Readability. Directives let you write expressive HTML. Looking at index.html you can understand the app's behavior just by reading the HTML.
Reusability. Directives let you create self-contained units of functionality. We could easily plug in this directive into another AngularJS app and avoid writing a lot of repetitive HTML.



///////////////////////////////////
///////////////////////////////////
// Services
///////////////////////////////////
///////////////////////////////////



///////////////////////////////////
///////////////////////////////////
// Routing
///////////////////////////////////
///////////////////////////////////






