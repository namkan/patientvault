// Wait for the DOM to be ready
// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#personal_info").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
     
      first_name : "required",
      last_name: "required",
      genders: "required",
      country: "required",
      state: "required",
      city: "required",
      address: "required",
      // email: {
      //   required: false,
      //   // Specify that email should be validated
      //   // by the built-in "email" rule
      //   email: true,
      // },
     
      
    },
    // Specify validation error messages
    messages: {
      first_name: "Please enter First Name!!",
      last_name : "Please enter Last Name!!",
      genders:"Plese select Gender!!",
      country:"Please give Country Name!!",
      state:"Please give State Name!!",
      city:"Please give City Name!!",
      address:"Please give Your address!!",
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
