// Calvin Chu, Biraj Chowdhury
// SoftDev1 pd9
// K4 -- I See a Red Door...
// 2020-02-05

var c = document.getElementById("slate");
var ctx = c.getContext('2d');
var option = 0; // 0 (default = dot)
                // 1 (rect)
var isDrawing = false;
var corners = [];

var toggle = document.getElementById("toggle");
var clear = document.getElementById("clear");

var draw = function(d){
  isDrawing = d;
  if (isDrawing && option == 0) ctx.fillRect(event.clientX - c.getBoundingClientRect().left, event.clientY - c.getBoundingClientRect().top, 5, 5);
  if (isDrawing && option == 1 && corners.length == 0) {
    corners.push(event.clientX - c.getBoundingClientRect().left);
    corners.push(event.clientY - c.getBoundingClientRect().top);
  }
  if (!isDrawing && option == 1) {
    var newX = event.clientX - c.getBoundingClientRect().left;
    var newY = event.clientY - c.getBoundingClientRect().top;
    var deltaX = Math.abs(corners[0] - newX);
    var deltaY = Math.abs(corners[1] - newY);
    if (corners[0] <= newX && corners[1] <= newY) ctx.fillRect(corners[0], corners[1], deltaX, deltaY);
    else if (corners[0] > newX && corners[1] <= newY) ctx.fillRect(newX, corners[1], deltaX, deltaY);
    else if (corners[0] <= newX && corners[1] > newY) ctx.fillRect(corners[0], newY, deltaX, deltaY);
    else if (corners[0] > newX && corners[1] > newY) ctx.fillRect(newX, newY, deltaX, deltaY);
    corners = [];
  }
};

var move = function(e){
  if (isDrawing) {
    if (option == 0) {
      ctx.fillRect(event.clientX - c.getBoundingClientRect().left, event.clientY - c.getBoundingClientRect().top, 5, 5);
    }
  }
};

var swap = function(){
    if (option == 0){
      toggle.innerText = "Rectangle";
      option = 1;
    }
    else{
      toggle.innerText = "Dot";
      option = 0;
    }
};

clear.addEventListener("click", function(){ctx.clearRect(0, 0, c.width, c.height);});
toggle.addEventListener("click", function(){swap()});
c.addEventListener("mousedown", function(){draw(true)});
c.addEventListener("mousemove", function(e){move(e)});
window.addEventListener("mouseup", function(){draw(false)});
