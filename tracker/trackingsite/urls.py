from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from .views import BillView, BillCreate, BillUpdate, BillDelete, PaymentCreate


admin.autodiscover()

urlpatterns = [
    path('', BillView.as_view(), name='bill-list'),
    path('bill/add/', BillCreate.as_view(), name='bill-add'),
    path('bill/<int:pk>/', BillUpdate.as_view(), name='bill-update'),
    path('bill/<int:pk>/delete/', BillDelete.as_view(), name='bill-delete'),
    path('bill/<int:pk>/pay/', PaymentCreate.as_view(), name='payment-add'),
]
