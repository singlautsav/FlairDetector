<script>
        
        
        // var barData = {labels :['AskIndia', 'Business/Finance', 'Food', 'Non-Political', 'Photography', 'Policy/Economy', 'Politics', 'Scheduled', 'Science/Technology', 'Sports', '[R]eddiquette'], datasets :[{
        //         fillColor: "rgba(151,187,205,0.2)",
        //         strokeColor: "rgba(151,187,205,1)",
        //         pointColor: "rgba(151,187,205,1)",
        //     data : {{values}}
        //     }]
        // }

        var barData = {
			labels:['AskIndia', 'Business/Finance', 'Food', 'Non-Political', 'Photography', 'Policy/Economy', 'Politics', 'Scheduled', 'Science/Technology', 'Sports', '[R]eddiquette'],
			datasets: [{
				label: 'Max # Comment',
				fillColor: "light green",
                // strokeColor: "rgba(151,187,205,1)",
                // pointColor: "rgba(151,187,205,1)",
				data: {{values}}
			}, {
				label: 'Max Upvotes',
				fillColor:"pink",
				borderWidth: 1,
				data: {{values2}}
			}]

        }
        
        var mychart = document.getElementById("chart").getContext("2d");
        steps = 5
        max = {{max}}
        // draw bar chart
        new Chart(mychart).Bar(barData, { 
            scaleOverride: true,
            scaleSteps: steps,
            scaleStepWidth: Math.ceil(max / steps),
            scaleStartValue: 0,
            scaleShowVerticalLines: true,
            scaleShowGridLines : true,
            barShowStroke : true,
            scaleShowLabels: true
        });
        </script>