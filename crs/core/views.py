from django.shortcuts import render
from django.views.generic import ListView,DeleteView,View,CreateView
import csv
# Create your views here.
def home(request):
    csv_fp=open('hour.csv','r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request,'home.html',{
        'data':out,'headers':headers
    })


def dataset(request):
    return render(request,'Table2.htm')