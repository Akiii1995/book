from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Qty = models.IntegerField()
    Is_Active = models.BooleanField(default=True)

    class Meta:
        db_table = "book"


    def __str__(self):
        return f"{self.Name}"
