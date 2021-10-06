describe('Tests the contact Page', () => {
	beforeEach(() => {
		cy.visit('/contact');
	});

	it('Requires name', () => {
		cy.get('#send')
			.click()
			.get('#fullName')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('Requires email', () => {
		cy.get('#fullName')
			.type('Cypress Test')
			.get('#send')
			.click()
			.get('#emailAddress')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('Requires message', () => {
		cy.get('#fullName')
			.type('Cypress Test')
			.get('#emailAddress')
			.type('cypress.com')
			.get('#send')
			.click()
			.get('#subject')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('Requires real email', () => {
		cy.get('#fullName')
			.type('Cypress Test')
			.get('#emailAddress')
			.type('cypress.com')
			.get('#subject')
			.type('hello')
			.get('#send')
			.click()
			.get('#emailAddress')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('Sends an email', () => {
		cy.get('#fullName')
			.type('Cypress Test')
			.get('#emailAddress')
			.type('cypress@icloud.com')
			.get('#subject')
			.type('This is email will succeed in sending')
			.get('#send')
			.click()
			.get('#sucess > .modal > .modal-content > .modal-par > p')
			.should('be.visible');
	});
});
