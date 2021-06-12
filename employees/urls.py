from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .api import *
from .views import EmployeeViewSet
app_name='employees'
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('addemp',EmployeeViewSet)
urlpatterns=[
    path('api/get-data',get_data,name='get-data'),
    path('api/insert',insert),
    path('api/',include(router.urls)),
    path('api/payment',payment)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)