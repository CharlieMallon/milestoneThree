describe('Deletes the Category', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Cancel Deletes category', () => {
		cy.get(':nth-child(6) > .section-header')
			.click()
			.get('.card-action > .open-modal > .delete > img')
			.click()
			.get('#cancel_button')
			.click()
			.get('#burger-btn')
			.click()
			.get('nav > ul > :nth-child(2) > a')
			.click();
	});

	it('Deletes category', () => {
		cy.get(':nth-child(6) > .section-header')
			.click()
			.get('.all-cats')
			.should('have.length', 1)
			.get('.delete')
			.click()
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal')
			.should('contain', 'Category Successfully Deleted');
	});
});
