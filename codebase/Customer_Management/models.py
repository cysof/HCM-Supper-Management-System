from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    about_me = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: The email address of the object.
        :rtype: str
        """
        return self.email
    
    def has_module_perms(self, app_label):
        """
        Check if the user has permissions for a specific app label.

        Args:
            app_label (str): The label of the app to check permissions for.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        """
        Check if the user has permission for a specific permission.

        Args:
            perm (str): The permission to check.
            obj (Optional[Any]): The object to check the permission against. Defaults to None.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        return self.is_superuser
    
        """
        Check if the user has permission for a specific permission.

        Args:
            perm (str): The permission to check.
            obj (Optional[Any]): The object to check the permission against. Defaults to None.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
    def get_full_name(self):
        """
        Returns the full name of the user by concatenating the first name and last name.

        :return: The full name of the user.
        :rtype: str
        """
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """
        Get the short name of the user.

        Returns:
            str: The first name of the user.
        """
        return self.first_name