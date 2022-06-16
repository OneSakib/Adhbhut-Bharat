from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse_lazy, reverse
from next_prev import next_in_order, prev_in_order
import json


# Create your views here.
class Index(TemplateView):
    template_name = 'ADBH/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        historicalplace = HistoricalPlaceModel.objects.all().order_by('-timestamp')[:2]
        freedomfighter = FreedomFighterModel.objects.all().order_by('-timestamp')[:2]
        factblog = FactBlogModel.objects.all().order_by('-timestamp')[:2]
        customandtradition = CustomAndTraditionModel.objects.all().order_by('-timestamp')[:2]
        slide = SlideImage.objects.all()
        data = {
            'historicalplace': historicalplace,
            'freedomfighter': freedomfighter,
            'factblog': factblog,
            'customandtradition': customandtradition,
            'slides': slide,
        }
        context['data'] = data
        return context


class HistoricalPlaces(ListView):
    template_name = 'ADBH/historicalplaces.html'
    model = HistoricalPlaceModel
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(HistoricalPlaces, self).get_context_data(**kwargs)
        context['Historyactive'] = True
        return context


class HistoricalPlacesDetail(DetailView, FormView):
    template_name = 'ADBH/detail/historicalplace.html'
    model = HistoricalPlaceModel
    form_class = HistoricalPlaceCommentForm

    def get_context_data(self, **kwargs):
        context = super(HistoricalPlacesDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(pk=kwargs.get('object').pk)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = HistoricalPlaceComments.objects.filter(post=kwargs['object'])
        context['Historyactive'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = HistoricalPlaceCommentForm(request.POST)
        form.instance.post = HistoricalPlaceModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(
            reverse_lazy('ADBH:historicalplacesdetail', kwargs={'slug': self.kwargs.get('slug')}))


class IndianHistory(View):
    def get(self, request):
        history = IndianHistoryModel.objects.first()
        return HttpResponseRedirect(reverse_lazy('ADBH:indianhistorydetail', kwargs={'slug': history.slug}))


class IndianHistoryDetail(DetailView, FormView):
    template_name = 'ADBH/detail/indianhistory.html'
    model = IndianHistoryModel
    form_class = IndianHistoryCommentForm

    def get_context_data(self, **kwargs):
        context = super(IndianHistoryDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(slug=kwargs.get('object').slug)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = IndianHistoryComments.objects.filter(post=kwargs['object'])
        context['slides'] = IndianHistoryModel.objects.all()
        context['indianhistoryactive'] = True
        context['name'] = obj.title
        # Pagination
        currentpost = obj
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prevslug'] = None
        context['nextslug'] = None
        if prev != None:
            context['prevslug'] = prev.slug
        if next != None:
            context['nextslug'] = next.slug
        return context

    def post(self, request, *args, **kwargs):
        form = IndianHistoryCommentForm(request.POST)
        form.instance.post = IndianHistoryModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:indianhistorydetail', kwargs={'slug': self.kwargs.get('slug')}))


class CurrentIndia(View):
    def get(self, request):
        current = CurrentIndianModel.objects.first()
        return HttpResponseRedirect(reverse_lazy('ADBH:currentindiadetail', kwargs={'slug': current.slug}))


class CurrentIndiaDetail(DetailView, FormView):
    template_name = 'ADBH/detail/currentindia.html'
    model = CurrentIndianModel
    form_class = CurretIndiaCommentForm

    def get_context_data(self, **kwargs):
        context = super(CurrentIndiaDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(slug=kwargs.get('object').slug)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = CurrentIndiaComments.objects.filter(post=kwargs['object'])
        context['slides'] = CurrentIndianModel.objects.all()
        context['currentindianactive'] = True
        context['name'] = obj.title
        # Pagination
        currentpost = obj
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prevslug'] = None
        context['nextslug'] = None
        if prev != None:
            context['prevslug'] = prev.slug
        if next != None:
            context['nextslug'] = next.slug
        return context

    def post(self, request, *args, **kwargs):
        form = CurretIndiaCommentForm(request.POST)
        form.instance.post = CurrentIndianModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:currentindiadetail', kwargs={'slug': self.kwargs.get('slug')}))


class FreedomFighter(ListView):
    template_name = 'ADBH/freedomfighter.html'
    model = FreedomFighterModel
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(FreedomFighter, self).get_context_data(**kwargs)
        context['freedomactive'] = True
        return context


class FreedomFighterDetail(DetailView, FormView):
    template_name = 'ADBH/detail/freedomfighter.html'
    model = FreedomFighterModel
    form_class = FreedomFighterCommentForm

    def get_context_data(self, **kwargs):
        context = super(FreedomFighterDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(pk=kwargs.get('object').pk)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = FreedomFighterComments.objects.filter(post=kwargs['object'])
        context['freedomactive'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = FreedomFighterCommentForm(request.POST)
        form.instance.post = FreedomFighterModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:freedomfighterdetail', kwargs={'slug': self.kwargs.get('slug')}))


class FactBlog(ListView):
    template_name = 'ADBH/factblog.html'
    model = FactBlogModel

    def get_context_data(self, **kwargs):
        context = super(FactBlog, self).get_context_data(**kwargs)
        context['factactive'] = True
        return context


class FactBlogDetail(DetailView, FormView):
    template_name = 'ADBH/detail/factsblog.html'
    model = FactBlogModel
    form_class = FactBlogCommentForm

    def get_context_data(self, **kwargs):
        context = super(FactBlogDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(slug=kwargs.get('object').slug)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = FactBlogComments.objects.filter(post=kwargs['object'])
        context['factactive'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = FactBlogCommentForm(request.POST)
        form.instance.post = FactBlogModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:factblogdetail', kwargs={'slug': self.kwargs.get('slug')}))


class CustomAndTraditions(ListView):
    template_name = 'ADBH/customandtradition.html'
    model = CustomAndTraditionModel

    def get_context_data(self, **kwargs):
        context = super(CustomAndTraditions, self).get_context_data(**kwargs)
        context['customactive'] = True
        return context


class CustomAndTraditionsDetail(DetailView, FormView):
    template_name = 'ADBH/detail/customandtradition.html'
    model = CustomAndTraditionModel
    form_class = CustomAndTraditionCommentForm

    def get_context_data(self, **kwargs):
        context = super(CustomAndTraditionsDetail, self).get_context_data(**kwargs)
        obj = self.model.objects.get(pk=kwargs.get('object').pk)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = CustomAndTraditionComments.objects.filter(post=kwargs['object'])
        context['customactive'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = CustomAndTraditionCommentForm(request.POST)
        form.instance.post = CustomAndTraditionModel.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(
            reverse_lazy('ADBH:customandtraditiondetail', kwargs={'slug': self.kwargs.get('slug')}))


class Searched(View):
    template_name = 'ADBH/searched.html'

    def get(self, request):
        search = request.GET.get('search')
        history = HistoricalPlaceModel.objects.filter(post__icontains=search)
        freedom = FreedomFighterModel.objects.filter(post__icontains=search)
        fact = FactBlogModel.objects.filter(post__icontains=search)
        custom = CustomAndTraditionModel.objects.filter(post__icontains=search)
        context = {
            'history': history,
            'freedom': freedom,
            'fact': fact,
            'custom': custom
        }
        return render(request, 'ADBH/searched.html', context)


class Comments(View):
    def get(self, request):
        historical = HistoricalPlaceComments.objects.all().reverse()[:30]
        indianhistory = IndianHistoryComments.objects.all().reverse()[:30]
        currentindia = CurrentIndiaComments.objects.all().reverse()[:30]
        freedomfighter = FreedomFighterComments.objects.all().reverse()[:30]
        factblog = FactBlogComments.objects.all().reverse()[:30]
        custom = CustomAndTraditionComments.objects.all().reverse()[:30]
        context = {
            'comment': True,
            'historical': historical,
            'indianhistory': indianhistory,
            'currentindia': currentindia,
            'freedomfighter': freedomfighter,
            'factblog': factblog,
            'custom': custom
        }
        return render(request, 'ADBH/comments.html', context)

    def post(self, request):
        if request.method == 'POST':
            obj = request.POST.get('object')
            pk = request.POST.get('pk')
            if obj == 'historical':
                HistoricalPlaceComments.objects.get(pk=pk).delete()
            elif obj == 'indianhistory':
                IndianHistoryComments.objects.get(pk=pk).delete()
            elif obj == 'currentindia':
                CurrentIndiaComments.objects.get(pk=pk).delete()
            elif obj == 'freedomfighter':
                FreedomFighterComments.objects.get(pk=pk).delete()
            elif obj == 'factblog':
                FactBlogComments.objects.get(pk=pk).delete()
            elif obj == 'custom':
                CustomAndTraditionComments.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse_lazy('ADBH:comments'))


class SiteMap(View):
    def get(self, request):
        return render(request, 'sitemap.xml', content_type='text/xml')
