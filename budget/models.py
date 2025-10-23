from django.db import models
from datetime import date

class Entries(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    # Fields
    date = models.DateField(default=date.today)
    item = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    ttype = models.CharField(
        "type",
        max_length=2,
        choices=TYPE_CHOICES,
        default=EXPENSE,
    )

    class Meta:
        # newest line first
        ordering = ['-id']
    
    @property
    def signed_amount(self):
        """Returns positive for income, negative for expense."""
        return self.amount if self.ttype == self.INCOME else -self.amount
    
    def __str__(self):
        return f"{self.get_ttype_display()} ${self.amount} - {self.item}"
