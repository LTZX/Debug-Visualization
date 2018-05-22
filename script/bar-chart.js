var div = d3.select("body").append("div").attr("class", "toolTip");
var round = d3.format(".2f");

function drawbarchart(data){
  var sum = d3.sum(data,function(d){ return d.value;})

  var widthb = $("#exTab2").width() - 30;
  var heightb = $("#exTab2").height() - 10;
  var axisMargin = 20,
      marginb = 30,
      valueMargin = 4,
      barHeight = (heightb-axisMargin-marginb*2)* 0.4/data.length,
      barPadding = (heightb-axisMargin-marginb*2)*0.6/data.length,
      scaleb, xAxisb, labelWidth = 0;

  var max = d3.max(data, function(d) { return d.value; });
  var colorb = d3.scaleOrdinal(d3.schemeCategory10);

  var svgb = d3.select('#bar-chart')
          .append("svg")
          .attr("width", widthb)
          .attr("height", heightb)
          .attr("transform", "translate(0,30)");

  var bar = svgb.selectAll("g")
          .data(data)
          .enter()
          .append("g");

  svgb.append('text')
    .text("Hover to see the percentage")
    .attr("id", "bblock")
    .attr("transform", "translate(30,8)")
    .style("font-size", "12px")
    .style("opacity",0.5)

  bar.attr("class", "bar")
          .attr("cx",0)
          .attr("transform", function(d, i) {
              return "translate(" + marginb + "," + (i * (barHeight + barPadding) + barPadding) + ")";
          });

  bar.append("text")
          .attr("class", "labelb")
          .attr("y", barHeight / 2)
          .attr("dy", ".35em") //vertical align middle
          .text(function(d){
              return d.label;
          }).each(function() {
            var count = this.innerHTML.length;
      labelWidth = Math.ceil(Math.max(labelWidth, count*10));
  });

  scaleb = d3.scaleLinear()
          .domain([0, max])
          .range([0, widthb - marginb*2 - labelWidth]);

  xAxisb = d3.axisBottom(scaleb)
           .tickSize(-heightb + 2*marginb + axisMargin)
           .ticks(max)

  bar.append("rect")
          .attr("transform", "translate("+labelWidth+", 0)")
          .attr("height", barHeight)
          .attr("width", function(d){
              return scaleb(d.value);
          })
          .attr("fill", function(d){
              return colorb(d.label);
          });

  bar.append("text")
          .attr("class", "value")
          .attr("y", barHeight / 2)
          .attr("dx", -valueMargin + labelWidth) //margin right
          .attr("dy", ".35em") //vertical align middle
          .attr("text-anchor", "end")
          .text(function(d){ return d.value; })
          .attr("x", function(d){
              var width = 100;
              return Math.max(width + valueMargin, scaleb(d.value));
          });

  bar
          .on("mousemove", function(d){
              div.style("left", d3.event.pageX+10+"px");
              div.style("top", d3.event.pageY-25+"px");
              div.style("display", "inline-block");
              div.html((d.label + ': ' + round(d.value/sum*100)+"%"));
          });
  bar
          .on("mouseout", function(d){
              div.style("display", "none");
          });

  svgb.append("g")
          .attr("class", "axisHorizontal")
          .attr("transform", "translate(" + (marginb + labelWidth) + ","+ (heightb - axisMargin*2 - marginb)+")")
          .call(xAxisb);
}
