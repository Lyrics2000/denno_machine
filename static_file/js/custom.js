$(function(){
	$("#webticker").webTicker();
	$("#webtickers").webTicker({duplicate:true, speed: 50, direction: 'right', rssurl:'http://yourwebsite.com/rss/', rssfrequency:1, startEmpty:false, hoverpause:true});	
	
	
});
$( document ).ready(function() {
	$('#tabs li' ).click(function() {
	$('#tabs li' ) .children('.flow') .hide();
	$(this) .find('a#comment').append('<div class="flow" style="width:125px;"></div>');
	$(this) .append('<div class="flow"></div>');
	});
	
	$('#element').tooltip('show')
	
	
			$( '.ser1').hover(function(e) {
			  $(this) .children('h2') .css({ "background": "url('images/services-icon_03.png') no-repeat scroll 0 0 transparent", "color":"#bccf02"
            });        
			$(this) .children('.read-more') .css({ "background": "url('images/green-red-more_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  }, function(e) {
				   $(this) .children('h2') .css({ "background": "url('images/service-icon-hover_03.png') no-repeat scroll 0 0 transparent", "color":"#666666"
            });  
			$(this) .children('.read-more') .css({ "background": "url('images/readmore_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  });
			  
			$( '.ser2').hover(function(e) {
			  $(this) .children('h2') .css({ "background": "url('images/services-icon-hover2_03.png') no-repeat scroll 0 0 transparent", "color":"#bccf02"
            });        
			$(this) .children('.read-more') .css({ "background": "url('images/green-red-more_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  }, function(e) {
				   $(this) .children('h2') .css({ "background": "url('images/service-icon2_03.png') no-repeat scroll 0 0 transparent", "color":"#666666"
            });  
			$(this) .children('.read-more') .css({ "background": "url('images/readmore_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  });
			  
			  
			$( '.ser3').hover(function(e) {
			  $(this) .children('h2') .css({ "background": "url('images/sservice-icon3-hover_03.png') no-repeat scroll 0 0 transparent", "color":"#bccf02"
            });        
			$(this) .children('.read-more') .css({ "background": "url('images/green-red-more_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  }, function(e) {
				   $(this) .children('h2') .css({ "background": "url('images/service-icon3_03.png') no-repeat scroll 0 0 transparent", "color":"#666666"
            });  
			$(this) .children('.read-more') .css({ "background": "url('images/readmore_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  });
			  
			  
			$( '.ser4').hover(function(e) {
			  $(this) .children('h2') .css({ "background": "url('images/services-icon4-hover_03.png') no-repeat scroll 0 0 transparent", "color":"#bccf02"
            });        
			$(this) .children('.read-more') .css({ "background": "url('images/green-red-more_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  }, function(e) {
				   $(this) .children('h2') .css({ "background": "url('images/services-icon4_03.png') no-repeat scroll 0 0 transparent", "color":"#666666"
            });  
			$(this) .children('.read-more') .css({ "background": "url('images/readmore_03.png') no-repeat scroll 0 0 transparent", "background-position":"right center"
			});
			
			
			  });
			  
			  
			  
			  $( '.post-image').hover(function(e) {
				  
			  $(this) .children('.type-icon') .show();
			   $(this) .children('.stars-img') .show();
			
			
			
			  }, function(e) {
				  $(this) .children('.type-icon') .hide();
			   $(this) .children('.stars-img') .hide();
						
			
			  });
			  
			  
			  
	
});
$(function() {
    $('.accordion-heading').click(function(e) {
        if ($(this).hasClass("ac-act")) {
				   $('.accordion-heading').removeClass("ac-act").addClass("ac-dis");
				  $this.removeClass("ac-act").addClass("ac-dis");
				  
				  return;
			   }
		if ($(this).hasClass("ac-dis")) {
				$('.accordion-heading').removeClass("ac-act").addClass("ac-dis");
				  $(this).removeClass("ac-dis").addClass("ac-act");
				  return;
			   }
	});
});  
		  
