from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .pypdf import Convert
# Create your views here.


def Upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            request_file = request.FILES['uploadFile']
            convertFormat = form.cleaned_data['convertFormat']
            if request_file:
                fs = FileSystemStorage()
                file = fs.save(request_file.name, request_file)
                fileurl = fs.url(file)
                Convert()

            return redirect('home')

    else:
        form = UploadForm()
        return render(request, "index.html", {'form': form})
