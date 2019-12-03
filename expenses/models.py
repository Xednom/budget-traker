import uuid

from django.db import models
from django.conf import settings


class TypeOfExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "Type of Expense"
        verbose_name_plural = "Type of Expenses"
        ordering = ['-name']
    
    def __str__(self):
        return "%s" % (self.name)


class ExpenseTracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    type_of_expenses = models.ForeignKey(TypeOfExpenses, null=True, blank=True, on_delete=models.PROTECT)
    expenses = models.DecimalField(max_digits=19, decimal_places=2)
    budgets = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        verbose_name = 'Expense Tracker'
        verbose_name_plural = 'Expense Trackers'
        ordering = ['-date']