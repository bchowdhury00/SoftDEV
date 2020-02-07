// Calvin Chu, Biraj Chowdhury
// SoftDev1 pd9
// K5 -- ...and I want to Paint It Better
// 2020-02-06

//  e.preventDefault(); -> if the agent calling the method does not handle the event, do not run its normal functionality
//  ctx.beginPath(); -> begins a new line/path to start drawing
//  e.offsetX -> provides the offset in the X coordinate of the mouse the position of the event's occurence and the padding edge of the target
//  e.offsetY -> provides the offset in the Y coordinate of the mouse the position of the event's occurence and the padding edge of the target

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
  if (isDrawing && option == 0) ctx.arc(event.offsetX, event.offsetY, 5, 0, 2 * Math.PI);
  if (isDrawing && option == 1 && corners.length == 0) {
    corners.push(event.offsetX);
    corners.push(event.offsetY);
  }
  if (!isDrawing && option == 1) {
    var newX = event.offsetX;
    var newY = event.offsetY;
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
      ctx.beginPath();
      ctx.arc(event.offsetX, event.offsetY, 5, 0, 2 * Math.PI);
      ctx.stroke();
      ctx.fill();
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
