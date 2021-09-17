from django.db import models
 
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=50)
    money_amount = models.IntegerField()
    card_number = models.CharField(max_length=50)
    status = models.IntegerField()
    class Meta:
        db_table = 'users'
