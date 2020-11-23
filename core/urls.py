from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from core import views

router = DefaultRouter()
router.register('register', views.UserProfileViewSet)
router.register('tasks',views.TasksViewSet)
router.register('addCar', views.addCarViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]