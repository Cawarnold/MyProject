app.controller('MainController',['$scope',function($scope) {
  $scope.title = 'MyTitle';
  $scope.promo = '2-4-1 Deal';
  $scope.products = [ 
  { 
    name: 'The Book of Trees', 
    price: 19, 
    pubdate: new Date('2014', '03', '08'), 
    cover: 'img/the-book-of-trees.jpg',
    likes: 0,
    dislikes: 0
  }, 
  { 
    name: 'Program or be Programmed', 
    price: 8, 
    pubdate: new Date('2013', '08', '01'), 
    cover: 'img/program-or-be-programmed.jpg',
    likes: 0,
    dislikes: 0
  },
  { 
    name: 'Dune', 
    price: 6, 
    pubdate: new Date('1965', '08', '01'), 
    cover: 'img/dune.jpg',
    likes: 0,
    dislikes: 0
  },
  { 
    name: 'Stuff Matters', 
    price: 14, 
    pubdate: new Date('2014', '05', '27'), 
    cover: 'img/stuff-matter.jpg',
    likes: 0,
    dislikes: 0
  }
  ];
  $scope.plusOne = function(index) { 
    $scope.products[index].likes += 1; 
  };
  $scope.minusOne = function(index) { 
    $scope.products[index].dislikes += 1; 
  };
}]);