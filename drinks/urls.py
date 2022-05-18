from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import drink_list, drink_detail

urlpatterns = [
    path('drinks/', drink_list),
    path('drinks/<int:id>', drink_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)