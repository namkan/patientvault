// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#medicalmodal").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      problem: "required",
      started : "required",
      status: "required",
      // reaction_details: "required",

      // email: {
      //   required: false,
      //   // Specify that email should be validated
      //   // by the built-in "email" rule
      //   email: true,
      // },
     
      
    },
    // Specify validation error messages
    messages: {
      problem: "Please enter problem!!",
      started : "Please starting date!!",
      status:"Plese enter status!!",
      // reaction_details:"Please give details!!",
      
    
      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
