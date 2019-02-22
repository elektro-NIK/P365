function roundTo(num, n) {
    return Math.round(num*Math.pow(10,n))/Math.pow(10,n);
}

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Name');
    data.addColumn('number', 'Slices');
    data.addRows(ds);

    var options = {
        width: 250,
        height: 250,
        pieHole: 0.6,
        pieSliceText: 'none',
        pieSliceBorderColor: 'none',
        backgroundColor: 'none',
        legend: 'none',
        tooltip: {
            trigger: 'none'
        },
        colors: [
            '#E25668',
            '#E28956',
            '#E2CF56',
            '#AEE256',
            '#68E256',
            '#56E289',
            '#56E2CF',
            '#56AEE2',
            '#5668E2',
            '#8A56E2',
            '#CF56E2',
            '#E256AE'
        ]
    };

    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));

    function overHandler(x) {
        var num = data.getValue(x.row, 1);
        $('#chart_legend>ul li').eq(x.row).css('font-weight', 'Bold');
        $('#chart_label_dig').text(roundTo(num, 2));
    }

    function outHandler() {
        var sum = 0;
        for (var y = 0; y < data.getNumberOfRows(); y++)
            sum += data.getValue(y, 1);
        $('#chart_legend>ul li').css('font-weight', '');
        $('#chart_label_dig').html(roundTo(sum, 2));
    }

    google.visualization.events.addListener(chart, 'onmouseover', overHandler);
    google.visualization.events.addListener(chart, 'onmouseout', outHandler);

    outHandler();
    chart.draw(data, options);

    $('#chart_legend>ul li').each(function(index, item) {
        $(item).mouseover(function() {
            chart.setSelection([{row: index, column: null}]);
            overHandler({row: index});
        });
        $(item).mouseout(function() {
            chart.setSelection([]);
            outHandler();
        });
    });
}

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);
