from django.urls import path
from. import views

urlpatterns = [
    path("",views.first,name="first"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("add_blog",views.add_blog,name="add_blog"),
    path("my_blog",views.my_blog,name="my_blog"),
    path("update_page/<int:bid>",views.update_page,name="update_page"),
    path("delete_page/<int:bid>",views.delete_page,name="delete_page"),
    path("add_like/<int:bid>/<int:Likes>",views.add_like,name="add_like")
]
