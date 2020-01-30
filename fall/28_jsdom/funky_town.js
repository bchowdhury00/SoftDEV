/*
Team prefix --  Biraj Chowdhury and Kazi Jamal
SoftDev1 pd9
K28 -- Electric Bungaloo
2019-12-11
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
    return fibonacci(n-1) + fibonacci(n-2);
    
};

var gcd = function(a,b){
  if (a < b){
    return gcd(b, a);
  }
  if (a % b == 0) return b;
  return gcd(a-b, b);
};

var students = ['Manfred', 'Biraj', 'Tammy', 'Fluffy', 'Unicorn'];

var randomStudent = function(){
  var index = Math.floor(Math.random() * students.length);
  return students[index];
};

var printToConsoleFib = function(){
    var ans = fibonacci(8);
    console.log(ans);
    showoutput(ans)
};

var printToConsoleFact = function(){
    var ans = factorial(7);
    console.log(ans);
    showoutput(ans)
};

var printToConsoleRand = function(){
    var ans = randomStudent();
    console.log(ans);
    showoutput(ans);

}

var printToConsoleGreat = function(){
    var ans = gcd(1115,45);
    console.log(ans);
    showoutput(ans);
};

var huh = document.getElementById("a");
var what = document.getElementById("b");
var err = document.getElementById("c");
var areyousure = document.getElementById("d");
var output = document.getElementById("e");

var answers = []

var showoutput = function(n){
    if (answers.length > 0)
	answers.pop();
    answers.push(n);
    output.append(answers);
};
    

huh.addEventListener('click',printToConsoleFib);
what.addEventListener('click',printToConsoleFact);
err.addEventListener('click',printToConsoleRand);
areyousure.addEventListener('click',printToConsoleGreat);
