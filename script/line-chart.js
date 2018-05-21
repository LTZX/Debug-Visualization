var widthl = $("#exTab2").width() * 0.8;
var heightl = $("#exTab2").height() * 0.75;
const marginl = { top: 20, right: 50, bottom: 30, left: 50 };

const parseTime = d3.timeParse('%d-%b-%y');
const bisectDate = d3.bisector(d => d.date).left;
const formatValue = d3.format(',.2f');
const formatCurrency = d => `$${formatValue(d)}`;

const xl = d3.scaleTime()
  .range([0, widthl]);

const yl = d3.scaleLinear()
  .range([heightl, 0]);

const line = d3.line()
  .x(d => xl(d.date))
  .y(d => yl(d.close));

const svgl = d3.select('#line-chart').append('svg')
  .attr('width', widthl + marginl.left + marginl.right)
  .attr('height', heightl + marginl.top + marginl.bottom)
  .append('g')
    .attr('transform', `translate(${marginl.left}, ${marginl.top})`);

d3.tsv('data/line-chart.tsv', type, (error, data) => {
  if (error) throw error;

  data.sort((a, b) => a.date - b.date);

  xl.domain([data[0].date, data[data.length - 1].date]);
  yl.domain(d3.extent(data, d => d.close));

  svgl.append('g')
    .attr('class', 'x axis axis--x')
    .attr('transform', `translate(0, ${heightl})`)
    .call(d3.axisBottom(xl));

  svgl.append('g')
    .attr('class', 'y axis axis--y')
    .call(d3.axisLeft(yl))
    .append('text')
      .attr('class', 'axis-title')
      .attr('transform', 'rotate(-90)')
      .attr('y', 6)
      .attr('dy', '.71em')
      .style('text-anchor', 'end')
      .text('Price ($)');

  // style the axes
  d3.selectAll('.axis path')
    .styles({
      fill: 'none',
      stroke: '#000',
      'shape-rendering': 'crispEdges'
    });

  d3.selectAll('.axis line')
    .styles({
      fill: 'none',
      stroke: '#000',
      'shape-rendering': 'crispEdges'
    });

  svgl.append('path')
    .datum(data)
    .attr('class', 'line')
    .attr('d', line);

  const focus = svgl.append('g')
    .attr('class', 'focus')
    .style('display', 'none');

  focus.append('circle')
    .attr('r', 4.5);

  focus.append('line')
    .classed('x', true);

  focus.append('line')
    .classed('y', true);

  focus.append('text')
    .attr('x', 9)
    .attr('dy', '.35em');

  svgl.append('rect')
    .attr('class', 'overlay')
    .attr('width', widthl)
    .attr('height', heightl)
    .on('mouseover', () => focus.style('display', null))
    .on('mouseout', () => focus.style('display', 'none'))
    .on('mousemove', mousemove);

  d3.selectAll('.line')
    .styles({
      fill: 'none',
      stroke: 'steelblue',
      'stroke-width': '1.5px'
    });

  d3.select('.overlay')
    .styles({
      fill: 'none',
      'pointer-events': 'all'
    });

  d3.selectAll('.focus')
    .style('opacity', 0.7);

  d3.selectAll('.focus circle')
    .styles({
      fill: 'none',
      stroke: 'black'
    });

  d3.selectAll('.focus line')
    .styles({
      fill: 'none',
      'stroke': 'black',
      'stroke-width': '1.5px',
      'stroke-dasharray': '3 3'
    });

  function mousemove() {
    const x0 = xl.invert(d3.mouse(this)[0]);
    const i = bisectDate(data, x0, 1);
    const d0 = data[i - 1];
    const d1 = data[i];
    const d = x0 - d0.date > d1.date - x0 ? d1 : d0;
    focus.attr('transform', `translate(${xl(d.date)}, ${yl(d.close)})`);
    focus.select('line.x')
      .attr('x1', 0)
      .attr('x2', -xl(d.date))
      .attr('y1', 0)
      .attr('y2', 0);

    focus.select('line.y')
      .attr('x1', 0)
      .attr('x2', 0)
      .attr('y1', 0)
      .attr('y2', heightl - yl(d.close));

    focus.select('text').text(formatCurrency(d.close));
  }
});

function type(d) {
  d.date = parseTime(d.date);
  d.close = +d.close;
  return d;
}
