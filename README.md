# To Do Application - the Reward scheme!

[View the live website here](http://cm-ms3-to-did.herokuapp.com/home)

---

This aplication is a To Do list specifically targeted at people with energy sapping illnesses such
as chronic fatigue, long COVID or depression. It aims to assist in the recovery back to 'normal' life. It encourages the user to think how big a task is and doesn't immediately delete done task, meaning the user can review their day.

---

## User Experience (UX)

-   ### User stories

    #### User Story 1

    As a user, I want to keep track of my To Do list.

    #### Acceptance Criteria

    -   Add a to do item
    -   Complete a to do item
    -   Delete a to do item
    -   Add extra information
        -   Description
        -   Category - such as house work, Work, Crafts.
        -   Deadlines (timescales)
        -   Subtasks/dependencies/contentions - stretch
        -   Energy weighting (high, medium, low)
        -   Recurring tasks.
    -   Prioritize tasks

    #### Description:

    The user will be able to easily add to do items using a 'title'. There will then be optional
    felids that can be populated after creation. The user will be able to prioritize tasks quickly.

    #### User Story 2

    As a user, I want to review my priorities at the beginning of the day.

    #### Acceptance Criteria

    -   A prompt that asks the user to prioritise the tasks for the day
    -   Pulls yesterdays prioritise for review
    -   Looks at the due date of tasks and suggests priorities.
    -   Checks tasks don't go over 'energy' targets (i.e 5 small tasks)

    #### Description:

    The user will be prompted to review and prioritise tasks. The application will 'remind' the user
    of their energy goals if they put too much in their day.

    #### User Story 3

    As a user, I want to review my done tasks at the end of the day.

    #### Acceptance Criteria

    -   A prompt that shows the user the tasks they have completed that day
    -   Gives an opportunity for the user to review/put in tomorrows priorities.
    -   Gives the user a positive message?

    #### Description:

    The user will be prompted to review the tasks that have been done in the day. The option
    will be given to set the next days priorities.

    #### User Story 4

    As a user, I want to have control over my settings and preferences

    #### Acceptance Criteria

    -   setting and preferences are easily readable
    -   can be changed at the touch of a button
    -   settings are explained well.

    #### Description:

    The user will be able to access and edit all preferences. Settings will be simply explained and easy to access.

    #### User Story 5

    As a user, I want to know how to use this application.

    #### Acceptance Criteria

    -   The instruction for the application should be clear and visible on first opening.
    -   The buttons should be clearly indicated.
    -   Instructions should tell the user how to;
        -   Log on/off
        -   Add a to do item/tally
        -   Complete/delete a to do item/tally
        -   Add/remove rewards
        -   Contact developer for feedback/support
    -   The instruction to use the application should be accessible whist playing.

    #### Description:

    The instruction will pop up on fist opening the application. Instructions will indicate how to use the
    application. The instructions will be accessible through a 'help' button

    #### User Story 6

    As a returning user, I want to see my To Do list.

    #### Acceptance Criteria

    -   The user will have a log on to see their To Do list stored
    -   The user will be able to log off.
    -   The user will have the option to delete the account and associated data.

    #### Description:

    The user will be prompted to log on to the application to see there to do list.

    #### User Story 7

    As a user, I want give feedback on this application.

    #### Acceptance Criteria

    -   A way to send an email to the developer.
    -   To be alerted when the email has sent or failed to send.
    -   Validation on the boxes to ensure that all relevant boxes are filed in.
    -   Validation on the email address to say an email has been inputted.

    #### Description:

    This will be achieved using a contact form and the JS email service. With a pop up modal to tell the
    user that the message has been sent or failed to send. The required attribute will be added to each of
    the required boxes. The email attribute will be added to the email box. This will ensure the user is
    alerted if any of the information is incorrect or incomplete.

    #### User Story 8

    As a user, I want to view the website and content clearly on any device

    #### Acceptance Criteria

    -   Website layout is well displayed and readable across all sized devices and different orientations.

    #### Description:

    Flexbox will be used to lay the content of the website. Mobile first design will be used when
    coding the project and testing will be required to ensure the layout is clear on all devices. No
    elements should overlap their containers and all items should be responsive.

-   ### Design

    The design of this application is simple and easy to use.

    -   #### Colour Scheme

        ![colours](assets\images\toDidColours.png)
        I chose calming colours for the main colour scheme. The colours on tasks is a nice positive green.

    -   #### Typography

        I chose a simple easy to read font [Rubik](https://fonts.google.com/specimen/Rubik?category=Sans+Serif) from [google fonts](https://fonts.google.com/).

    -   #### Symbols and Buttons

        Symbols came from [google icons](https://fonts.google.com/icons) as they are familiar to most users and have nice lines.

*   ### Wireframes

    -   Mobile Wireframes - [View](assets/wireframes/phone.png)

    -   Tablet Wireframes - [View](assets/wireframes/tablet.png)

## Features

I have split the features into Beta, Issue 1, Issue 2 & Issue 3. The project is currently
at the Issue one.

-   ### Beta

    -   Register
    -   Log on/off
    -   CRUD functions for Tasks
    -   Make Responsive on all Devices.

-   ### Issue 1

    -   CRUD functions for all categories
    -   Prioritize and complete tasks from the 'home' page
    -   Allows the user to view Tasks completed 'Today'
    -   Simple explication of how the app works.

-   ### Issue 2

    -   Pulls yesterdays prioritise for review
    -   Looks at the due date of tasks and suggests priorities.
    -   Checks tasks don't go over 'energy' targets (i.e 5 small tasks)
    -   User can edit and delete there account
    -   Add a category from the Account Page

-   ### Issue 3
    -   A prompt that asks the user to prioritise the tasks for the day
    -   Sign up form with extra questions
    -   fancy Graphical explanation of how the app works.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)
-   [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Frameworks, Libraries & Programs Used

-   [Google Fonts](https://fonts.google.com/)
-   [RandomKeygen](https://randomkeygen.com/)
-   [Heroku](https://id.heroku.com/)
-   [WTForms](https://wtforms.readthedocs.io/en/2.3.x/)
-   [Cypress](https://docs.cypress.io/guides/overview/why-cypress)

### Resources

-   [Code Institute Course Content](https://courses.codeinstitute.net/)
-   Code Institute **SLACK Community**
-   [Stack Overflow](https://stackoverflow.com/)
-   [YouTube](https://www.youtube.com/)
-   [CSS-Tricks](https://css-tricks.com/)
-   [Balsamiq](https://balsamiq.com/wireframes/)
-   [CSS Filter generator](https://codepen.io/sosuke/pen/Pjoqqp)

## Testing

Full Testing is detailed in a separate file [here](testing.md).

### Interesting Bugs / Issues

This section will detail the interesting Issues and Bugs that I came across whilst coding and the main ones that I found during testing.

**During coding**

| Issue/Bug                                     | Comments                                                                                                                                                                                                                                                                | Final Fix                                                                                                                                                                                                                                    |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to store dates to show back to the user   | Not the first problem I expected to encounter. The format of dates seemed to be many and the main issue i was having is that MongoDB wouldn't accept the output from WTForms                                                                                            | After much research i came across this [article](https://www.w3.org/QA/Tips/iso-date)and concluded that the best way to store the due date is in accordance with ISO 8601 which is YYYY-MM-DD and as a string, that can be manipulated later |
| Implementation of sliders on the account page | I was stuck here for longer than I care to remember. After great sucess implementing a cool slider for the opening and closing of tasks (lines 118 - 140 in the JS) I tried implementing this to the account page. It didn't work as unordered lists don't have height. | I ended up calculating the available height for the section slider to be opened in                                                                                                                                                           |
| Changing the colour of a SVG file using CSS   | Tried changing the text fill and background colours I could change the colour in the SGV file but this would limit options for the future                                                                                                                               | Filter was the correct property that needed to be changed but it doesn't take a hex value so I used the [CSS Filter generator](https://codepen.io/sosuke/pen/Pjoqqp) to get my desired                                                       |

**During Testing**

| Issue/Bug                                | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Final Fix                                                                                                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to test the html5 inbuilt validation | I could see that it was working but could work out how to get cypress to 'register' it was working and couldn't find the bubble in developer tools.                                                                                                                                                                                                                                                                                                                    | Finally found this [Blog Post](https://glebbahmutov.com/blog/form-validation-in-cypress/) that explained how to check the validation status                                                                      |
| Forms are not validating correctly       | One of the big this I found is that somewhere during my coding I have stopped validating my forms, for the most part this was an easy fix, I just turned it back on. However the due date on the Add and Edit Task forms is stopping the form from submitting when the 'official' form validation is turned on. I spent some time looking around for a full fix however it looks like i have to completely re-evaluate how I interact and store dates in the database. | I have re-set up the validation for the forms that I can. for the Add/Edit forms there is validation on the server side and the error handling will handle any problems until this issue can be correctly fixed. |

## Deployment

### Project Creation

I used VScode and git to produce this project.
The following commands were used to keep version control

-   `git add .` to stage files before committing
-   `git commit -m "message explaining commit"` to commit the local repository
-   `git push` to push all committed changes to the GitHub repository

### Deployment to Heroku

**Create application:**

1. Navigate to Heroku.com and login or sign up.
2. Click on the new button.
3. Select create new app.
4. Enter the app name, this must be unique.
5. Select region.
6. Click Create App.

**Set up connection to Github Repository:**

1. Click the deploy tab
2. Select GitHub as the deployment method.
3. A prompt to find a github repository to connect to will then be displayed.
4. Enter the repository name for the project and click search.
5. Once the repo has been found, click the connect button.
6. To enable automatic deployment (_optional_)
    1. Scroll to the Automatic deploys section
    2. Choose the branch you want to deploy from
    3. Click Enable Automation Deploys.

**Set environment variables:**

1. Click on the settings tab
2. Click the 'reveal config vars' button.
3. Variables needed:
    - IP
    - MONGO_DBNAME
    - MONGO_URI
    - PORT
    - SECRET_ACCESS_KEY

_These variables change depending on your set up so I will not add mine here._

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/CharlieMallon/milestoneTwo)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

Inspirations came from many of the to do aplication out there but I particularly like [any.do](https://www.any.do/) and [todoist](https://todoist.com/).

### Code

Credits for code not modified for my purposes is created in the code as well. These are the places that I learnt some of the extra bits I wanted to include.
| Source | Comments|
| --- | --- |
| https://www.youtube.com/watch?v=EpJRJsmqnn0 | The video I used to set up my registration form with wtforms|
| https://www.youtube.com/watch?v=HY0le1NAczc&t=0s | The video that explains how to create the base for the macro used to clean up the WTForm's code|
| https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_collapsible | How to implement Collapsible sections|
| https://jonsuh.com/hamburgers/ | Some very cool hamburgers!|
| https://dollarshaveclub.github.io/shave/ | A neat bit of js I have used to shorten the titles of the tasks when they go over two lines of text|
| https://www.geeksforgeeks.org/python-404-error-handling-in-flask/ | How to handle 404 errors in flask|
| https://css-tricks.com/custom-scrollbars-in-webkit/ | How to style the default scroll bars, so that my site can be accessible and still look good|

### Content

-   All content was written by the developer.

### Media

I used gif's from [giphy](giphy.com) to make my error pages slightly amusing and therefore 'nicer' to look at these are the original links;

-   https://giphy.com/gifs/studiosoriginals-mothers-day-iDiO5gkqaVjZ7cxnSV
-   https://giphy.com/gifs/looneytunes-looney-tunes-wile-e-coyote-39wBF8ZtAwIXvDnI23

### Acknowledgements

-   My Mentor Brian Macharia for some good guidance.
-   Mr_Bim_alumni for general encouragement and the occasional kick up the backside.
-   Anthony for the prods in the right direction.
-   Eventyret for breaking the security as soon as he was given the links to the site.
