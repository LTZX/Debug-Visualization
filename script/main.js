var ncolor = "class", nsize = "lines";

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

function cutstr(str){
  var i = 0;
  for(var char in str){
    if(str[char] === '-') break;
    i += 1;
  }
  return str.substring(0,i);
}

function orgtimedata(time){
  for(each in time){
    for(d in time[each]){
        time[each][d].date = parseTime(time[each][d].date);
        time[each][d].close = +time[each][d].close;
      }
    }
    return time;
}

function onenode(d,data){
  d3.selectAll(".node").attr("fill", "grey")
  d3.select("#node"+d.id)
  .attr("fill", function(d) { return colorf(d.data[ncolor]); })
  $('#code').empty();
  $('#code').append(data.code[d.id])
  $('#line-chart').empty();
  $('#gittable').empty();
  $('#bar-chart').empty();
  drawlinechart(data.time[d.id]);
  drawgittable(data.table[d.id]);
  drawbarchart(data.bar[d.id]);
  d3.select("#lblock").text(d.id + " - " + d.data.name)
}

function setback(data){
  $('#code').empty();
  $('#line-chart').empty();
  $('#gittable').empty();
  $('#bar-chart').empty();

  drawlinechart(data.time['total']);
  drawgittable(data.table['total']);
  drawbarchart(data.bar['total']);
}

d3.json("data/data.json", function(error, data) {
    orgtimedata(data.time);
    // === set up the selections
    var groupby = data.groupby;
    //$('#classes').append()
    for(each in groupby){
      for(ele in groupby[each]){
        $('#o'+each).append('<option>'+ele+'</option>');
      }
    }
    var methods = data.force.nodes;
    for(each in methods){
      $('#omethod').append('<option>'+ methods[each].data['MID'] + ' - ' + methods[each].data.name+'</option>');
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
      setback(data)
      var that = this;
      d3.selectAll(".node")
      .attr("fill", function(d) { return colorf(d.data[that.id]); })
      d3.select("#cblock")
      .text("Color of Node: " + that.id);
      ncolor = that.id
    })
    d3.selectAll(".bugbutton").on('click',function(){
      setback(data)
      if(this.id === "show"){
        d3.selectAll(".node")
        .attr("r", function(d){ return scalebug(d.data.bugs.length); })
        d3.selectAll(".true")
        .style("stroke-width", "2px")
        .style("stroke", "red");
        d3.select("#sblock")
        .text("Size Of Node: Number of Bugs");
      } else {
        d3.selectAll(".node")
        .attr("r", function(d){ return scalesize(d.data.lines); })
        .style("stroke", "#fff")
        .style("stroke-width", "1.5px")
        d3.selectAll(".link")
        .style("stroke", "#999")
        .style("stroke-width", "1px")
        d3.select("#sblock")
        .text("Size Of Node: Number of Lines");
      }
    })

    var groupby = data.groupby;
    $(".listselect").on('changed.bs.select', function(){
      $('.methodselect').selectpicker('deselectAll');
      setback(data)

      d3.selectAll(".node").attr("fill", "grey")
      var selected = [];
      for(each in groupby){
        var val = $("#o"+each).val();
        for(select in val){
          for(ele in groupby[each][val[select]]){
            var ele = groupby[each][val[select]][ele]
            d3.select("#node"+ele)
            .attr("fill", function(d) { return colorf(d.data[ncolor]); })
          } } }
    })

    $(".methodselect").on('changed.bs.select', function(){
      $('.listselect').selectpicker('deselectAll');
      var val = $("#omethod").val();
      onenode(data.force.nodes[cutstr(val[0])],data);
    })

    d3.selectAll('.node').on('click',function(d){
      $('.listselect').selectpicker('deselectAll');
      $('.methodselect').selectpicker('deselectAll');
      onenode(d,data);
    })
    drawlinechart(data.time['total']);
    drawgittable(data.table['total']);
    drawbarchart(data.bar['total']);
    //fancy table
    //$('#gittable').append(data.tmp);

    //$(document).ready(function() {
    //    $('#example').DataTable();
    //} );


})
