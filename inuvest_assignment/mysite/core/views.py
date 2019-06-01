from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
class Home(TemplateView):
    template_name = 'home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        file_path = os.path.join('media', uploaded_file.name)
        with open(file_path, 'r') as f:
            for line in f:
                array = line.split(",")
                if (array[2]!='High' or array[3]!='Low'):
                    c3 = int(array[2])
                    d3 = int(array[3])
                    print ('TR = ',c3-d3)
    return render(request, 'upload.html', context)
