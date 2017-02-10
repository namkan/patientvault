$(function(){
	$('#profile_validation').validate({
		rules:{
			country:{
				required: true,
			},
			state:{
				required: true,
			},
			city:{
				required: true,
			},
		},
		messages:{
			country:"Please enter country name",
			state:"Please enter state name",
			city:"vPlease enter city name",
		},
	});
});