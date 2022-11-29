// Form AJAX
$('#form2').on('submit', function(e){
    console.log("IN there")
    e.preventDefault();
    $.ajax({
         type : "POST",
         url: "/form_ajax2/",
         data: {
            select : $('#select').val(),
            from : $('#from').val(),
            where : $('#where').val(),
            sign : $('#sign').val(),
            value : $('#value').val(),
            type : $('#type').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
  
         success: function(data){
            //call message ajax endpoint
            console.log("Success")
            message_ajax2(data.select, data.from, data.where, data.sign, data.value, data.type)
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
     });
  });
  
  // Message AJAX
  function message_ajax2(select, from, where, sign, value, type){
      $.ajax({
         type : "POST",
         url: "/message_ajax2/",
         data: {
            select: select, 
            from: from,
            where: where,
            sign: sign,
            value: value,
            type: type,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
         success: function(data){
            $('#output3').html(data.rendered_data)
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
      });
  }