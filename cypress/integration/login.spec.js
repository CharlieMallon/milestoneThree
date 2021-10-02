describe('The login Page - functionality', () => {
    beforeEach(() => {
        cy.viewport(320, 480)
        cy
            .visit('/')
            .get('.hamburger-box').click()
            .get('nav > ul > :nth-child(3) > a').click();
    })

    it('greets with Sign In', () => {
        cy.get('h2').contains('Log In');
    })

    it('links to /register', () => {
        cy
            .contains('Need an account?')
            .should('have.attr', 'href', '/register');
    })

    it('has a back button', () => {
        cy
            .contains('Cancel').click()
            .url().should('contain', '/home')
    })

    it('requires username', () => {
        cy
            .get('form').contains('Log In').click()
            .get('#username').then($el => $el[0].checkValidity()).should('be.false');
    })

    it('requires password', () => {
        cy
            .get('#username').type('Username')
            .get('form').contains('Log In').click()
            .get('#password').then($el => $el[0].checkValidity()).should('be.false');
    })

    it('requires valid username and password', () => {
        cy
            .get('#username').type('CypressTestUser')
            .get('#password').type('password{enter}')
            .get('.modal-par').should('contain', 'Incorrect Username and/or Password');
    })

    it('navigates to /account on successful Sign In', () => {
        cy
        .get('#username').type('CypressTestUser')
        .get('#password').type('CypressTestUserPassword{enter}')
        .url().should('contain', '/account')
    })
})
