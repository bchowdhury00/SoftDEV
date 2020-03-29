//Connor Oh & Jeff Lin & Biraj Chowdhury
//SoftDev2 pd9
//K12 -- Connect the Dots
//2020-03-38

var xmlns = "http://www.w3.org/2000/svg"
var svg = document.getElementById('vimage'); //gets the svg element
var clearbutton = document.getElementById("clear"); //gets the clear button element
var drawing = false; //checks if we drawing yet
var prevX, prevY; //the previous coordinates

var clearSvg = function(e){ //clears the canvas
  /*
  var clearedVimage = document.createElementNS(xmlns,"rect");
  clearedVimage.setAttribute("width", 500);
  clearedVimage.setAttribute("height", 500);
  clearedVimage.setAttribute("style", "fill:white");
  svg.append(clearedVimage);
  */
    while(svg.firstChild){
	svg.removeChild(svg.firstChild);
    }
    drawing = false;
};

var drawLine = function(x,y){
    var line = document.createElementNS(xmlns,"line");
    line.setAttribute("x1",prevX);
    line.setAttribute("y1",prevY);
    line.setAttribute("x2",x);
    line.setAttribute("y2",y);
    line.setAttribute("stroke","black");
    svg.appendChild(line);
};

var drawCircle = function(){
    x=event.offsetX;
    y=event.offsetY;
    var circle = document.createElementNS(xmlns,"circle");
    circle.setAttribute ("r",2);
    circle.setAttribute("cx",x);
    circle.setAttribute("cy",y);
    svg.appendChild(circle);
    if (drawing){
	drawLine(x,y);
    }
    prevX = x;
    prevY = y;
    drawing = true;
};



clearbutton.addEventListener('click', clearSvg);
svg.addEventListener('click',function(){drawCircle()});
