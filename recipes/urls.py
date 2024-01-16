from django.urls import path
from recipes.views import my_view, main_page

urlpatterns = [
    path('', main_page),
    path('sobre/', my_view),

]