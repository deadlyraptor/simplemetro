from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        'line/<str:line_code>',
        views.StationListView.as_view(),
        name='line',
    ),
]
