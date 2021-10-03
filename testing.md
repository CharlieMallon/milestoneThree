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

1.  Nav bar links are not whole buttons
2.  You cannot delete your user account
3.  The title on the contact page is not bound
4.  Register function doesn't load the Account Page
5.  When no tasks planned/completed the bar should say something like 'No Tasks Prioritised'
6.  When No tasks are found the text needs some padding
7.  You should be able to add a category from the Account Page
8.  On large screens the tasks should be split into two lists
9.  Error Pages need more content - images?
10. Landing Page on mobile should have a 'log in' link in the top right corner (not just the burger icon)
11. Username can be too many characters (over two lines) which messes up the calculations on the accounts page
12. Boxes should turn red when required sections not filled in
13. Task name should keep the capitals the user writes (eg Test Task not Test task)
14. Cant click 'done' on add tasks as it doesn't give a 'done-date' to the database
15. Due by sate on home - mobile is backwards (2021-10-10)
16.
