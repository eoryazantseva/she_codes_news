from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username
    # we want to get the username from the db, so that we could show something like: ""Hello, Username!"". We are now going to create forms.py file in the user folder.

