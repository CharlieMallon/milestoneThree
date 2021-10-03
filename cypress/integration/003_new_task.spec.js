describe('The Accounts Page', () => {
	beforeEach(() => {
		cy.login().get('.add').click();
	});

	it('Cancels create new Task', () => {
		cy.get('#cancel_button').click().url().should('contain', '/home');
	});

	it('Requires a task name', () => {
		cy.get('#submit_button')
			.click()
			.get('#task_name')
			.then(($el) => $el[0].checkValidity())
			.should('be.false');
	});

	it('Adds a Task with only a Task Name', () => {
		cy.get('#task_name')
			.type('Test task one')
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Added');
		cy.get('section > .modal-background')
			.click()
			.get('.small-screen > .task')
			.should('contain', 'Test task one')
			.get('.small-screen > .task > .task-card > .task-header > .task-header-internal')
			.click()
			.get('.small-screen > .task > :nth-child(1)')
			.should('have.class', 'small')
			.should('have.class', 'open')
			.should('contain', 'No Category')
			.should('contain', 'No Due Date')
			.get(
				'.small-screen > .task > .task-card > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.invoke('attr', 'src')
			.should('include', 'check-box-empty');
	});

	it('Adds a Task with All task details', () => {
		cy.get('#task_name')
			.type(
				'Test task two - the long one to check that shave works, it needs to be quite long!'
			)
			.get('#task_description')
			.type('This is another test task')
			.get('#is_priority')
			.check()
			.get('#due_date')
			.type('2021-10-10')
			.get('#task_size-1')
			.click()
			.get('#task_category')
			.select('Coding')
			// This bit is broken!
			// .get('#is_done')
			// .check()
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Added');
		cy.get('section > .modal-background')
			.click()
			.get('.small-screen > .task')
			.should('contain', 'Test task two')
			.get(
				'.small-screen > .task > :nth-child(1) > .task-header > .task-header-internal > .buttons > .arrow'
			)
			.click()
			.get('.small-screen > .task > :nth-child(1)')
			.should('have.class', 'medium')
			.should('have.class', 'open')
			.should('contain', 'Coding')
			.should('contain', 'Due by: 2021-10-10')
			.get(
				'.small-screen > .task > .task-card > .task-body > :nth-child(1) > .priority > .check-box > img'
			)
			.invoke('attr', 'src')
			.should('include', 'check-box-full');
	});

	it('Adds a New Task with New category', () => {
		cy.get('#task_name')
			.type('Test task three')
			.get('#task_description')
			.type('A description of the task goes here is can be quite long! ')
			.get('#task_size-2')
			.click()
			.get('p')
			.contains('Add new category')
			.click()
			.get('#add_category')
			.type('Test Category One')
			.get('#submit_button')
			.click()
			.get('section > .modal-background > .modal > .modal-content > .modal-par')
			.should('contain', 'Task Successfully Added');
		cy.get('section > .modal-background')
			.click()
			.get('.small-screen > .task')
			.should('contain', 'Test task three')
			.get('.small-screen > .task > :nth-child(3)')
			.click()
			.should('contain', 'Test category one');
	});
});
