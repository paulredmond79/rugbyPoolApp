from django.shortcuts import get_object_or_404,render

# Create your views here.

from .models import series

def index(request):
    return HttpResponse("Hello, world. You're at the rugby pool index.")

def series_list(request):
    series_list = series.objects.all()
    #template = loader.get_template('series/index.html')
    context = {
        'series_list': series_list
    }
    #output = ', '.join(s.name for s in series_list)
    return render(request,'series/index.html',context)

def series_detail(request, series_id):
    my_series = get_object_or_404(series,pk=series_id)
    context = {
        'series_name': my_series.name,
        'start_date': my_series.start_date,
        'end_date': my_series.end_date,
        'match_set': my_series.match_set.all()
    }
    return render(request,'series/detail.html',context)

