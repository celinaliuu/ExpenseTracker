"""
URL configuration for ExpenseTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ExpenseLogging import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenselogs/add/', views.addExpense, name='addExpense'),
    path('<int:expenseid>/delete/', views.deleteExpense, name='deleteExpense'),
    path('expenselogs/', views.expenseLogs, name = 'expenseLogs'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('<int:expenseid>/', views.updateView, name = 'updateView'),
    path('<int:expenseid>/update/', views.updateExpense, name = 'updateExpense'),
    path('accounts/login/', auth_views.LoginView.as_view(), name = 'login'),
    path('signup/', views.signUpView, name = 'signUp'),
    path('logout/', views.customLogout, name = "logout"),
    path('visualization/', views.expenseVisualization, name='visualization'),
    path('expense-chart-data/', views.expenseChartData, name='expense-chart-data'),
    path('visualization/', views.expenseVisualization, name='expenseVisualization'),
    

]
