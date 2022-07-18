from django.contrib.sitemaps import Sitemap
from .models import *


class CommonSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def lastmod(self, obj):
        return obj.timestamp


class HistoricalPlaceModel_sitemap(CommonSitemap):
    def items(self):
        return HistoricalPlaceModel.objects.all()


class IndianHistoryModel_sitemap(CommonSitemap):
    def items(self):
        return IndianHistoryModel.objects.all()


class CurrentIndianModel_sitemap(CommonSitemap):
    def items(self):
        return CurrentIndianModel.objects.all()


class FreedomFighterModel_sitemap(CommonSitemap):
    def items(self):
        return FreedomFighterModel.objects.all()


class FactBlogModel_sitemap(CommonSitemap):
    def items(self):
        return FactBlogModel.objects.all()


class CustomAndTraditionModel_sitemap(CommonSitemap):
    def items(self):
        return CustomAndTraditionModel.objects.all()


AB_sitemap = {
    'HistoricalPlaceModel_sitemap': HistoricalPlaceModel_sitemap,
    'IndianHistoryModel_sitemap': IndianHistoryModel_sitemap,
    'CurrentIndianModel_sitemap': CurrentIndianModel_sitemap,
    'FreedomFighterModel_sitemap': FreedomFighterModel_sitemap,
    'FactBlogModel_sitemap': FactBlogModel_sitemap,
    'CustomAndTraditionModel_sitemap': CustomAndTraditionModel_sitemap
}
