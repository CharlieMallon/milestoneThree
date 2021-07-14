# To Do Application - the Reward scheme!

[View the live website here]()

This application is a To Do list with a Twist, it uses the reward theory to give you rewards for completing tasks.  This rewards are given at random intervals so as to encourage tasks to be done without rewards.  The inspiration for this came from an experiment on children -name experiment - find experiment - this one? (https://bingschool.stanford.edu/news/mark-lepper-intrinsic-motivation-extrinsic-motivation-and-process-learning)

Started as a To Do app, is now more like a life planner/tracker - integrated life organization app.

Done tasks / not done tasks - no failed tasks.

all about positily renforcement

When a prioritied task is not completed on the day it was prioritied have a pop up that allows you to reveiw/roll over your tasks.

Completed tasks turn green and have a animation that makes them move to the bottom of the list/off the list

Canceled tasks line out fade and 'disapear'

Notifications
    -   On phone/watch/computer?
    -   emails?
    -   https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API - for android
    -   https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html - for apple?

Done list! - i want to see what i have completed today!

Settings - need to be able to adjust how often you are pinged.

https://www.healthline.com/health/intrinsic-motivation#extrinsic-motivation - a bit about motivation

**Name Ideas**
- DOOO
- Rewarding To Do's

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
        -   Subtasks/dependencies/contentions
        -   Hashtags?
        -   Recurring tasks.
    -   Prioritize tasks

    #### Description:

    The user will be able to easily add to do items using a 'title'. There will then be optional felids that can be populated after creation. The user will be able to prioritize tasks quickly (i.e this task needs to be done today!).

    #### User Story 2

    As a user, I want to Tally how many times something is done.

    #### Acceptance Criteria

    -   Add a Tally button
    -   Increase the Tally 
    -   Delete a Tally
    -   Add extra information to the tally button
        -   Description
        -   Icon
        -   Target number (is over good or bad?)
    -   Time period for tally 
        -   Daily
        -   Weekly
        -   Monthly

    #### Description:

    The user will easily be able to add to an existing tally from the home page. Creation or deletion of a Tally will be done on a Tally modal or page.

    #### User Story 3

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

    The instruction will pop up on fist opening the application. Instructions will indicate how to use the application. The instructions will be accessible through a 'help' button

    #### User Story 4

    As a returning user, I want to see my To Do's/Tallies.

    #### Acceptance Criteria

    -   The user will have a log on with there To Do's / Tally's stored
    -   The user will have the option to delete the account and associated data.

    #### Description:

    The user will be prompted to log on to the application to see there to do list, tally's and rewards.

    #### User Story 5

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

    #### User Story 6

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

        Dark and light modes. I want some calming colours (not to in your face) for the main colours scheme. The done colours on tasks should be a nice positive green.

    -   #### Typography

        simple easy to read - dyslexic font?
        Tick's should cross the line of the box

    -   #### Buttons

        Circles except the burger menu

    -   #### symbols

        need to find multiple symbols for things, look at font awesome - this is mainly for the tally bit.

    -   #### sound

        when a task is completed it needs to go bing - or some such sound that is a good positive yes I have done this!

*   ### Wireframes

    -   Mobile Wireframes - [View](assets\wireframe\phone.png)

    -   Tablet Wireframes - [View](assets\wireframe\tablet.png)

    -   Window Wireframes - [Not completed - no link]()

## Features

I have split the features into Beta, Issue 1, Issue 2 & Issue 3. The project is currently at the design conception stage.

-   ### Beta

    -   Users cannot see each others To Do's
    -   All CRUD functions
    -   Tell you how to use the application.
    -   Make Responsive on all Devices.

-   ### Issue 1

    -   Tell you how to use the aplication - with cool arrow graphics in 'slide' format

-   ### Issue 2

    -

-   ### Issue 3
    -

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used

1. [SweetAlert2](https://sweetalert2.github.io/)
2. [Google Fonts](https://fonts.google.com/)
3. [Font Awesome](https://fontawesome.com/)

### Resources

-   [Am I Responsive Design](http://ami.responsivedesign.is/#)
-   [Code Institute Course Content](https://courses.codeinstitute.net/)
-   Code Institute **SLACK Community**
-   [Stack Overflow](https://stackoverflow.com/)
-   [YouTube](https://www.youtube.com/)
-   [CSS-Tricks](https://css-tricks.com/)
-   [Balsamiq](https://balsamiq.com/wireframes/)
-   [info on iPhone design](https://webkit.org/blog/7929/designing-websites-for-iphone-x/)

## Testing

Testing is detailed in a separate file [here](testing.md).

### Bugs

This section will detail the bugs that I came across coding and the main one that I found during testing.

**During coding**

| Bug | Things Tried | Final Fix |
| --- | ------------ | --------- |
| Bug | Things Tried | Final Fix |

**During testing**

| Test Ref | Test Description | Bug Description | Final fix | Comment |
| -------- | ---------------- | --------------- | --------- | ------- |
| Test Ref | Test Description | Bug Description | Final fix | Comment |

## Deployment

## Credits

Inspirations [any.do](https://www.any.do/) a to do list that looks cool

### Code

Name my inspirations

### Content

-   All content was written by the developer.

### Media

-   [justy](https://giphy.com/justy) on [giphy.com](https://giphy.com) for the confetti background
-   [wifflegif](https://wifflegif.com/) on [giphy.com](https://giphy.com) for the ghost
-   [imgflip](https://imgflip.com/gif-maker?from=images) was used to make the keys.gif

### Acknowledgements

-   My Mentor Brian Macharia for some good guidance.
-   Mr_Bim_alumni for general encouragement and the occasional kick up the backside.
