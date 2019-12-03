from rest_framework import serializers
from expenses.models import ExpenseTracker, TypeOfExpenses

from django.contrib.auth import get_user_model
User = get_user_model()


class ExpenseTrackerSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), allow_null=True, required=False)
    type_of_expenses = serializers.SlugRelatedField(slug_field='name', queryset=TypeOfExpenses.objects.all(), allow_null=True, required=False)
    
    class Meta:
        model = ExpenseTracker
        fields = "__all__"


class TypeOfExpensesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeOfExpenses
        fields = "__all__"
