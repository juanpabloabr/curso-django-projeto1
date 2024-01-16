from django.urls import path
from recipes.views import main_page

urlpatterns = [
    path('', main_page),

]