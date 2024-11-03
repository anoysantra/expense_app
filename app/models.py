from django.db import models

# Create your models here.

class Expense(models.Model):
    class Category(models.TextChoices):
        GROCERY = 'grocery', 'Grocery'
        FOOD_DELIVERY = 'food_delivery', 'Food Delivery'
        ONLINE_ORDER = 'online_order', 'Online Order'
        SENT_TO_SOMEONE = 'sent_to_someone', 'Sent to Someone'
        UBER_RAPIDO = 'uber_rapido', 'Uber/Rapido'
        SHOPPING = 'shopping', 'Shopping'
        OTHERS = 'others', 'Others'

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"

    
