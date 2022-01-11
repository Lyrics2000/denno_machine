jQuery(document).ready(function(){
								
jQuery('#style-switch').animate({left:-212});
		
jQuery('#t-row-left-ss').animate({left:0});

var selector = 1;

jQuery('#t-row-left-ss').click(function(){
										
	if (selector == 1) {
	
	jQuery('#style-switch').animate({left:0});
		
	jQuery('#t-row-left-ss').animate({left:212});
	
	$(".color-square").click(function(){
    		var id = $(this).attr("data-col");
    		
    		$("#switch_style").attr("href","css/" + id + ".css");    		
    	});

	
	selector = 0;
	
	}
	else {
		
		jQuery('#style-switch').animate({left:-212});
		
	jQuery('#t-row-left-ss').animate({left:0});
		
		selector = 1;
		}
		
		
});


});
