from django.shortcuts import render, redirect
from . models import Client

# Create your views here.


def clients(request):
    client = Client.objects.all()
    return render(request, 'index.html', {'clients': client})


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        id_no = request.POST.get('id_no')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        project = request.POST.get('project')

        if len(request.FILES) != 0:
            image = request.FILES['image']

        query = Client(name=name, id_no=id_no,phone=phone, email=email, project=project, image=image)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        id_no = request.POST.get('id_no')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        project = request.POST.get('project')

        edit = Client.objects.get(id=id)
        edit.name = name
        edit.id_no = id_no
        edit.phone = phone
        edit.email = email
        edit.project = project
        if len(request.FILES) != 0:
            if len(edit.image) > 0:
                edit.image = request.FILES['image']
        edit.save()
        return redirect("/")

    y = Client.objects.get(id=id)
    context = {"y": y}
    return render(request, "edit.html", context)


def deleteData(request, id):
    y = Client.objects.get(id=id)
    y.delete()
    return redirect("/")

    return render(request, "index.html")
