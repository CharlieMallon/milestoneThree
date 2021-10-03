describe('The Accounts Page', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Cancels Delete Task', () => {
		cy.get('.mobile-nav > h1 > a').click().get('.small-screen > .task > :nth-child(1)').click();
		cy.get(
			'.open > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img'
		).click();
		cy.get(
			'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-title > h2'
		).should('contain', 'Delete Task');
		cy.get('#cancel_button').click();
		cy.get('.small-screen > .task').children().should('have.length', 4);
	});

	it('Delete Task on Home Page', () => {
		cy.get('.mobile-nav > h1 > a')
			.click()
			.get('.small-screen > .task > :nth-child(3)')
			.click()
			.get('.open > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img')
			.click()
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-title > h2'
			)
			.should('contain', 'Delete Task')
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('.small-screen > .task')
			.children()
			.should('have.length', 3)
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Deleted')
			.get('section > .modal-background')
			.click();
	});

	it('Delete Task on Account Page - To Do Today', () => {
		cy.get(':nth-child(4) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > .large > .task-header > .task-header-internal > .task-name > strong > .shave-me'
			)
			.click()
			.get('.open > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img')
			.click()
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-title > h2'
			)
			.should('contain', 'Delete Task')
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Deleted')
			.get('section > .modal-background')
			.click()
			.get(':nth-child(4) > .section-header > :nth-child(2) > p > .section-arrow')
			.click()
			.get('.open > .section-content')
			.should('contain', 'No Tasks Found');
	});

	it('Delete Task on Account Page - Other Tasks', () => {
		cy.get(':nth-child(5) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > .large > .task-header > .task-header-internal > .task-name > strong > .shave-me'
			)
			.click()
			.get('.open > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img')
			.click()
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-title > h2'
			)
			.should('contain', 'Delete Task')
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Deleted')
			.get('section > .modal-background')
			.click()
			.get(':nth-child(5) > .section-header > :nth-child(2) > p > .section-arrow')
			.click()
			.get('.open > .section-content')
			.should('contain', 'No Tasks Found');
	});

	it('Delete Task on Account Page - Done Tasks', () => {
		cy.get(':nth-child(3) > .section-header')
			.click()
			.get('.open > .section-content > .task > .task-header')
			.click()
			.get('.open > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img')
			.click()
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-title > h2'
			)
			.should('contain', 'Delete Task')
			.get(
				'.open > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Deleted')
			.get('section > .modal-background')
			.click()
			.get(':nth-child(3) > .section-header > :nth-child(2) > p > .section-arrow')
			.click()
			.get('.open > .section-content')
			.should('contain', 'No Tasks Found');
	});
});
