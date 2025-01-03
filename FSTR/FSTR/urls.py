
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pereval import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'coords', views.CoordsViewSet, basename='coords')
router.register(r'level', views.LevelViewSet, basename='level')
router.register(r'pereval', views.PerevalViewSet, basename='pereval')
router.register(r'images', views.ImagesViewSet, basename='images')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

]
