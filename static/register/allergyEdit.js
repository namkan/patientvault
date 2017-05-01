// Wait for the DOM to be ready
// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#allergyedit").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      substance: "required",
      category1 : "required",
      serverity1: "required",
      
      // email: {
      //   required: false,
      //   // Specify that email should be validated
      //   // by the built-in "email" rule
      //   email: true,
      // },
     
      
    },
    // Specify validation error messages
    messages: {
      substance: "Please enter any substance!!",
      category1 : "Please choose any category!!",
      serverity1:"Plese choose an effect!!",
      
      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
