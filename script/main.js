var ncolor = "class", nsize = "lines";

$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

function cutstr(str){
  var i = 0;
  for(var char in str){
    if(char == '-') break;
    i += 1;
  }
  return str.substring(0,i);
}

d3.json("data/data.json", function(error, data) {
    console.log(data);
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
      var that = this;
      d3.selectAll(".node")
      .attr("fill", function(d) { return colorf(d.data[that.id]); })
      d3.select("#cblock")
      .text("Color of Node: " + that.id);
      ncolor = that.id
    })
    d3.selectAll(".bugbutton").on('click',function(){
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
    d3.selectAll(".listselect").on('change', function(){
      $('.methodselect').selectpicker('deselectAll');
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

    d3.selectAll(".methodselect").on('change', function(){
      $('.listselect').selectpicker('deselectAll');
      d3.selectAll(".node").attr("fill", "grey")
      var val = $("#omethod").val();
      for(ele in val){
        var id = cutstr(ele)
        d3.select("#node"+id)
        .attr("fill", function(d) { return colorf(d.data[ncolor]); })
      }
    })

    var codes = data.code;
    d3.selectAll('.node').on('click',function(d){
      $('#code').empty();
      $('#code').append(codes[d.id])
    })

    //fancy table
    //$('#gittable').append(data.tmp);

    //$(document).ready(function() {
    //    $('#example').DataTable();
    //} );
})
