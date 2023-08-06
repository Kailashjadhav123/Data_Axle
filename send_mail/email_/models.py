from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=1000)
    employee_ID = models.AutoField(unique=True, primary_key=True)
    email_id = models.EmailField()
    birth_date = models.DateField()
    join_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee_ID}"


class Template(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
class Mail_Logs(models.Model):
    employee_ID = models.IntegerField()
    message = models.TextField()
    mail_sent_date = models.DateField()
    mail_type = models.CharField(max_length=1000)
    status= models.CharField(max_length=1000)
    