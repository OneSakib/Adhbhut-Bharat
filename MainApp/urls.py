from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ADBH'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('historicalplaces/', views.HistoricalPlaces.as_view(), name='historicalplaces'),
    path('historicalplaces/<int:pk>/', views.HistoricalPlacesDetail.as_view(), name='historicalplacesdetail'),
    path('indianhistory/', views.IndianHistory.as_view(), name='indianhistory'),
    path('currentindia/', views.CurrentIndia.as_view(), name='currentindia'),
    path('freedomfighter/', views.FreedomFighter.as_view(), name='freedomfighter'),
    path('freedomfighter/<int:pk>/', views.FreedomFighterDetail.as_view(), name='freedomfighterdetail'),
    path('factblog/', views.FactBlog.as_view(), name='factblog'),
    path('factblog/<int:pk>/', views.FactBlogDetail.as_view(), name='factblogdetail'),
    path('customandtradition/', views.CustomAndTraditions.as_view(), name='customandtradition'),
    path('customandtradition/<int:pk>/', views.CustomAndTraditionsDetail.as_view(), name='customandtraditiondetail'),
    path('searched/', views.Searched.as_view(), name='searched'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
