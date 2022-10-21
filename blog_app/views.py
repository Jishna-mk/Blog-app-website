

# Create your views here.

from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog_app.forms import BlogListForm, UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.models import BlogList

# Create your views here


def first(request):
    blogs=BlogList.objects.all()
    return render(request, "home.html",{"all_blogs":blogs})


def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Taken")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already taken")
                return redirect("signup")
            else:
                new_user=form.save()
                new_user.save()
                messages.info(request,"New user Created")
                return redirect('signin')

    return render(request, "signup.html", {"form": form})


def signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("first")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("signin")

    return render(request,"login.html")

def signout(request):

    logout(request)
    return redirect("signin")

def add_blog(request):
    form=BlogListForm()
    if request.method=="POST":
        form=BlogListForm(request.POST,request.FILES)
        if form.is_valid():
            form_data=form.save()
            form_data.save()
            messages.info(request,"successfully Added")
            return redirect("first")
        else:
            messages.info(request,"Blog is not Added")   

    return render(request,"add_blog.html",{"Add_form":form})

def my_blog(request):
    # print(request.user.username)
    my_blogs=BlogList.objects.filter(Author_name=request.user.username)
    print(my_blogs)
    return render(request,"my_blog.html",{"my_blogs":my_blogs})
          
def update_page(request,bid):
    if request.method=="POST":
        BlogList.objects.filter(id=bid).update(Blog_title=request.POST["Blog_title"],Blog_detail=request.POST["Blog_detail"])
        return redirect("my_blog")
    single_blog=BlogList.objects.get(id=bid)
    return render(request,"edit_blog.html",{"single_blog": single_blog})

def delete_page(request,bid):
    blog=BlogList.objects.get(id=bid)
    blog.delete()
    messages.info(request,"successfully deleted")
    return redirect("my_blog")    

def add_like(request,bid,Likes):
    # print(Likes,"number of likes")
    BlogList.objects.filter(id=bid).update(Likes=Likes+1)

    return redirect("first")    