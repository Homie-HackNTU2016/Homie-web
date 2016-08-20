'use strict'

;(function(document, window, index) {
	$(".button-collapse").sideNav();
	$('.modal-trigger').leanModal();

	var searchField = $('#search');
	searchField.focus(function() {
		if (window.innerWidth < 680) {
			$('.button-collapse').animate({ opacity: '0' });
			$('.brand-logo').css('display', 'none');
			$('.search-wrapper').animate({ paddingLeft: '0px'});
			$('.main-content').animate({
				paddingTop: '+50px'
			}, 300, function() {
				$('#search').css({
					'color':'black',
					'background-color': 'white'
				});
			});
		}
	});

	searchField.blur(function() {
		$(this).val('');
		if (window.innerWidth < 680) {
			$('.button-collapse').animate({ opacity: '1' });
			$('.brand-logo').css('display', 'block');
			$('.search-wrapper').animate({ paddingLeft: '+=280px'});
			$('.main-content').animate({
				paddingTop: '-=50px'
			}, 300, function() {
				$('#search').css({
					'color':'white',
					'background-color': 'transparent'
				});
			});
		}
	});



}(document, window, 0));
