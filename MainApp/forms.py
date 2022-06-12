from django import forms
from .models import *


class HistoricalPlaceCommentForm(forms.ModelForm):
    class Meta:
        model = HistoricalPlaceComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class IndianHistoryCommentForm(forms.ModelForm):
    class Meta:
        model = IndianHistoryComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class CurrentIndiaCommentForm(forms.ModelForm):
    class Meta:
        model = CurrentIndiaComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class FreedomFighterCommentForm(forms.ModelForm):
    class Meta:
        model = FreedomFighterComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class FactBlogCommentForm(forms.ModelForm):
    class Meta:
        model = FactBlogComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class CustomAndTraditionCommentForm(forms.ModelForm):
    class Meta:
        model = CustomAndTraditionComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
