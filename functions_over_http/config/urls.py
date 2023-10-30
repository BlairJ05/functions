
from django.contrib import admin
from django.urls import path
from app.views import hello_view, age_view, order_total

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hey/<name>/', hello_view),
    path('age-in/<int:end>/<int:birthyear>/', age_view),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>/', order_total)
]
