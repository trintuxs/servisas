from django.urls import path

from automobilis.views import masina

urlpatterns = [
    path('Auto/', masina )
]