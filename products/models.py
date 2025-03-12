from django.db import models

# Create your models here.
category_choices=[
    ('Electronics','Electronics'),
    ('Clothing','Clothing'),
    ('Groceries','Groceries'),
    ('Furniture','Furniture'),
    ('Beauty','Beauty'),
    ('Sports','Sports'),
    ('Automobile','Automobile'),
    ('Books','Books'),
]
class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=50,choices=category_choices,default='Electronics')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TimeField(blank=True)
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name