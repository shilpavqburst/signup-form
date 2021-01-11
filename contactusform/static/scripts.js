$(document).ready( function(){
  $('#post-form').on('submit', function(event){
      event.preventDefault();

      //flag is a varible which would be used to check if there is any error. If there is
      //error it would become flase.

      var flag = true;

      var vname = $("#id_name").val();
      console.log(typeof(vname));
      var vemail = $("#id_email").val();
      var vphoneno = $("#id_phone_no").val();
      console.log(typeof(vphoneno));
      var vdescription = $("#id_description").val();

      $(".error").remove();


      //validation for name.
      if (vname.length < 1) {
          $('#id_name').after('<span class="error">**Please enter your name</span>');
          flag = false;
        }
      else {
          var nameRegEx = /[A-Za-z ]+$/;
          var validName = nameRegEx.test(vname);
          if (!validName){
              $('#id_name').after('<span class="error">**Please enter a valid name (no special characters allowed)</span>');
              flag = false;
          }
      }

      //validation for email.
      if (vemail.length < 1) {
          $('#id_email').after('<span class="error">**Please enter an Email</span>');
          flag = false;
        }
      else {
          var emailRegEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
          var validEmail = emailRegEx.test(vemail);
          if (!validEmail){
              $('#id_email').after('<span class="error">**Enter a valid email address (abc@gmail.com)');
              flag = false;
          }
      }

       //validation for phone number.
      if (vphoneno.length > 1){
         var phoneRegEx = /^[0-9]{10}$/;
         var validPhone = phoneRegEx.test(vphoneno);
         if (!validPhone){
             $('#id_phone_no').after('<span class="error">**Enter a valid 10 digit number');
             flag = false;
         }
     }

      //validation for description.
      if (vdescription.length <= 20) {
          $('#id_description').after('<span class="error">**Please enter a message not less than 20 characters</span>');
          flag = false;
      }





      if(flag){

          // ajax call
          $.ajax({
              type: "POST",
              url: "",
              data: {
                  name: $("#id_name").val(),
                  email: $("#id_email").val(),
                  phone_no: $("#id_phone_no").val(),
                  description: $("#id_description").val(),
                  csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                  action: "post",
              },
              success: function (json) {
                  document.getElementById("post-form").reset();
                  alert("Submitted Successfully !");
              },
              error: function (xhr, errmsg, err) {
                  console.log(xhr.status);
                  console.log(xhr.resposeText);
                  alert("Error !!");
              },
          });
      }
  })
});

