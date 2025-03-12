from django.db import models


from django.contrib.auth.models import AbstractUser
# Create your models here.
user_roles=(
    ('Distributor','Distributor'),
    ('Seller','Seller'),
    ('Admin','Admin'),
)

class CustomUser(AbstractUser):
    role=models.CharField(max_length=20,choices=user_roles,default='Seller')
    def __str__(self):
        return f"{self.username} ({self.role})"