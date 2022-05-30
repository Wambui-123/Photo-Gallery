from django.shortcuts import render, redirect, reverse
from .models import Image
from .forms import ImageForm, ImageModelForm  
# Create your views here.

def landing_page(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'landing.html',{"obj":obj})
        else:
            form=ImageForm()
            img=Image.objects.all()
            return render(request,'landing.html',{"img":img,"form":form})
    return render(request, 'landing.html')


def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'landing.html',{"obj":obj})
        else:
            form=ImageForm()
            img=Image.objects.all()
            return render(request,'landing.html',{"img":img,"form":form})
    return render(request,'landing.html')
    


# creating form
def gallery_upload(request):
    form = ImageModelForm()
    if request.method == "POST":
        print('Recieving Post Request')
        form = ImageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gallery_upload')
    context = {
        "form": form
    }
    return render(request, 'gallery/gallery_upload.html', context)

