from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    published_date = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title
