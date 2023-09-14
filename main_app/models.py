from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
def __str__self(self):
    return f'{self.name} ({self.id})'