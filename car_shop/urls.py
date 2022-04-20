from .views import CreateMark, ListMark, DetailMark
from django.urls import path

urlpatterns = [
    path('create_mark/', CreateMark.as_view(), name='register_mark'),
    path('mark_list/', ListMark.as_view(), name='mark_list'),
    path('mark/<int:pk>', DetailMark.as_view(), name='detail_mark')
]
