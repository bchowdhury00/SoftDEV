window.onload = function() {
  var d = document.getElementById("moves");
  var c = document.getElementById("cats");
  var r = document.getElementById("render");
  var t = document.getElementById("transition");

  var parse = function() {
    var arr = [];
      for (var i = 0; i < d.childElementCount; i++) {
        arr.push(d.children[i].innerHTML.split(","));
    }
    return arr;
  };
  var catData = parse();
  var one = [], two = [], tre = [], fou = [];
  var dataSet = [one, two, tre, fou];
  for (var y = 0; y < catData.length; y++) {
    for (var x = 1; x < catData[y].length; x++) {
      dataSet[x-1].push({"country":catData[y][0], "val":catData[y][x]});
    }
  };
  var transCounter = 0;
  var isRendered = false;
  var categories = [];
  for (var i = 0; i < c.childElementCount; i++) {
    categories.push(c.children[i].innerHTML);
  }
  categories = categories.slice(1, categories.length);

  var render = function(e) {
    if (isRendered) {
      var data = dataSet[e%dataSet.length];
      // set the dimensions and margins of the graph
      var margin = {top: 50, right: 20, bottom: 30, left: 150},
          width = 960 - margin.left - margin.right,
          height = data.length*10;
      // set the ranges
      var y = d3.scaleBand()
                .range([height, 0])
                .padding(0.1);
      var x = d3.scaleLinear()
                .range([0, width]);
      // append the svg object to the body of the page
      // append a 'group' element to 'svg'
      // moves the 'group' element to the top left margin
      d3.select("body").selectAll("svg").remove();
      var svg = d3.select("body").append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
        .append("g")
          .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");
        // format the data
        data.forEach(function(d) {
          d.val = +d.val;
        });
        // Scale the range of the data in the domains
        x.domain([0, d3.max(data, function(d){ return d.val; })])
        y.domain(data.map(function(d) { return d.country; }));
        //y.domain([0, d3.max(data, function(d) { return d.sales; })]);
        // append the rectangles for the bar chart
        svg.selectAll(".bar")
            .data(data)
          .enter().append("rect")
            .attr("class", "bar")
            //.attr("x", function(d) { return x(d.sales); })
            .attr("width", function(d) {return x(d.val); } )
            .attr("y", function(d) { return y(d.country); })
            .attr("height", y.bandwidth());
        // add the x Axis
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));
        svg.append("g")
            .attr("transform", "translate(0,0)")
            .call(d3.axisTop(x));
        // add the y Axis
        svg.append("g")
            .call(d3.axisLeft(y));
        svg.append("text")
            .attr("x", (width / 2))
            .attr("y", 0 - (margin.top / 2))
            .attr("text-anchor", "middle")
            .style("font-size", "16px")
            .style("text-decoration", "underline")
            .text(categories[e%dataSet.length]);
    }
  }

  r.addEventListener("click", function(){isRendered = true; render(transCounter);});
  t.addEventListener("click", function(){if (isRendered) {transCounter++;} render(transCounter);});

}
