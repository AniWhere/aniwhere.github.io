from django.contrib import admin
from django.urls import path,include
from awapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('board/',views.showattractions,name="showattractions"),
    path('bookmark/',views.bookmark,name="bookmark"),
    path('plan/',views.plan,name="plan"),
    path('recommend/',views.recommend,name="recommend"),
    path('search/',views.search,name="search"),
    path('check/',views.check,name="check"),
    path('check/<str:id>', views.check, name='check'),
    path('awaccounts/', include('awaccounts.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)