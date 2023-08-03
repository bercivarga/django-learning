from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='posts'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='post')
]