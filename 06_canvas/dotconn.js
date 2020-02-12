// Calvin Chu, Biraj Chowdhury
// SoftDev1 pd9
// K6 -- Dot Dot Dot
// 2020-02-11

var c = document.getElementById("playground");
var ctx = c.getContext('2d');
var option = 0; // 0 (default = dot)
                // 1 (rect)

var lastPoint = []
var draw = function() {
  ctx.beginPath();
  ctx.arc(event.offsetX, event.offsetY, 5, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  if (lastPoint.length == 0) lastPoint = [event.offsetX, event.offsetY]
  else {
    ctx.beginPath();
    ctx.moveTo(lastPoint[0], lastPoint[1]);
    ctx.lineTo(event.offsetX, event.offsetY);
    lastPoint = [event.offsetX, event.offsetY];
    ctx.stroke();
  }
};


var clear = document.getElementById("clear");
clear.addEventListener("click", function(){ctx.clearRect(0, 0, c.width, c.height); lastPoint = [];});
c.addEventListener("mousedown", function(){draw()});
