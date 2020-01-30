/*
Team prefix -- Manfred Tan, Biraj Chowdhury, and Tammy Chen
SoftDev1 pd9
K27 -- Sequential Progression
2019-12-10
*/


/*
var foo = function(n){
  return n;
};
*/

var factorial = function(n){
  if (n == 1) return 1;
  return (n * factorial(n-1));
};


var fibonacci = function(n){
  if (n < 2) return n;
  if (n == 2) return 1;
  return (fibonacci(n-1) + fibonacci(n-2));
};

var gcd = function(a,b){
  if (a < b){
    return gcd(b, a);
  }
  if (a % b == 0) return b;
  return gcd(a-b, b);
}

students = ['Manfred', 'Biraj', 'Tammy', 'Fluffy', 'Unicorn']

var randomStudent = function(){
  var index = Math.floor(Math.random() * students.length);
  return students[index];
}
