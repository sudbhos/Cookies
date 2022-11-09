from django.shortcuts import render

# Create your views here.
def namei(request):
    return render(request,"testapp/name.html")

def surnamei(request):
    fname=request.GET['fname']
    response=render(request,"testapp/surname.html")
    response.set_cookie('fname',fname)
    return response

def cityi(request):
    surname = request.GET['surname']
    response = render(request, "testapp/city.html")
    response.set_cookie('surname', surname)
    return response

def alli(request):
    city=request.GET["city"]
    fname=request.COOKIES.get("fname")
    surname=request.COOKIES.get('surname')
    response= render(request,"testapp/all.html",{'city':city,'fname':fname,'surname':surname})
    return response
