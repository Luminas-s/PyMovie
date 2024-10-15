from django.urls import path
from . import views

urlpatterns = [
    path('bookticket/', views.bookticket_view, name='bookticket'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('comboselection/', views.comboselection_view, name='comboselection'),
    path('trangphim/', views.trangphim_view, name='trangphim'),
]
