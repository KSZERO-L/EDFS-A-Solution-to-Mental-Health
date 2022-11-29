// Form AJAX
$('#form3').on('submit', function(e){
    console.log("IN there")
    e.preventDefault();
    $.ajax({
         type : "POST",
         url: "/form_ajax3/",
         data: {
            q : $('#q').val(),
            type : $('#type').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
  
         success: function(data){
            //call message ajax endpoint
            console.log("Success")
            message_ajax3(data.q, data.type)
            $("#q").val("");
            $("#type").val("");
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
     });
  });
  
  // Message AJAX
  function message_ajax3(q, type){
      $.ajax({
         type : "POST",
         url: "/message_ajax3/",
         data: {
            q: q,
            type: type,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
         success: function(data){
            if (q == "q1"){
               q1(data)
            }
            if (q == "q2"){
               q2(data)
            }
            if (q == "q3"){
               q3(data)
            }
            if (q == "q4"){
               q4(data)
            }
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
      });
  }

  function q1(send) {

   var data = send.replace(/'/g, '"');
   data = JSON.parse(data)
   var len = data.length

   var X = []
   var Y =[]

   var i;
   for (i = 0; i < len; i++) {
      X.push(data[i]['Country'])
      Y.push(data[i]['Prevalence'])
   }
   var data = [
      {
        x: X,
        y: Y,
        marker:{
         color: ['rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)',
         'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)']
       },
        type: 'bar'
      }
    ];
    var layout = {
      autosize: false,
      width: 1100,
      height: 500,
      title: 'Country vs Prevalence',
      xaxis: {
         title: 'Country',
       },
       yaxis: {  
         title: 'Prevalence',
       }
    };
    Plotly.newPlot('output4', data, layout);
   } 


   function q2(send) {

      var data = send.replace(/'/g, '"');
      data = JSON.parse(data)
      var len = data.length
   
      var X = []
      var Y =[]
      var Z = []
   
      var i;
      for (i = 0; i < len; i++) {
         X.push(data[i]['Country'])
         Y.push(data[i]['Psychiatrists'])
         Z.push(data[i]['Psychologists'])
      }
      var trace1 = {
         x: X,
         y: Y,
         name: "Psychiatrists",
         type: 'bar',
         marker: {
            color: 'rgb(158,202,225)',    
            line: {  
              color: 'rgb(8,48,107)',
              width: 1.5
            }
          }
       };
       var trace2 = {
         x: X,
         y: Z,
         name: "Psychologists",
         type: 'bar',
         marker: {
            color: 'rgba(58,200,225,.5)',
            line: {
              color: 'rgb(8,48,107)',
              width: 1.5
            }
          }
       };
       var data = [trace1, trace2];
       var layout = {
         autosize: false,
         width: 1100,
         height: 500,
         title: 'Number of Psychiatrists and Psychologists in various countries',
         xaxis: {
            title: 'Country',
          },
          yaxis: {  
            title: 'Category',
          }
       };
       Plotly.newPlot('output4', data, layout);
      } 

   function q3(send) {

      var data = send.replace(/'/g, '"');
      data = JSON.parse(data)
   
      var X = ["Maybe", "No", "Yes"]
      var Y =[data["Maybe"], data["No"], data["Yes"]]

      var data = [{
         values: Y,
         labels: X, 
         marker:{
            colors: ['rgba(222,45,38,0.8)', 'rgb(11, 133, 215)', 'rgb(118, 17, 195)']
          },
         type: 'pie',
         sort: false
       }];

      var layout = {
      autosize: false,
      width: 1100,
      height: 500,
      title: 'Composition of Mental Health Consequence',
      xaxis: {
         title: 'Mental Health Consequence',
         },
         yaxis: {  
         title: 'Count',
         }
      };
      Plotly.newPlot('output4', data, layout);
   } 


   function q4(send) {

      var data = send.replace(/'/g, '"');
      data = JSON.parse(data)
      var len = data.length
   
      var X = []
      var Y =[]
   
      var i;
      for (i = 0; i < len; i++) {
         X.push(data[i]['Country'])
         Y.push(data[i]['Happiness Score'])
      }
      var data = [
         {
           x: X,
           y: Y,
           marker:{
            color: ['rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)',
            'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)', 'rgba(222,45,38,0.8)']
          },
           type: 'bar'
         }
       ];
       var layout = {
         autosize: false,
         width: 1100,
         height: 500,
         title: 'Country vs Happiness Score for 2018',
         xaxis: {
            title: 'Country',
          },
          yaxis: {  
            title: 'Happiness Score',
          }
       };
       Plotly.newPlot('output4', data, layout);
      } 