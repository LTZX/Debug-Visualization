var widtht = $("#exTab2").width();
var heightt = $("#exTab2").height();
var titles = ['author', 'time', 'comment', 'GID'];

function drawgittable(data) {
  var sortAscending = true;
  var table = d3.select('#gittable').append('table').attr("class","gittablecontent");
  var headers = table.append('thead').append('tr')
    .selectAll('th')
    .data(titles).enter()
    .append('th')
    .text(function (d) { return d; })
    .style("text-transform", "capitalize")
    .on('click', function (d) {
      headers.attr('class', 'header');
      if (sortAscending) {
        rows.sort(function(a, b) { return b[d] < a[d]; });
        sortAscending = false;
        this.className = 'aes';
      } else {
        rows.sort(function(a, b) { return b[d] > a[d]; });
        sortAscending = true;
        this.className = 'des';
      }
    });

  var rows = table.append('tbody').selectAll('tr')
    .data(data).enter()
    .append('tr');

  rows.selectAll('td')
    .data(function (d) {
      return titles.map(function (k) {
        return { 'value': d[k], 'name': k};
      });
    }).enter()
    .append('td')
    .attr('data-th', function (d) { return d.name; })
    .text(function (d) { return d.value; });
}
