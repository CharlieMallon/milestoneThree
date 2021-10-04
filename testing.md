# Testing Doc

#

## Testing strategy.

There are two types of pages on this site, the 'public' pages which are viewed by users not logged in and the 'user' pages which a log in is required for

| Public       | User            |
| ------------ | --------------- |
| Landing page | Account         |
| Register     | Home            |
| Log In       | Contact         |
| Contact      | Add Task        |
|              | Edit Task       |
|              | Delete Task     |
|              | Prioritize Task |
|              | Complete Task   |
|              | Edit Category   |
|              | Delete Category |
|              | Log Out         |

## Testing order

-   create phase;
    -   user
    -   tasks
    -   categories
        -   in new task
        -   on account page
-   edit phase;
    -   task
        -   Account
            -   To Do
            -   Other Tasks
            -   Done Tasks
        -   Home
            -   To Do
            -   Done Tasks
    -   Categories
        -   Account section only
    -   user
        -   Username
        -   Password
-   Delete Phase;
    -   Task
        -   Account
            -   To Do
            -   Other Tasks
            -   Done Tasks
        -   Home
            -   To Do
            -   Done Tasks
    -   Categories
        -   Account section only
    -   user account and all associated data

## Testing notes

5.  When no tasks planned/completed the bar should say something like 'No Tasks Prioritised'
6.  add and edit forms are not validating correctly

7.  On large screens the tasks should be split into two lists
8.  Contact form - name/email issues
9.  Due by date is backwards (2021-10-10)
10. Task name should keep the capitals the user writes (eg Test Task not Test task)

### 'New' Pages required

2.  You cannot delete your user account
3.  You cannot edit your user details (username / password)
4.  You should be able to add a category from the Account Page

### fixed bugs

1.  Nav bar links are not whole buttons - fixed!
2.  The title on the contact page is not bound - fixed!
3.  Register function doesn't load the Account Page - fixed!
4.  When No tasks are found the text needs some padding - fixed!
5.  Landing Page on mobile should have a 'log in' link in the top right corner (not just the burger icon) - fixed!
6.  Register Page is registering even when the passwords don't match! - fixed!
7.  Edit task is not re-directing to home page or account page - fixed
8.  Username can be too many characters (over two lines) which messes up the calculations on the accounts page - FIXED - forms were not validating on submission
9.  errors need rendering correctly!
10. Error Pages need more content - images?
11. Cant click 'done' on add tasks as it doesn't give a 'done-date' to the database
12. You cannot click done in edit task - patch created and issue with the form validation
13. Edit and Delete buttons switch there order, pick a consistent order! - now edit then Delete on all tasks and categories
14. done date not added when editing the priority.

### Future features

12. Boxes should turn red when required sections not filled in
