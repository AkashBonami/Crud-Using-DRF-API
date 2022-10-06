from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ListViewApi.as_view(),name='Read'),
    path('create/',views.CreateViewApi.as_view(),name='create'),
    path('update/<int:pk>/',views.UpdateViewApi.as_view(),name='update'),
    path('delete/<int:pk>/',views.DestroyViewApi.as_view(),name='delete')
]
