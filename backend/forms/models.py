from django.db import models

# Create your models here.
class Forms(models.Model):
    form_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField( max_length=254)
    address = models.CharField( max_length=500)


    def __str__(self) -> str:
        return self.name