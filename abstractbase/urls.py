from django.urls import path
from .views import CreateUserView,CreateDoneView

urlpatterns = [
    path('create', CreateUserView.as_view(), name='create'),
    path('create-done', CreateDoneView.as_view(), name='create-done')
]
