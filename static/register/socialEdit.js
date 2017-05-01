// Wait for the DOM to be ready
// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#social1").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      alcohol_usage: "required",
      drinks : "required",
      tobaco_usage: "required",
      tobaco_quit_date: "required",
      drug_usage: "required",
      drug_details: "required",


      // email: {
      //   required: false,
      //   // Specify that email should be validated
      //   // by the built-in "email" rule
      //   email: true,
      // },
     
      
    },
    // Specify validation error messages
    messages: {
      alcohol_usage: "Please enter Alcohol Usage!!",
      drinks : "Please enter drinks!!",
      tobaco_usage:"Please enter tobaco usage!",
      tobaco_quit_date:"Please give details!!",
      drug_usage:"Plese enter drug_usage!!",
      drug_details:"Please enter drug details!!",
      
    
      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
