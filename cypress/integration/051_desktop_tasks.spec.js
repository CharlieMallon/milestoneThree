const { get } = require('http');

describe('Create, edit, complete and delete Task on desktop', () => {
	beforeEach(() => {
		cy.login().viewport(992, 768).get('.desk-nav-bar > h1 > a').click();
	});

	it('Adds tasks for rest of test', () => {
		cy.get('.add-task-btn').click();
		cy.get('#task_name')
			.type('Desktop Test task one')
			.get('#submit_button')
			.click()
			.get('section > .modal-background')
			.click();
		cy.get('.add-task-btn').click();
		cy.get('#task_name')
			.type('Desktop Test task two')
			.get('#submit_button')
			.click()
			.get('section > .modal-background')
			.click();
	});

	it('Prioritizes task two', () => {
		cy.get('.task-list > .task > :nth-child(2) > .task-header > .task-header-internal')
			.click()
			.get('.open > .task-body > :nth-child(1) > .priority > .check-box > img')
			.click()
			.get('section > .modal-background')
			.click()
			.get(
				'.task-list > .task > :nth-child(1) > .task-header > .task-header-internal > .task-name > strong > .shave-me'
			)
			.should('contain', 'two');
	});

	it('Completes task two', () => {
		cy.get(':nth-child(1) > .task-header > .done-box > .check-box > p > img')
			.click()
			.get('section > .modal-background')
			.click()
			.get('.doneSection > .main-section-content > .task-list')
			.should('have.length', 1);
	});

	it('edits task one', () => {
		cy.get(
			'.toDo > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
		)
			.click()
			.get(
				'.toDo > .main-section-content > .task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .edit > a > img'
			)
			.click()
			.get('#task_name')
			.type(' - edited {enter}')
			.get(
				'.toDo > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
			)
			.should('contain', 'edited');
	});

	it('edits done task', () => {
		cy.get(
			'.doneSection > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
		)
			.click()
			.get(
				'.doneSection > .main-section-content > .task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .edit > a > img'
			)
			.click()
			.get('#task_name')
			.type(' - edited again {enter}')
			.get(
				'.doneSection > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
			)
			.should('contain', 'edited again');
	});

	it('deletes task one', () => {
		cy.get(
			'.toDo > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
		)
			.click()
			.get(
				'.toDo > .main-section-content > .task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete'
			)
			.click()
			.get(
				'.toDo > .main-section-content > .task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('section > .modal-background')
			.click()
			.get('.toDo > .main-section-content > .task-list')
			.should('contain', 'No Tasks');
	});

	it('deletes done task', () => {
		cy.get(
			'.doneSection > .main-section-content > .task-list > .task > .task-card > .task-header > .task-header-internal'
		)
			.click()
			.get(
				'.doneSection > .main-section-content > .task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .open-modal > .delete > img'
			)
			.click()
			.get(
				'.task-list > .task > .task-card > .task-body > :nth-child(3) > .task-buttons > .modal-background > .modal > .modal-content > form > .modal-btns > :nth-child(1) > #submit_button'
			)
			.click()
			.get('section > .modal-background')
			.click()
			.get('.toDo > .main-section-content > .task-list')
			.should('contain', 'No Tasks');
	});
});
