var data = {
  labels : ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sept.','Oct.','Nov.','Dec.'],
  datasets : [
    {
      label: 'Week 1',
      data: [8, 6, 5, 7, 9, 8, 1, 6, 3, 3, 8, 7]
    },
    {
      label: 'Week 2',
      data: [6, 8, 5, 6, 5, 5, 7, 0, 0, 3, 0, 7]
    },
    {
      label: 'Week 3',
      data: [8, 5, 6, 4, 2, 2, 3, 0, 2, 0, 10, 8]
    },
    {
      label: 'Week 4',
      data: [4, 0, 7, 4, 6, 3, 2, 4, 2, 10, 8, 2]
    },
    {
      label: 'Week 5',
      data: [1, 0, 0, 7, 0, 4, 1, 3, 4, 5, 1, 10]
    }
  ]
};

options = {
    // String - background color for graph
    backgroundColor: '#fff',
    // Boolean - whether each box in the dataset is outlined
    stroke: false,
    // Number - width of the outline stroke.
    strokePerc: 0.05,
    // String - the outline stroke color.
    strokeColor: "rgb(128,128,128)",
    // String - the outline stroke highlight color.
    highlightStrokeColor: "rgb(192,192,192)",
    // Boolean - whether to draw the heat map boxes with rounded corners
    rounded: true,
    // Number - the radius (as a percentage of size) of the rounded corners
    roundedRadius: 0.1,
    // Number - padding between heat map boxes (as a percentage of box size)
    paddingScale: 0.05,
    // String - "gradient", "palette"
    colorInterpolation: "gradient",
    // Array[String] - the colors used for the active color scheme.
    // Any number of colors is allowed.
    colors: [ "rgba(220,220,220,0.9)", "rgba(151,187,205,0.9)"],
    // Boolean - whether boxes change color on hover.
    colorHighlight: true, 
    // Number - a floating point value which specifies how much lighter or
    // darker a color becomes when hovered, where 1 is no change, 
    // 0.9 is slightly darker, and 1.1 is slightly lighter.
    colorHighlightMultiplier: 0.92,
    // Boolean - Whether to draw labels on the boxes
    showLabels: true, 
    // Number - the font size of the label as percentage of box height
    labelScale: 0.2,
    // String - label font family
    labelFontFamily: '"HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif',
    // String - label font style
    labelFontStyle: "normal",
    // String - label font color
    labelFontColor: "rgba(0,0,0,0.5)",
    // String - tooltipTemplate
    tooltipTemplate: "<%= xLabel %> | <%= yLabel %> : <%= value %>",
    // String - template for legend generation
    legendTemplate : '<div class="<%= name.toLowerCase() %>-legend">'+
            '<span class="<%= name.toLowerCase() %>-legend-text">'+
            '<%= min %>'+
            '</span>'+
            '<% for (var i = min; i <= max; i += (max-min)/6){ %>'+ // change 6 to number of divisions required
            '<span class="<%= name.toLowerCase() %>-legend-box" style="background-color: <%= colorManager.getColor(i).color %>;">  </span>'+
            '<% } %>'+
            '<span class="<%= name.toLowerCase() %>-legend-text">'+
            '<%= max %>'+
            '</span>'+
            '</div>'
};
var ctx = document.getElementById("activity").getContext('2d');
var newChart = new Chart(ctx).HeatMap(data, options);
