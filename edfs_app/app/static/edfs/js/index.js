// Form AJAX
$('#form').on('submit', function(e){
   e.preventDefault();
   $.ajax({
        type : "POST",
        url: "/form_ajax/",
        data: {
           command_input : $('#command_input').val(),
           type : $('#type').val(),
         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
         dataType: "json",
        },
 
        success: function(data){
           //call message ajax endpoint
           message_ajax(data.command_input, data.type)
        },
        error: function(errorMessage) {
             console.log(errorMessage)
        }
    });
 });
 
 // Message AJAX
 function message_ajax(command_input, type){
     $.ajax({
        type : "POST",
        url: "/message_ajax/",
        data: {
           command_input: command_input,
           type: type,
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

