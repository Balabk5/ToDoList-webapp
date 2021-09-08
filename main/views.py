from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.core.files.storage import FileSystemStorage
from main.models import Document
from main.forms import DocumentForm
import os


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newitem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid request")
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})


def base(response):
    return render(response, "main/base.html", {})


def home(response):
    documents = Document.objects.all()
    return render(response, "main/home.html", {'documents': documents})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})


def view(response):
    return render(response, "main/view.html", {})


def form_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'main/form_upload.html', {'uploaded_file_url': uploaded_file_url})

    return render(request, 'main/form_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'main/model_form_upload.html', {'form': form})
