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
    showLabels: false,
    // Number - the font size of the label as percentage of box height
    labelScale: 0.2,
    // String - label font family
    labelFontFamily: 'monospace, sans-serif',
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

function disp_canvas() {
    let req = new XMLHttpRequest()
    req.addEventListener("load", function () {
        let resp = JSON.parse(this.responseText)
        let ctx = document.getElementById("activity").getContext('2d');
        let data = {
            labels : ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sept.','Oct.','Nov.','Dec.'],
            datasets : resp["datasets"]
        };
        var chart = new Chart(ctx).HeatMap(data, options);
    })
    req.open("GET", "/api/activity")
    req.send()
}

disp_canvas()
