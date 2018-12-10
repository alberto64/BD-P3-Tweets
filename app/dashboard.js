/**
 * Created by manuel on 5/8/18.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart', 'bar', 'table']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawModelTotalChart);
google.charts.setOnLoadCallback(drawModel1TotalChart);
google.charts.setOnLoadCallback(drawModel2TotalChart);
google.charts.setOnLoadCallback(drawModel3TotalChart);

function drawModelTotalChart() {
    var allText = "Model1\t0.7594369803570206\nModel2\t0.753678822852981\nModel3\t0.767754318503638"

    console.log(allText);

    var allTextLines = allText.split("\n");
    console.log(allTextLines);
    var arrayData = [];
    for (var j=0; j<allTextLines.length; j++) {
            var row = allTextLines[j].split("\t");
            arrayData.push([row[0], parseFloat(row[1], 10)*100]);
    }

    console.log(arrayData);

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Models');
    data.addColumn('number', 'Accuracy Percentage');
    data.addRows(arrayData);

    var options = {
        title: 'Accuracy Percentage Between All Models',
        chartArea: {width: '800px'},
        hAxis: {
            title: 'Accuracy Percentage',
            minValue: 0,
            maxValue: 100
        },
        vAxis: {
            title: 'Models'
        }
    };

    var chart = new google.charts.Bar(document.getElementById('totalModelCount'));

    chart.draw(data, options);
}

function drawModel1TotalChart() {
   var allText = "0-No Medical Relation\t868\n1-Medical Relation\t2238\n2-Ambiguous\t20"

    console.log(allText);

    var allTextLines = allText.split("\n");
    console.log(allTextLines);
    var arrayData = [];
    for (var j=0; j<allTextLines.length; j++) {
            var row = allTextLines[j].split("\t");
            arrayData.push([row[0], parseInt(row[1], 10)]);
    }

    console.log(arrayData);

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Models');
    data.addColumn('number', 'Accuracy Percentage');
    data.addRows(arrayData);


    var options = {
      title: 'Total Tweets Per Categorization'
    };

    var chart = new google.visualization.PieChart(document.getElementById('totalModel1Count'));

    chart.draw(data, options);
}

function drawModel2TotalChart() {

      var allText = "0-No Medical Relation\t780\n1-Medical Relation\t2315\n2-Ambiguous\t31"

    console.log(allText);

    var allTextLines = allText.split("\n");
    console.log(allTextLines);
    var arrayData = [];
    for (var j=0; j<allTextLines.length; j++) {
            var row = allTextLines[j].split("\t");
            arrayData.push([row[0], parseInt(row[1], 10)]);
    }

    console.log(arrayData);

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Models');
    data.addColumn('number', 'Accuracy Percentage');
    data.addRows(arrayData);


    var options = {
      title: 'Total Tweets Per Categorization'
    };

    var chart = new google.visualization.PieChart(document.getElementById('totalModel2Count'));

    chart.draw(data, options);
}

function drawModel3TotalChart() {

      var allText = "0-No Medical Relation\t868\n1-Medical Relation\t2238\n2-Ambiguous\t20"

    console.log(allText);

    var allTextLines = allText.split("\n");
    console.log(allTextLines);
    var arrayData = [];
    for (var j=0; j<allTextLines.length; j++) {
            var row = allTextLines[j].split("\t");
            arrayData.push([row[0], parseInt(row[1], 10)]);
    }

    console.log(arrayData);

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Models');
    data.addColumn('number', 'Accuracy Percentage');
    data.addRows(arrayData);


    var options = {
      title: 'Total Tweets Per Categorization'
    };

    var chart = new google.visualization.PieChart(document.getElementById('totalModel3Count'));

    chart.draw(data, options);
}