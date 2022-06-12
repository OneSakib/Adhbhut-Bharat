from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from django.urls import reverse_lazy, reverse


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
        form.instance.post = HistoricalPlaceModel.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:historicalplacesdetail', kwargs={'pk': self.kwargs.get('pk')}))


class IndianHistory(ListView):
    template_name = 'ADBH/indianhistory.html'
    model = IndianHistoryModel
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(IndianHistory, self).get_context_data(**kwargs)
        context['slides'] = IndianHistoryModel.objects.all()
        context['indianhistoryactive'] = True
        return context


class CurrentIndia(ListView):
    template_name = 'ADBH/currentindia.html'
    model = CurrentIndianModel
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(CurrentIndia, self).get_context_data(**kwargs)
        context['slides'] = CurrentIndianModel.objects.all()
        context['currentindianactive'] = True
        return context


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
        form.instance.post = FreedomFighterModel.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:freedomfighterdetail', kwargs={'pk': self.kwargs.get('pk')}))


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
        obj = self.model.objects.get(pk=kwargs.get('object').pk)
        obj.viewcounter += 1
        context['viewcounter'] = obj.viewcounter
        obj.save()
        context['comments'] = FactBlogComments.objects.filter(post=kwargs['object'])
        context['factactive'] = True
        return context

    def post(self, request, *args, **kwargs):
        form = FactBlogCommentForm(request.POST)
        form.instance.post = FactBlogModel.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:factblogdetail', kwargs={'pk': self.kwargs.get('pk')}))


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
        form.instance.post = CustomAndTraditionModel.objects.get(pk=self.kwargs.get('pk'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('ADBH:customandtraditiondetail', kwargs={'pk': self.kwargs.get('pk')}))


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
