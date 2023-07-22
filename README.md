# Evgeniia Riazantseva - She Codes News Project

## About This Project

This is a news website that allows users to read news stories,  and authors to create them.

## How To Run This Code

1. Clone the repo to your machine.

2. In the terminal, change directory into the repo you just cloned down:

`cd she_codes_news`

3. It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python. The name of the virtual environment is your choice, in this tutorial we will call it "venv".
Now, create a new virtual environment, like so:

`python -m venv venv`

4. Then activate the environment.

Windows command:``. venv/Scripts/activate``
Mac command: `source venv/bin/activate

5. Now install the requirements: 

`python -m pip install -r requirements.txt``

6. Open the repo in VS Code or your preferred editor:
`code .`

7. Make migrations. To do that you need to change the directories so that you're next to the "manage.py" file. 

`cd she_codes_news`

Now make the initial migrations:

`python manage.py migrate`

8. Run the server:

`python manage.py runserver`

8. Open the development server link terminal gives you. In my case it is http://127.0.0.1:8000

## Database Schema

![ ERD ]( {{ ./erd.drawio.png }} )

## Project Features 

- [ ] Order stories by date
- [ ] Styled "new story" form
- [ ] Story images
- [ ] Log-in/log-out
- [ ] "Account view" page
- [ ] "Create Account" page
- [ ] View stories by author
- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
- [ ] "Create Story" functionality only available when user is logged in


## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories bycategory.
- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.