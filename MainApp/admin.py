from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(HistoricalPlaceModel)
class HistoricalPlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(IndianHistoryModel)
class IndianHistoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(CurrentIndianModel)
class CurrentIndiaAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(FreedomFighterModel)
class FreedomFighterAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(FactBlogModel)
class FactBlogAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(CustomAndTraditionModel)
class CustomAndTraditionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['timestamp']
    search_fields = ['title', 'post']


@admin.register(HistoricalPlaceComments)
class HistoricalPlaceCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(IndianHistoryComments)
class IndianHistoryCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(CurrentIndiaComments)
class CurrentIndiaCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(FreedomFighterComments)
class FreedomFighterCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(FactBlogComments)
class FactBlogCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(CustomAndTraditionComments)
class CustomAndTraditionCommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'post', 'timestamp']
    list_filter = ['timestamp', 'active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(SlideImage)
class SlideImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']
