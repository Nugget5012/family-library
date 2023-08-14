from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('manuals/', views.products, name='products'),
    path('manuals/<int:id>', views.detail, name='detail'),
    path('manuals/search',views.search, name='search'),
    path('manuals/view-pdf/', views.pdf_view,name='pdf_view'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)