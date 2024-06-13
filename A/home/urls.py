from . import views
from django.urls import path, include

app_name = 'home'
bucket_urls =[
    path('', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj_bucket/<key>', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
]
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name= 'product_detail'),


]