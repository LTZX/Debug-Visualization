var widthp = $("#exTab1").width();
var heightp = $("#exTab1").height() - 10;
var donut = donutChart()
    .width(widthp)
    .height(heightp)
    .cornerRadius(3) // sets how rounded the corners are on each slice
    .padAngle(0.015) // effectively dictates the gap between slices
    .variable('Percentage')
    .category('Name');

//d3.tsv('data/pie-chart.tsv', function(error, data) {
    //if (error) throw error;
function drawpiechart(data){
    d3.select('#pie-chart')
        .datum(data) // bind data to the div
        .call(donut); // draw chart in div
}
//});
