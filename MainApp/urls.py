from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .sitemaps import AB_sitemap
from django.contrib.sitemaps.views import sitemap

app_name = 'ADBH'

sitemaps = dict()
sitemaps.update(AB_sitemap)

urlpatterns = [
                  path('', views.Index.as_view(), name='index'),
                  path('historicalplaces/', views.HistoricalPlaces.as_view(), name='historicalplaces'),
                  path('historicalplaces/<slug>/', views.HistoricalPlacesDetail.as_view(),
                       name='historicalplacesdetail'),
                  path('indianhistory/', views.IndianHistory.as_view(), name='indianhistory'),
                  path('indianhistory/<slug>/', views.IndianHistoryDetail.as_view(), name='indianhistorydetail'),
                  path('currentindia/', views.CurrentIndia.as_view(), name='currentindia'),
                  path('currentindia/<slug>/', views.CurrentIndiaDetail.as_view(), name='currentindiadetail'),
                  path('freedomfighter/', views.FreedomFighter.as_view(), name='freedomfighter'),
                  path('freedomfighter/<slug>/', views.FreedomFighterDetail.as_view(), name='freedomfighterdetail'),
                  path('factblog/', views.FactBlog.as_view(), name='factblog'),
                  path('factblog/<slug>/', views.FactBlogDetail.as_view(), name='factblogdetail'),
                  path('customandtradition/', views.CustomAndTraditions.as_view(), name='customandtradition'),
                  path('customandtradition/<slug>/', views.CustomAndTraditionsDetail.as_view(),
                       name='customandtraditiondetail'),
                  path('searched/', views.Searched.as_view(), name='searched'),
                  path('comments/', views.Comments.as_view(), name='comments'),
                  path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
