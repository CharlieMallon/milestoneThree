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
22. add and edit forms are not validating correctly

20. Edit and Delete buttons switch there order, pick a consistent order!

8.  On large screens the tasks should be split into two lists
21. Contact form - name/email issues
15. Due by sate on home - mobile is backwards (2021-10-10)
13. Task name should keep the capitals the user writes (eg Test Task not Test task)

### 'New' Pages required
2.  You cannot delete your user account
17. You cannot edit your user details (username / password)
7.  You should be able to add a category from the Account Page
### fixed bugs
1.  Nav bar links are not whole buttons - fixed!
3.  The title on the contact page is not bound - fixed!
4.  Register function doesn't load the Account Page - fixed!
6.  When No tasks are found the text needs some padding - fixed!
10. Landing Page on mobile should have a 'log in' link in the top right corner (not just the burger icon) - fixed!
16. Register Page is registering even when the passwords don't match! - fixed!
19. Edit task is not re-directing to home page or account page - fixed
11. Username can be too many characters (over two lines) which messes up the calculations on the accounts page - FIXED - forms were not validating on submission
22. errors need rendering correctly!
9.  Error Pages need more content - images?
14. Cant click 'done' on add tasks as it doesn't give a 'done-date' to the database
18. You cannot click done in edit task

### Future features
12. Boxes should turn red when required sections not filled in
