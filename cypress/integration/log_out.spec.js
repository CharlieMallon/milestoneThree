describe('Log Out', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Logs Out on Mobile', () => {
		cy.get('.hamburger-box')
			.click()
			.get('nav > ul > :nth-child(3) > a')
			.click()
			.url()
			.should('contain', '/home');
	});

	it('Logs Out on Desktop', () => {
		cy.viewport(992, 600);
		cy.get('.desktop-nav > ul > :nth-child(3)').click().url().should('contain', '/home');
	});
});
