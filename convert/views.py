from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .pypdf import Convert
# Create your views here.


class Upload(View):
    def get(self, request):
        context = {
            'convert': {
                'ready': False,
                'name': ""
            },
            'download': {
                'isDone': False,
                'link': "\\"
            }
        }
        return render(request, "index.html", context)

    def post(self, request):
        if (request.POST.get('convertFormat')):
            convertFormat = request.POST['convertFormat']
            name = request.POST['name']
            Convert(name, convertFormat)

            context = {
                'convert': {
                    'ready': True,
                    'name': name,
                },
                'download': {
                    'ready': True,
                    'link': name+convertFormat,
                }
            }
            return render(request, "index.html", context)

        else:
            uploadedfile = request.FILES['uploadFile']
            fs = FileSystemStorage()
            fs.save(uploadedfile.name, uploadedfile)

            context = {
                'convert': {
                    'ready': True,
                    'name': uploadedfile.name[:-4],
                },
                'download': {
                    'ready': False,
                    'link': "\\"
                }
            }
            return render(request, "index.html", context)
