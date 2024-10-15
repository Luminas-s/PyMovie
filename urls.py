from django.contrib import admin
from django.urls import path, include
from booking import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("booking/", include("booking.urls")),]
#     path("bookticket/", include("bookticket.urls")),
#     path("comboselection/", include("comboselection")),
#     path("checkout/",include("checkout.urls")),
# ]  
