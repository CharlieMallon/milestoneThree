describe('Edit Tasks', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Cancels Edit Task from home page', () => {
		cy.get('.mobile-nav > h1 > a')
			.click()
			.get('.small-screen > .task > :nth-child(1)')
			.click()
			.get(
				'.small-screen > .task > :nth-child(1) > .task-body > :nth-child(3) > .task-buttons > .edit'
			)
			.click();
		cy.url().should('contain', '/edit_task/');
		cy.get('#cancel_button').click().url().should('contain', '/home');
	});

	it('Edits Task on account - To Do Today', () => {
		cy.get(':nth-child(4) > .section-header')
			.click()
			.get('.open > .section-content > .task > .medium > .task-header')
			.click()
			.get('.medium > .task-body > :nth-child(3) > .task-buttons > .edit')
			.click()
			.url()
			.should('contain', '/edit_task/')
			.get('#task_name')
			.type(' - edited')
			.get('#task_description')
			.type('- This task has been edited')
			.get('#is_priority')
			.click()
			.get('#due_date')
			.type('2021-10-20')
			.get('#task_size-2')
			.click()
			.get('#task_category')
			.select('Test category one')
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Updated')
			.get('section > .modal-background')
			.click()
			.url()
			.should('contain', '/home')
			.get(
				'.small-screen > .task > :nth-child(1) > .task-header > .task-header-internal > .buttons > .arrow'
			)
			.click()
			.get('.small-screen > .task > :nth-child(1)')
			.should('have.class', 'large')
			.should('have.class', 'open')
			.should('contain', 'Test category one')
			.should('contain', 'Due by: 2021-10-20')
			.get(
				'.small-screen > .task > .task-card > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.invoke('attr', 'src')
			.should('include', 'check-box-empty');
	});

	it('Edits Task on account - Other Tasks', () => {
		cy.get(':nth-child(5) > .section-header')
			.click()
			.get('.task > :nth-child(2) > .task-header')
			.click()
			.get('.open > .task-body > :nth-child(3) > .task-buttons > .edit > a > img')
			.click()
			.url()
			.should('contain', '/edit_task/')
			.get('#task_name')
			.type(' - edited')
			.get('#is_done')
			.check()
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Updated')
			.get('section > .modal-background')
			.click()
			.url()
			.should('contain', '/home')
			.get('.done > .task-header > .task-header-internal')
			.should('contain', 'task one - edited')
			.get('.done > .task-header > .done-box > .check-box > img')
			.invoke('attr', 'src')
			.should('include', 'check-box-full');
	});

	it('Completes Task on home', () => {
		cy.get('.mobile-nav > h1 > a')
			.click()
			.get(
				'.small-screen > .task > :nth-child(2) > .task-header > .done-box > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Done')
			.get('section > .modal-background')
			.click()
			.get(':nth-child(2) > .task-header > .done-box > .check-box > img')
			.get('.task > :nth-child(3)')
			.should('contain', 'Test task four')
			.get(':nth-child(3) > .task-header > .done-box > .check-box > img')
			.invoke('attr', 'src')
			.should('include', 'check-box-full');
	});

	it('Prioritizes Task on home', () => {
		cy.get('.mobile-nav > h1 > a')
			.click()
			.get('.small-screen > .task > :nth-child(2) > .task-header > .task-header-internal')
			.click()
			.get('.open > .task-body > :nth-child(1) > .priority > .check-box > img')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Prioritised')
			.get('section > .modal-background')
			.click()
			.get(
				'.small-screen > .task > :nth-child(1) > .task-header > .task-header-internal > .buttons > .exclamation'
			)
			.should('exist');
	});

	it('Completes Task on Account', () => {
		// in Completed
		cy.get(':nth-child(3) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > :nth-child(1) > .task-header > .done-box > .check-box >'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Un-done')
			.get('section > .modal-background')
			.click();
		// in To Do
		cy.get(':nth-child(4) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > .large > .task-header > .done-box > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Done')
			.get('section > .modal-background')
			.click();
		// in other
		cy.get(':nth-child(5) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > :nth-child(2) > .task-header > .done-box > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Done')
			.get('section > .modal-background')
			.click();
	});

	it('Prioritizes Task on Account', () => {
		// in Completed
		cy.get(':nth-child(3) > .section-header')
			.click()
			.get(
				'.section.open > .section-content > .task > .large > .task-header > .task-header-internal'
			)
			.click()
			.get(
				'.section.open > .section-content > .task > .large > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Un-prioritised')
			.get('section > .modal-background')
			.click();
		// in other
		cy.get(':nth-child(5) > .section-header')
			.click()
			.get(
				'.open > .section-content > .task > .large > .task-header > .task-header-internal > .buttons > .arrow'
			)
			.click()
			.get(
				'.section.open > .section-content > .task > .large > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Prioritised')
			.get('section > .modal-background')
			.click();
		// in To Do
		cy.get(':nth-child(4) > .section-header')
			.click()
			.get('.open > .section-content > .task > .large > .task-header > .task-header-internal')
			.click()
			.get(
				'.section.open > .section-content > .task > .large > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Un-prioritised')
			.get('section > .modal-background')
			.click();
	});
});
