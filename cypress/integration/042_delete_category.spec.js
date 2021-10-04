describe('Deletes the Category', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Cancel Deletes category', () => {
		cy.get(':nth-child(6) > .section-header')
			.click()
			.get('.delete')
			.click()
			.get('#cancel_button')
			.click()
			.get('#burger-btn')
			.click()
			.get('ul > :nth-child(2) > a')
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
