var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
};

var removeItem = function(e) {
  e.remove()
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener( 'mouseover', function(){changeHeading(this.innerHTML)});
  lis[i].addEventListener( 'mouseout', function(){changeHeading("Hello World!")});
  lis[i].addEventListener( 'click', function(){removeItem(this)});
}

var addItem = function() {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.addEventListener( 'mouseover', function(){changeHeading(this.innerHTML)});
  item.addEventListener( 'mouseout', function(){changeHeading("Hello World!")});
  item.addEventListener( 'click', function(){removeItem(this)});
  item.innerHTML = "WORD";
  list.append(item);
}

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
	if ( n <= 2 ){
		return 1;
	}
	else{
		return fib(n-1) + fib(n-2);
	}
};

var addFib = function(e) {
	console.log(e);
	var list = document.getElementById("fiblist");
	var len = list.getElementsByTagName("li").length;
	var item = document.createElement("li");
	item.innerHTML = fib(len);
	list.append(item);
}
var FibList = [];

var addFib2 = function(e) {
    var list = document.getElementById("fiblist");
    var len = FibList.length
    var item = document.createElement("li");
    if (len < 2){
	item.innerHTML = 1;
	FibList.push(1);
    }
    else{
	item.innerHTML = FibList[len - 1] + FibList[len - 2];
	FibList.push(FibList[len - 1] + FibList[len - 2]);	
    }
    list.append(item);
}

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
