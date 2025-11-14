from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.portfolio_list, name='portfolio_list'),
    path('add/', views.add_stock, name='add_stock'),
]
