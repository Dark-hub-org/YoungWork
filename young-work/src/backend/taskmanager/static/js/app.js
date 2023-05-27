// *********Модальное окно***********

document.addEventListener('DOMContentLoaded', function() {

	let btn = document.getElementById('open__model');
	let modal = document.getElementById('my__modal');
	let modalBox = document.querySelector('.modal__box');
	let btnModalClose = document.querySelector('.modal__close');

	btn.addEventListener('click', function() {
		modal.classList.add('open');

			btnModalClose.addEventListener('click', function() {
			modal.classList.remove('open');
		});
	});

	modal.addEventListener('click', (e) => {
		if(!e.target.classList.contains('modal')) {
			modal.classList.remove('open');
		}
	})

});








