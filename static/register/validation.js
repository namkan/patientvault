// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#registration").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      first_name: "required",
      last_name : "required",
      email: {
        required: false,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true,
      },
      mobile_number: {
        required: true,
        maxlength: 10,
        minlength: 10,
        
      },
      password: {
        required: true,
        minlength: 5,
      },
      cpassword: {
        required: true,
        equalTo: "#password",
      },
    },
    // Specify validation error messages
    messages: {
      first_name: "Please enter your first name!!",
      last_name : "Please enter your last name!!",
      email: {
        email: "Please enter a valid email address!!",
       }, 
      mobile_number: {
        required: "Please enter phone number",
        maxlength: "Please enter a valid phone number!!",
        minlength: "Please enter a valid phone number!!",
        
      },
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 5 characters long",
      },
      cpassword: {
        required: "Please confirm your password!!",
        equalTo : "password must be same",
      },
      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
