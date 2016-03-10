from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
from polls.models import Question, Choice
import pyexcel.ext.xls
import pyexcel.ext.xlsx

from .models import Data
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'chart/temp.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        end = Data.objects.all().count()
        start = end-10
        return Data.objects.all()[start:end]

    

class UploadFileForm(forms.Form):
    file = forms.FileField()




def import_sheet(request):
    if request.method == "POST":
        Data.objects.all().delete()
        form = UploadFileForm(request.POST,
                              request.FILES)
        
        if form.is_valid():
            request.FILES['file'].save_to_database(
                model=Data,
                mapdict=['x_value', 'y_value'])
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render_to_response('chart/index.html',
                              {'form': form},
                              context_instance=RequestContext(request))

    
