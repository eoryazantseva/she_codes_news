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
- 
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/fceb92da-30d4-4a36-befe-fce1df7fd1d3)
  
- Styled "new story" form:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/6b9f1342-0983-4234-9641-aa568ca67d9a)
  
- Story images:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/cd0a032f-beda-4e22-839a-71fcde7552a6)

- Log-in/Log-out:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/a288790c-0328-4f01-b74d-3829c7007679)
  
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/36a44ae2-c101-4318-a626-4ee36006f1b7)

- "Account view" page:

   ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/e3704857-0440-4e95-9332-f2edcfec0ed4)

- "Create Account" page:

- ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/23281ac7-2f23-4f8b-a30e-137addfb7e59)

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/12446166-61be-4a04-8a80-1e6089136a99)

- View stories by author:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/d98c3adc-2838-4df3-800a-0edf49b015e7)
  
- "Log-in" button only visible when no user is logged in/:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/cc181c2c-6738-4fe1-879c-c33bc24688ad)
  
- "Log-out" button only visible when a user *is* logged in:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/d8297931-c153-4784-8203-28dc1e28e265)
  
- "Create Story" functionality only available when user is logged in:

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/d57594a2-65bf-4786-950b-47f1fac2e638)
  
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/2df2db04-0c21-4861-ba79-214187028bae)


## Additional Features:

- Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories):

  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/c32cb670-422e-4870-a3b6-47f954f24b48)
  
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/7bb76109-5a94-44b6-b786-d163f05fda7c)
  
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/1c243432-b228-4156-abda-9555b4ae6abc)
  
  ![image](https://github.com/eoryazantseva/she_codes_news/assets/93800981/379386fc-3ff9-443c-8f57-a52058613985)


