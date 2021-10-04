// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })

Cypress.Commands.add('login', () => {
	// sets mobile Viewport
	cy.viewport(320, 480);
	// visit the log in page
	cy.visit('/').get('.hamburger-box').click().get('nav > ul > :nth-child(3) > a').click();
	// log in
	cy.get('#username')
		.type('Cypress')
		.get('#password')
		.type('password{enter}')
		.url()
		.should('contain', '/account');
});

//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
