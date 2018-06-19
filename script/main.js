var ncolor = "file", nsize = "lines";
var cuscolors = ["#ffcc00","#ff9933","#ff66ff","#3333cc","#cc33ff","#9966ff","#0099ff","#66ccff","#66ffff","#00ff99","#66ff33","#ccff33","#ffff00","#0099cc","#669999"]

var condition = {active:3, length:{1:0,2:0,3:0}, code:{on:"true", data:{'code':" "}}, otherdata:{on:"true", data:{'pie-chart':[]} }, gitdata:{on:"true", data:{'line-chart':[], gittable:[], 'bar-chart':[]} }};
condition['length'][3] = ($(window).height() - 100) * 0.27;
condition['length'][2] = ($(window).height() - 100) * 0.40;
condition['length'][1] = ($(window).height() - 100) * 0.8;

var title1 = ['author', 'time', 'comment', 'GID'];
var title2 = ['file-name', 'method-name', 'line-number', 'bug-detail'];

var project=
{'number-of-tests': 23, 'number-of-bugs': 15};
var bug=[{'file-name': 'test_group.py', 'method-name': 'test_accept', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_accept_not_pending', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_decline', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_decline_degenerate', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_decline_not_pending', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite_full', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite_in_group', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite_individual', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite_not_enrolled', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_invite_wrong_assignment', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_remove', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_remove_degenerate', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_remove_not_in_group', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''},
        {'file-name': 'test_group.py', 'method-name': 'test_remove_self', 'line-number': '26', 'bug-detail': 'AttributeError: \'Course\' object has no attribute \'enroll\''}]

var piedata = [{'name':'Passed','value': (281-7),'percentage':(project['number-of-tests']-project['number-of-bugs'])/project['number-of-tests']},
 {'name':'Failed','value': 7, 'percentage':project['number-of-bugs']/project['number-of-tests']}]

var forcedata;
var bigdata;
d3.select('#detail').on('click',function(){
  this.classList.toggle("clicked");
  var contain = this.classList.contains('clicked');
  if(contain){
    d3.select("#rightpanel").style('display','block')
    d3.select("#leftpanel").attr('class','col-md-7')
    $('#forced-directed').empty();
    drawforce(forcedata,bigdata)
  } else {
    d3.select("#rightpanel").style('display','none')
    d3.select("#leftpanel").attr('class','col-md-12')
    $('#forced-directed').empty();
    drawforce(forcedata,bigdata)
  }
})

var acc = document.getElementsByClassName("accordion");
var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");
        var contain = this.classList.contains('active');
        var panel = this.nextElementSibling;
        if(contain){
          condition['active'] += 1
          condition[panel.id].on = true;
        } else {
          condition['active'] -= 1
          condition[panel.id].on = false;
        }
        /* Toggle between hiding and showing the active panel */
        //console.log(panel.id)
        if (panel.style.display === "none") {
            panel.style.display = "block";
        } else {
            panel.style.display = "none";
        }
        changelayout();
    });
}
function changelayout(){
  var exc = {'gitdata':'exTab2', 'otherdata':'exTab1', 'code':'code'};
  if (condition['active'] == 0){ return; }
  for (i = 0; i < acc.length; i++) {
    var panel = acc[i].nextElementSibling;
    if(condition[panel.id].on == false){ continue; }
    d3.select('#'+exc[panel.id])
    .style('height', condition['length'][condition['active']] + 'px');
    for(var each in condition[panel.id]['data']){
      if(each == "code"){
        $('#code').empty();
        $('#code').append(condition['code']['data']['code'])
      } else {
        $('#' + each).empty();
        switch (each) {
          case 'line-chart':
            drawlinechart(condition[panel.id]['data'][each]);
            break;
          case 'gittable':
            drawgittable(condition[panel.id]['data'][each], 'gittable', 'exTab2', title1);
            break;
          case 'bar-chart':
            drawbarchart(condition[panel.id]['data'][each]);
            break;
          case 'pie-chart':
            drawpiechart(condition[panel.id]['data'][each]);
            break;
          case 'other':
            drawgittable(bug, 'other', 'exTab1', title2);
            break;
        }
      }
    }
  }
}
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
        time[each][d].odate = time[each][d].date;
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
  condition['code']['data']['code'] = data.code[d.id];
  $('#line-chart').empty();
  $('#gittable').empty();
  $('#bar-chart').empty();
  drawlinechart(data.time[d.id]);
  drawgittable(data.table[d.id], 'gittable', 'exTab2', title1);
  drawbarchart(data.bar[d.id]);
  d3.select("#lblock").text(d.id + " - " + d.data.name)
}

function setback(data){
  $('#code').empty();
  $('#line-chart').empty();
  $('#gittable').empty();
  $('#bar-chart').empty();

  drawlinechart(data.time['total']);
  drawgittable(data.table['total'], 'gittable', 'exTab2', title1);
  drawbarchart(data.bar['total']);
}

d3.json("data/final/data.json", function(error, data) {
    bigdata = data;
    forcedata = data.force;
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

    drawforce(data.force, data);
    d3.selectAll(".gbbutton").on('click',function(){
      setback(data)
      var that = this;
      d3.selectAll(".node")
      .attr("fill", function(d) { return colorf(d.data[that.id]); })
      d3.select("#cblock")
      .text("Color of Node: " + that.id);
      ncolor = that.id

      //$('#pie-chart').empty();
      //drawpiechart(data.pie[that.id]);
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


    drawlinechart(data.time['total']);
    drawgittable(data.table['total'], 'gittable', 'exTab2', title1);
    drawbarchart(data.bar['total']);
    drawgittable(bug, 'other', 'exTab1', title2);
    drawpiechart(piedata);

})
