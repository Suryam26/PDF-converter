from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .pypdf import Convert
# Create your views here.


class Upload(View):
    def get(self, request):
        context = {
            'name': "",
            'convert': {
                'ready': False,
            },
            'download': {
                'isDone': False,
                'link': "\\"
            }
        }
        return render(request, "index.html", context)

    def post(self, request):
        uploadedfile = request.FILES['uploadFile']
        fs = FileSystemStorage()
        fs.save(uploadedfile.name, uploadedfile)

        context = {
            'name': uploadedfile.name,
            'convert': {
                'ready': True,
                'type': 'None',
            },
            'download': {
                'ready': False,
                'link': "\\"
            }
        }
        return render(request, "index.html", context)


class ConvertFile(View):
    def post(self, request):
        convertFormat = request.POST['convertFormat']
        name = request.POST['name']
        Convert(name[:-4], convertFormat)

        context = {
            'name': name,
            'convert': {
                'ready': True,
                'type': convertFormat,
            },
            'download': {
                'ready': True,
                'link':  name[:-4]+convertFormat,
            }
        }
        return render(request, "index.html", context)
