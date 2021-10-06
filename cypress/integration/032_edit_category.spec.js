describe('Edit the Category', () => {
	beforeEach(() => {
		cy.login();
	});

	it('Adds a New Task with New category', () => {
		cy.get(':nth-child(6) > .section-header').click().get('.card-action > .edit').click();
		cy.get('#task_category').type('- Edited');
		cy.get('#submit_button').click();
		cy.get('.error-messages > li')
			.should('contain', 'Category must be between 4 and 20 characters')
			.get('#task_category')
			.type(
				'{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace}{backspace} Edited Category {enter}'
			)
			.get('section > .modal-background > .modal')
			.should('contain', 'Category Successfully Updated');
		cy.get('section > .modal-background').click();
	});
});
