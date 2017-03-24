$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#login").validate({
    // Specify validation rules
    rules: {
    	username:{
    		required: true,

    	},
    	password:{
    		required: true,
    		minlength: 5,
    	},

    },
    messages: {
    	username:{
    		required: 'Please enter the User Name',
    	},
    	password:{
    		required: "Please provide a password",
        	minlength: "Your password must be at least 5 characters long",
    	},
    },
  });
});