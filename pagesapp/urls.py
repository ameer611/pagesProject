from django.urls import path
from .views import HomePageView, AboutPageView, ProductsPageView, HistoryPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('products/', ProductsPageView.as_view(), name = 'product'),
    path('history/', HistoryPageView.as_view(), name = 'history'),
    path('', HomePageView.as_view(), name= 'home'),
]