from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.username)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    mail_id = models.EmailField()
    address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return '{}'.format(self.name)