// Form AJAX
$('#form').on('submit', function(e){
    e.preventDefault();
    $.ajax({
         type : "POST",
         url: "/form_ajax/",
         data: {
            command_input : $('#command_input').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
  
         success: function(data){
            $('#output1').html(data.msg)
            //call message ajax endpoint
            message_ajax(data.command_input)
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
     });
  });
  
  // Message AJAX
  function message_ajax(command_input){
      $.ajax({
         type : "POST",
         url: "/message_ajax/",
         data: {
            command_input: command_input,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          dataType: "json",
         },
         success: function(data){
            $('#output2').html(data.rendered_data)
         },
         error: function(errorMessage) {
              console.log(errorMessage)
         }
      });
  }