describe('Register Account', () => {
	beforeEach(() => {
		cy.viewport(320, 480);
		cy.visit('/').get('.hamburger-box').click().get('nav > ul > :nth-child(2) > a').click();
	});

	it('greets with Register', () => {
		cy.get('h2').should('contain', 'Register');
	});

	it('links to /login', () => {
		cy.contains('Have an account?').should('have.attr', 'href', '/login');
	});

	it('has a back button', () => {
		cy.contains('Cancel').click().url().should('contain', '/');
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
			.type('Cypress')
			.get('form')
			.contains('Register')
			.click()
			.get('#password')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('requires confirmation of password', () => {
		cy.get('#username')
			.type('Cypress')
			.get('#password')
			.type('password')
			.get('form')
			.contains('Register')
			.click()
			.get('#confirm_password')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('requires must pass validation', () => {
		cy.get('#username')
			.type('CypressUserTooLong')
			.get('#password')
			.type('p')
			.get('#confirm_password')
			.type('pt')
			.get('form')
			.contains('Register')
			.click();
		cy.get('.register-form > :nth-child(2) > li')
			.should('contain', 'Username must be between 4 and 10 characters')
			.get('.register-form > :nth-child(4) > li')
			.should('contain', 'Password must be between 4 and 25 characters')
			.get(':nth-child(6) > li')
			.should('contain', 'Passwords must match');
	});

	it('requires a new username', () => {
		cy.get('#username')
			.type('Admin')
			.get('#password')
			.type('password')
			.get('#confirm_password')
			.type('password{enter}')
			.get('.modal-par')
			.should('contain', 'Username already exists');
	});

	it('register', () => {
		cy.get('#username')
			.type('Cypress')
			.get('#password')
			.type('password')
			.get('#confirm_password')
			.type('password{enter}')
			.url()
			.should('contain', 'cypress');
	});
});
