# To Do Application - the Reward scheme!

[View the live website here](http://cm-ms3-to-did.herokuapp.com/home)

---

This aplication is a To Do list specifically targeted at people with energy sapping illnesses such
as chronic fatigue, long COVID or depression. It aims to assist in the recovery back to 'normal' life.  It encourages the user to think how big a task is and doesn't immediately delete done task, meaning the user can review their day.

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

    -   A promp that asks the user to prioritise the tasks for the day
    -   Pulls yesterdays prioritise for review
    -   Looks at the due date of tasks and suggests priorities.
    -   Checks tasks don't go over 'energy' targets (i.e 5 small tasks)

    #### Description:

    The user will be prompted to review and prioritise tasks.  The application will 'remind' the user
    of their energy goals if they put too much in their day.

    #### User Story 3

    As a user, I want to review my done tasks at the end of the day.

    #### Acceptance Criteria

    -   A promp that shows the user the tasks they have completed that day
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

    -   #### symbols and buttons

        Symbols came from [google icons](https://fonts.google.com/icons) as they are fairly familiar to most users.  and have nice lines.

*   ### Wireframes

    -   Mobile Wireframes - [View](assets/wireframes/phone.png)

    -   Tablet Wireframes - [View](assets/wireframes/tablet.png)

    -   Window Wireframes - [Not completed - no link]()

## Features

I have split the features into Beta, Issue 1, Issue 2 & Issue 3. The project is currently
at the design conception stage.

-   ### Beta

    -   Register
    -   Log on/off
    -   All CRUD functions
    -   Tell you how to use the application.
    -   Make Responsive on all Devices.

-   ### Issue 1

    -   Tell you how to use the aplication - with cool arrow graphics in 'slide' format
    -   Sign up form with extra questions
        -   what do you want to use app for?
    -   Prompts that tell the user how to source

-   ### Issue 2

    -   

-   ### Issue 3
    -

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

### Resources

-   [Code Institute Course Content](https://courses.codeinstitute.net/)
-   Code Institute **SLACK Community**
-   [Stack Overflow](https://stackoverflow.com/)
-   [YouTube](https://www.youtube.com/)
-   [CSS-Tricks](https://css-tricks.com/)
-   [Balsamiq](https://balsamiq.com/wireframes/)
-   [CSS Filter generator](https://codepen.io/sosuke/pen/Pjoqqp)

## Testing

Testing is detailed in a separate file [here](testing.md).

### Bugs

This section will detail the bugs that I came across coding and the main one that I found during testing.

One of the first problems i came across was not something i expected, how to store dates, it doesnt seem like it should be that hard, just drop it into the database as a date.  but in what format? how do i make it readable to all, why wont the database acept the output from wtforms?!? I did some research and concluded that the best way to store the duedate is in accordance with ISO 8601 (good old ISO) which is YY-MM-DD and as a string, that can be manipulated later. [artical](https://www.w3.org/QA/Tips/iso-date)

After great sucess implementing a cool slider for the opening and closing of tasks (lines 19 - 40 in the JS) i tried implementing this to the account page, i had some real troubble with the height turns out that ul's dont have height! who knew! I tried wapping the list in a div (didnt work) so will have to come up with a diffrent aproach to the height of these section.

How do i change the colour of SVG files using css. 
    https://stackoverflow.com/questions/22252472/how-to-change-the-color-of-an-svg-element
    I used the [CSS Filter generator](https://codepen.io/sosuke/pen/Pjoqqp)



**During coding**

| Bug | Things Tried | Final Fix |
| --- | ------------ | --------- |
| Bug | Things Tried | Final Fix |

**During testing**

| Test Ref | Test Description | Bug Description | Final fix | Comment |
| -------- | ---------------- | --------------- | --------- | ------- |
| Test Ref | Test Description | Bug Description | Final fix | Comment |


https://glebbahmutov.com/blog/form-validation-in-cypress/ - to test the html 5 required form function
## Deployment

## Credits

Inspirations [any.do](https://www.any.do/) a to do list that looks cool

### Code

https://www.youtube.com/watch?v=EpJRJsmqnn0 - video i used to set up my registration form with wtforms.
https://www.youtube.com/watch?v=HY0le1NAczc&t=0s - clean up code using macro
https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_collapsible - collapable arrows!
https://jonsuh.com/hamburgers/ - hamburger!
https://dollarshaveclub.github.io/shave/ - to shorten titles
https://www.geeksforgeeks.org/python-404-error-handling-in-flask/ - what to do with 404 errors
https://css-tricks.com/custom-scrollbars-in-webkit/ - style scroll bars!

### Content

-   All content was written by the developer.

### Media
-   https://giphy.com/gifs/studiosoriginals-mothers-day-iDiO5gkqaVjZ7cxnSV
-   https://giphy.com/gifs/looneytunes-looney-tunes-wile-e-coyote-39wBF8ZtAwIXvDnI23

### Acknowledgements

-   My Mentor Brian Macharia for some good guidance.
-   Mr_Bim_alumni for general encouragement and the occasional kick up the backside.
-   Anthony for the prods in the right direction.
-   
