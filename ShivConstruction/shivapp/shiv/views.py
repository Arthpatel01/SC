from django.shortcuts import render, HttpResponse

# Create your views here.
def Index(request):

    if request.method == 'POST':
        print('*******************************************')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        print(name)
        print(email)
        print(message)
    return render(request, 'index.html')