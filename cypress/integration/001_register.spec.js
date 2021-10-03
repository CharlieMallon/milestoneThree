describe('The Accounts Page', () => {
	beforeEach(() => {
		// sets mobile Viewport
		cy.viewport(320, 480);
		// visit the log in page
		cy.visit('/').get('.hamburger-box').click().get('nav > ul > :nth-child(2) > a').click();
	});

	it('greets with Register', () => {
		cy.get('h2').should('contain', 'Register');
	});

	it('links to /login', () => {
		cy.contains('Have an account?').should('have.attr', 'href', '/login');
	});

	it('has a back button', () => {
		cy.contains('Cancel').click().url().should('contain', '/home');
	});

	it('requires username', () => {
		cy.get('form')
			.contains('Register')
			.click()
			.get('#username')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('requires password', () => {
		cy.get('#username')
			.type('CypressTestUser')
			.get('form')
			.contains('Register')
			.click()
			.get('#password')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('requires confirmation of password', () => {
		cy.get('#username')
			.type('CypressTestUser')
			.get('#password')
			.type('password')
			.get('form')
			.contains('Register')
			.click()
			.get('#confirm_password')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('requires matching passwords', () => {
		cy.get('#username')
			.type('CypressTestUser')
			.get('#password')
			.type('password')
			.get('#confirm_password')
			.type('password-two')
			.get('form')
			.contains('Register')
			.click();
	});

	it('requires a new username', () => {
		cy.get('#username')
			.type('CypressTestUser')
			.get('#password')
			.type('password')
			.get('#confirm_password')
			.type('password{enter}')
			.get('.modal-par')
			.should('contain', 'Username already exists');
	});
});
