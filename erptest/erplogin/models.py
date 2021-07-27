from django.db import models
import pyodbc

# Create your models here.
class sqlserverconn(models.Model):
    EMPLOYEE_CODE =models.BigIntegerField()
    FIRST_NAME =models.CharField(max_length=250)
    LAST_NAME =models.CharField(max_length=250)
    LOGIN_PASSKEY =models.CharField(max_length=250)

    def __str__(self) -> str:
        return super().__str__()

