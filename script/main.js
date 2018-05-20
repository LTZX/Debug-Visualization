d3.json("data/data.json", function(error, data) {
    console.log(data);
    // === set up the selections
    var groupby = data.groupby;
    //$('#classes').append()
    for(each in groupby){
      for(ele in groupby[each]){
        $('#'+each+'options').append('<option>'+ele+'</option>');
      }
    }
    var methods = data.force.nodes;
    for(each in methods){
      $('#methodoptions').append('<option>'+methods[each].id+'</option>');
    }
    var f = data.filedata;
    $('#table1').append('<td>'+f["lines-of-code"]+'</td><td>'+f.lines+
    '</td><td>'+f.comments+'</td><td>'+f.method+
    '</td><td>'+f.class+'</td>');
    $('#table2').append('<td>'+f.file +'</td><td>'+f.directory+'</td><td>'+f.bug+
    '</td><td>'+f["time-range"][0]+' ~ '+f["time-range"][1]+'</td><td>'+f.author+
    '</td>');

    drawforce(data.force);
    d3.selectAll(".gbbutton").on('click',function(){
      var that = this;
      d3.selectAll(".node")
      .attr("fill", function(d) { return colorf(d.data[that.id]); })
      d3.select("#cblock")
      .text("Color of Node: " + that.id);
    })
    d3.selectAll(".bugbutton").on('click',function(){
      if(this.id === "show"){
        d3.selectAll(".node")
        .attr("r", function(d){ return scalebug(d.data.bugs.length); })
        d3.selectAll(".true")
        .style("stroke", "red");
        d3.select("#sblock")
        .text("Size Of Node: Number of Bugs");
      } else {
        d3.selectAll(".node")
        .attr("r", function(d){ return scalesize(d.data.lines); })
        .style("stroke", "#fff")
        d3.selectAll(".link")
        .style("stroke", "#999")
        d3.select("#sblock")
        .text("Size Of Node: Number of Lines");
      }
    })
})
