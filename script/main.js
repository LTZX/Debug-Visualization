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
    console.log(data.force)
    drawforce(data.force);
})

d3.json("data/force-directed.json", function(error, graph) {
  console.log(graph)
  //drawforce(graph)
})
