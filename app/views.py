from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from app.models import *
class SchoolList(ListView):
    model=School
    #template_name=
    #queryset=
    ordering=['scname']
    context_object_name='schools' 

class School_Detail(DetailView):
    model=School
    context_object_name='schoolobj'

class Home(TemplateView):
    template_name='app/home.html'

class School_Create(CreateView):
    model=School
    fields='__all__'


class School_Update(UpdateView):
    model=School
    fields='__all__'



class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')