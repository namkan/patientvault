$(function(){
	$('#form1').validate({
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
			city:"Please enter city name",
		},
	});
});