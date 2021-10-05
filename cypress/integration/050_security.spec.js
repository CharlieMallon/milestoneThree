describe('Security', () => {
	it('tries to access a Task', () => {
		cy.visit('/edit_task/615c76092b0f4fbf4afb7f63', { failOnStatusCode: false });
	});
});
