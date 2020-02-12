var c = document.getElementById('playground');
var ctx = c.getContext('2d')
var circle = function(s){
  ctx.beginPath();
  ctx.arc(300,300, s, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
}

var stop = function(requestid){
  window.cancelAnimation(requestid);
}

var animation = function()


var clear = document.getElementById("clear");
clear.addEventListener("click", function(){ctx.clearRect(0, 0, c.width, c.height);});
c.addEventListener("mousedown", function(){circle()});
