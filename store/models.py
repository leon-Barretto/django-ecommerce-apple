from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES =[
        ('Mac', 'MAC'),
        ('IPHONE', 'iPhone'),
        ('IPAD', 'iPad'),
        ('WATCH', 'Watch'),
        ('TV', 'TV'),
        ('ACCESSORIES', 'Accessories'), 
    ]




    Name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Mac')
    Price = models.DecimalField(max_digits=10, decimal_places=3)
    Url = models.URLField(default='https://example.com')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.Name
    

