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

![ ERD ](https://github.com/eoryazantseva/she_codes_news/blob/main/erd.drawio.png)

## Project Features 

- Order stories by date:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/fceb92da-30d4-4a36-befe-fce1df7fd1d3)
- Styled "new story" form:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/6b9f1342-0983-4234-9641-aa568ca67d9a)
- Story images:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/cd0a032f-beda-4e22-839a-71fcde7552a6)

- Log-in/Log-out:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/a288790c-0328-4f01-b74d-3829c7007679)
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/36a44ae2-c101-4318-a626-4ee36006f1b7)

- "Account view" page:
  [ ] 
- "Create Account" page:
- ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/23281ac7-2f23-4f8b-a30e-137addfb7e59)
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/12446166-61be-4a04-8a80-1e6089136a99)
- View stories by author:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/d98c3adc-2838-4df3-800a-0edf49b015e7)
- "Log-in" button only visible when no user is logged in/:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/ccd3fbce-9553-4ed7-83e4-ac0020e2bee6)
- "Log-out" buttononly visible when a user *is* logged in:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/6343f559-5928-4360-ae76-e39b638189ea)
- "Create Story" functionality only available when user is logged in:
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/4121a72a-4b9a-41b8-b213-71b088f388b5)
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/78dd44f5-0434-4761-89e7-a5ba228997fc)


## Additional Features:
- Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories):
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/c32cb670-422e-4870-a3b6-47f954f24b48)
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/7bb76109-5a94-44b6-b786-d163f05fda7c)
