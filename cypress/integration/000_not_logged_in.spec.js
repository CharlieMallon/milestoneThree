describe('Not Logged In', () => {
	beforeEach(() => {
		cy.visit('/');
	});

	it('Landing page successfully loads', () => {
		cy.get('.desktop-nav > ul > :nth-child(1) > a')
			.click()
			.url()
			.should('contain', '/')
			.viewport(320, 480);
		cy.screenshot('landing_page_mobile').viewport(568, 320);
		cy.screenshot('landing_page_mobile_landscape').viewport(768, 1024);
		cy.screenshot('landing_page_tablet').viewport(992, 768);
		cy.screenshot('landing_page_desktop').viewport(1200, 900);
		cy.screenshot('landing_page_large_desktop');
	});

	it('Register page successfully loads', () => {
		cy.get('.desktop-nav > ul > :nth-child(2) > a')
			.click()
			.url()
			.should('contain', '/register')
			.viewport(320, 480);
		cy.screenshot('register_page_mobile').viewport(568, 320);
		cy.screenshot('register_page_mobile_landscape').viewport(768, 1024);
		cy.screenshot('register_page_tablet').viewport(992, 768);
		cy.screenshot('register_page_desktop').viewport(1200, 900);
		cy.screenshot('register_page_large_desktop');
	});

	it('Login page successfully loads', () => {
		cy.get('.desktop-nav > ul > :nth-child(3) > a')
			.click()
			.url()
			.should('contain', '/login')
			.viewport(320, 480);
		cy.screenshot('login_page_mobile').viewport(568, 320);
		cy.screenshot('login_page_mobile_landscape').viewport(768, 1024);
		cy.screenshot('login_page_tablet').viewport(992, 768);
		cy.screenshot('login_page_desktop').viewport(1200, 900);
		cy.screenshot('login_page_large_desktop');
	});

	it('Contact page successfully loads', () => {
		cy.get('.desktop-nav > ul > :nth-child(4) > a')
			.click()
			.url()
			.should('contain', '/contact')
			.viewport(320, 480);
		cy.screenshot('contact_page_mobile')
			.get('.hamburger-box')
			.click()
			.get('nav > ul > :nth-child(4) > a')
			.click()
			.url()
			.should('contain', '/contact')
			.viewport(568, 320);
		cy.screenshot('contact_page_mobile_landscape').viewport(768, 1024);
		cy.screenshot('contact_page_tablet').viewport(992, 768);
		cy.screenshot('contact_page_desktop').viewport(1200, 900);
		cy.screenshot('contact_page_large_desktop');
	});
});
