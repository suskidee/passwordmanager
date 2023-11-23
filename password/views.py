from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddForm, SearchForm
from .models import New
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            print(username)
            return redirect('search', my_search=username)
        else:
            messages.success(request, ('form cannot be blank'))
            return redirect('home')
    else:
        form = SearchForm()
        return render(request, "index.html", {'form':form})


@login_required
def view_all(request):
    obj = New.objects.filter(user=request.user).order_by("-website")
    return render(request, "all.html", {'object': obj})


@login_required
def search(request, my_search):
    user_id = request.user
    results = New.objects.filter(Q(username=my_search) & Q(user=user_id))
    return render(request, "search.html", {'object': results})


@login_required
def view(request, pk):
    obj = New.objects.get(id=pk)
    return render(request, "view.html", {'object': obj})


@login_required
def add(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            new_password = form.save(commit=False)
            new_password.user = request.user
            new_password = form.save()
            messages.success(request, ('password saved successfully'))
            return redirect('home')
        else:
            return redirect('add')
    else:
        form = AddForm()
        return render(request, "add.html", {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('you have been logged in'))
            return redirect('home')
        else:
            messages.success(request, ('user does not exist. click on the link at the bottom to register'))
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('sign up successful'))
            return redirect('home')
        else:
            messages.success(request, ('invalid details. please try again'))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ('you have been logged out'))
    return redirect('home')
