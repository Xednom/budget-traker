from django.urls import include, path

from rest_framework.routers import DefaultRouter

from users.api.views import UserViewSet
from expenses.api.views import ExpenseTrackerViewSet, TypeOfExpensesViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'expenses', ExpenseTrackerViewSet)
router.register(r'type_of_expenses', TypeOfExpensesViewSet)

urlpatterns = [
    path('', include(router.urls))
]