from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from expenses.api.serializers import ExpenseTrackerSerializer, TypeOfExpensesSerializer

from expenses.models import ExpenseTracker as expense, TypeOfExpenses as type_of_expenses


class ExpenseTrackerViewSet(viewsets.ModelViewSet):
    queryset = expense.objects.all()
    serializer_class = ExpenseTrackerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        curret_user = expense.objects.filter(name=self.request.user)


class TypeOfExpensesViewSet(viewsets.ModelViewSet):
    queryset = type_of_expenses.objects.all()
    serializer_class = TypeOfExpensesSerializer
    permission_classes = [IsAuthenticated]