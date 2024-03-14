from django.urls import path
from .views import home, create_lego, create_figure, create

urlpatterns = [
    path('', home, name='home'),
    path('create_lego/', create_lego, name='create_lego'),
    path('create_figure/', create_figure, name='create_figure'),
    path('create/', create, name='create'),
]