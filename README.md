# To Do Application - the Reward scheme!

So this project seems to have grown arms and legs.... pretty sure it will run away at some point!

For my MS3 submission I feel it needs to be pulled back quite a bit. I like the To Do aspect, something
that I really struggled with during my recovery from COVID was the lack of energy and the fact I never
felt like I achieved anything. so I want to build an aplication that encourages you to think in smaller
chunks and rewards you for doing simple every day tasks. Specifically I believe the aspect of a
traditional todo app that is missing when you are recovering from or still in an energy illness is a
promp to get you to review what you did in a day and review your prioritize at the beginning of the day.

As a stretch I think you should also be able to send messages to each other, send encouragement or just 
let someone know you thought of them that day.

This project will be based on some guidance from the NHS which I found particularly useful, Pace, plan 
and Prioritize. [link](https://www.yourcovidrecovery.nhs.uk/your-road-to-recovery/managing-daily-activities/)

Although the intent of this app has evolved I believe that most of the below is still relevant so I 
will leave it here for now

<!-- [View the live website here]() -->

---

This aplication is a To Do list specifically targeted at people with energy sapping illnesses such
as chronic fatigue long COVID or depression. It aims to assist in the recovery back to 'normal' life.

---

This application is a To Do list with a Twist, it uses the reward theory to give you rewards for
completing tasks. This rewards are given at random intervals so as to encourage tasks to be done
without rewards. The inspiration for this came from an experiment on children -name experiment -
find experiment - [this one](https://bingschool.stanford.edu/news/mark-lepper-intrinsic-motivation-extrinsic-motivation-and-process-learning)

Started as a To Do app, is now more like a life planner/tracker - integrated life organization app.

Done tasks / not done tasks - no failed tasks.

all about positive reinforcement

When a prioritised task is not completed on the day it was prioritised have a pop up that allows you
 to review/roll over your tasks.

Completed tasks turn green and have a animation that makes them move to the bottom of the list/off
the list

Canceled tasks line out fade and 'disappear'

Notifications - On phone/watch/computer? - emails?
-   [for android](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)
-   [for apple](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html)

Done list! - I want to see what I have completed today!

Settings - need to be able to adjust how often you are pinged.

https://www.healthline.com/health/intrinsic-motivation#extrinsic-motivation - a bit about motivation

**Name Ideas**

-   DOOO
-   Rewarding To Do's

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

    The user will be prompted to review and prortise tasks.  The application will 'remind' the user
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

    <!-- #### User Story 4

    As a user, I want to have control over my settings and preferences

    #### Acceptance Criteria

    -   setting and preferences are easily readable
    -   settings a

    #### Description:

     -->

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

        Dark and light modes. I want some calming colours (not to in your face) for the main colours
        scheme. The done colours on tasks should be a nice positive green.

    -   #### Typography

        simple easy to read - dyslexic font?
        Tick's should cross the line of the box

    -   #### Buttons

        Circles except the burger menu

    -   #### symbols

        need to find multiple symbols for things, look at font awesome - this is mainly for the tally bit.

    -   #### sound

        when a task is completed it needs to go bing - or some such sound that is a good positive yes I
        have done this!

*   ### Wireframes

    -   Mobile Wireframes - [View](assets/wireframes/phone.png)

    -   Tablet Wireframes - [View](assets/wireframes/tablet.png)

    -   Window Wireframes - [Not completed - no link]()

## Features

I have split the features into Beta, Issue 1, Issue 2 & Issue 3. The project is currently
at the design conception stage.

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
