from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    #path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),

    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),

    #path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),

    #path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),

    path('ckeditor/', include('ckeditor_uploader.urls')),


]

