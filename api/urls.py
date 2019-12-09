from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.api.views import UserViewSet
from expenses.api.views import ExpenseTrackerViewSet, TypeOfExpensesViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'expenses', ExpenseTrackerViewSet)
router.register(r'type_of_expenses', TypeOfExpensesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]