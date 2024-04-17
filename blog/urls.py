from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (home_view, about_view, category_view,
                    blog_single_view, tag_view,
                    bio_view, search_view)


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('cat/<str:name>/', category_view, name='category'),
    path('about/<int:id>/', blog_single_view, name='blog_single'),
    path('tag/<int:id>/', tag_view, name='tag'),
    path('bio/<int:id>/', bio_view, name='bio'),
    path('search/', search_view, name='search')

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

