//Connor Oh & Jeff Lin & Biraj Chowdhury
//SoftDev2 pd9
//K12 -- Connect the Dots
//2020-03-38

var xmlns = "http://www.w3.org/2000/svg"
var svg = document.getElementById('vimage'); //gets the svg element
var clearbutton = document.getElementById("clear"); //gets the clear button element


var clearSvg = function(e){
    while(svg.firstChild){
	svg.removeChild(svg.firstChild);
    }
};

var drawCircle = function(){
    x=event.offsetX;
    y=event.offsetY;
    var circle = document.createElementNS(xmlns,"circle");
    circle.setAttribute ("r",10);
    circle.setAttribute("cx",x);
    circle.setAttribute("cy",y);
    circle.setAttribute("fill","black");
    circle.addEventListener('click',changeColor);
    svg.appendChild(circle);

};


var changeColor = function(e){
    if (e.target.getAttribute("fill") == "black"){
	e.target.setAttribute("fill","green");
    }
    else{
	e.target.setAttribute("cx",Math.random() * 500);
	e.target.setAttribute("cy",Math.random() * 500);
	e.target.setAttribute("fill","black");
    }
}


clearbutton.addEventListener('click', clearSvg);
svg.addEventListener('click',function(){drawCircle()});
