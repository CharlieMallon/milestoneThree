describe('The login Page - views', () => {

    beforeEach(() => {
        cy.viewport(320, 480)
        cy
            .visit('/')
            .get('.hamburger-box').click()
            .get('nav > ul > :nth-child(3) > a').click();
    })

    it('takes a screenshot on mobile',() => {
        cy.screenshot('login-page-mobile')
        cy.viewport(480, 320)
        cy.screenshot('login-page-landscape-mobile')
    })

    it('takes a screenshot on Tablets',() => {
        cy.viewport(768, 1024)
        cy.screenshot('login-page-tablets')
        cy.viewport(1024, 768)
        cy.screenshot('login-page-landscape-tablets')
    })

    it('takes a screenshot on desktop',() => {
        cy.viewport(992, 600)
        cy.screenshot('login-page-desktop')
    })

    it('takes a screenshot on Large desktop',() => {
        cy.viewport(1200, 900)
        cy.screenshot('login-page-large-desktop')
    })

})