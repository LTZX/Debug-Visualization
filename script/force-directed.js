var colorf = d3.scaleOrdinal(cuscolors);

var scalesize, scalebug;
function drawforce(graph){
  var widthf = $("#forced-directed").width();
  var heightf = $("#page-content-wrapper").height() - 120;
  var str = d3.max([widthf,heightf]);

  var scalestr = d3.scaleLinear().domain([430,830]).range([-15, -80]);
  scalesize = d3.scaleLinear().domain([0,d3.max(graph.nodes, function(d){ return d.data.lines; })]).range([5,20]);
  scalebug = d3.scaleLinear().domain([0,d3.max(graph.nodes, function(d){ return d.data.bugs.length; })]).range([5,20]);

  var simulation = d3.forceSimulation()
      .force("link", d3.forceLink().id(function(d) { return d.id; }))
      .force("charge", d3.forceManyBody().strength(function(){
        if(str < 430){ return -15; }
        else { return scalestr(str); }
      }).distanceMax(heightf/5))
      .force("center", d3.forceCenter(widthf / 2, heightf / 2));

    var svgf = d3.select("#forced-directed")
      .append("svg")
      .attr("width", widthf)
      .attr("height", heightf)

    svgf.append("text")
    .text("Color of Node: Class")
    .attr("id", "cblock")
    .attr("transform", "translate(50,50)")
    .style("font-size", "15px")
    .style("text-transform", "capitalize")

    svgf.append("text")
    .text("Size Of Node: Number of Lines")
    .attr("id", "sblock")
    .attr("transform", "translate(50,75)")
    .style("font-size", "15px")
    .style("text-transform", "capitalize")


    var hoverins = svgf.append("text")
    .text("Hover to see the name of methods and its class")
    .style("font-size", "18px")
    .style("text-transform", "capitalize")
    .style("opacity",0.5)

    var hiw = hoverins.node().getBBox();
    hoverins
    .attr("transform", "translate("+ (widthf - hiw.width - 50) +", 50)")

    var link = svgf.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(graph.links)
      .enter().append("line")
      .attr("class", function(d){ return "link " + d.bug; })

    var node = svgf.append("g")
        .attr("class", "nodes")
      .selectAll("circle")
      .data(graph.nodes)
      .enter().append("circle")
        .attr("class", function(d){ return "node " + d.bug; })
        .attr("id", function(d){ return "node" + d.id; })
        .attr("r", function(d){ return scalesize(d.data.lines); })
        .attr("fill", function(d) { return colorf(d.data.class); })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("title")
        .text(function(d) { return d.data['MID'] + " - " + d.data.name; });

    simulation
        .nodes(graph.nodes)
        .on("tick", ticked);

    simulation.force("link")
        .links(graph.links);

    function ticked() {
      link
          .attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });

      node
          .attr("cx", function(d) { return d.x; })
          .attr("cy", function(d) { return d.y; });
    }

  function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
  }

  function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}
