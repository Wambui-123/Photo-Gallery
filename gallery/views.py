from django.shortcuts import render, redirect, reverse
from .models import Image
from .forms import ImageForm
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

# creating form
def gallery_upload(request):
    form = ImageForm()
    if request.method == "POST":
        print('Recieving Post Request')
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gallery_upload')
    context = {
        "form": form
    }
    return render(request, 'gallery/gallery_upload.html', context)

def gallery_create(request):
    form = ImageForm()
    img=Image.objects.all()
    if request.method == "POST":
        print('Recieving Post Request')
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'landing.html',{"img":img,"form":form})
    context = {
        "form": form
    }
    return render(request, "gallery/gallery_create.html", context)



def gallery_update(request, pk):
    gallery = Image.objects.get(id=pk)
    form = ImageForm(instance = gallery)
    if request.method == "POST":
        print('Recieving Post Request')
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/landing_')
    context = {
        "form": form,
         "gallery": gallery
    }
    return render(request, "gallery/gallery_update.html", context)


def gallery_delete(request, pk):
    gallery = Image.objects.get(id=pk)
    gallery.delete()
    return redirect('landing.html')

