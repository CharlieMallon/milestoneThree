describe('The Accounts Page', () => {
	beforeEach(() => {
		cy.login();
	});

	it('greets with Username', () => {
		cy.get('.header').should('contain', 'Cypress');
	});
});
