describe('Create a Category', () => {
	beforeEach(() => {
		cy.login().get('.add').click();
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
			.get('section > .modal-background > .modal > .modal-content > :nth-child(1)')
			.should('contain', 'New Category Added')
			.get('section > .modal-background > .modal > .modal-content > :nth-child(2)')
			.should('contain', 'Task Successfully Added');
		cy.get('section > .modal-background')
			.click('right')
			.get('.small-screen > .task')
			.should('contain', 'Test task three')
			.get('.small-screen > .task > :nth-child(4)')
			.click()
			.should('contain', 'Test category one');
	});
});
