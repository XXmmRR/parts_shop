from .views import CreateMark, ListMark, DetailMark, CreateModel, ListModel, DetailModel
from django.urls import path

urlpatterns = [
    path('mark/create_mark/', CreateMark.as_view(), name='register_mark'),
    path('mark/mark_list/', ListMark.as_view(), name='mark_list'),
    path('mark/<int:pk>/', DetailMark.as_view(), name='detail_mark'),
    path('model/create_model/', CreateModel.as_view(), name='register_model'),
    path('model/list_model/', ListModel.as_view(), name='model_list'),
    path('model/<int:pk>/', DetailModel.as_view(), name='detail_model')
]
