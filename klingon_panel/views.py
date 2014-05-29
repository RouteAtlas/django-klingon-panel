# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

class HomePageView(TemplateView):
    
    def get(self, request):
        return HttpResponseRedirect("/es")


class IndexPageView(TemplateView):
    #template_name = "index.html"

    def get(self, request, lang):
        #ipdb.set_trace()
        return render_to_response("index.html", {"lang":lang})

      
class ListPageView(TemplateView):
    
    def get(self, request, lang, section):
        #ipdb.set_trace()
        return render_to_response("list.html", {"lang":lang, "section":section})
