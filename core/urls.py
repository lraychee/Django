from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 設定根目錄頁面
]
