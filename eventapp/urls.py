from eventapp import views
from django.urls import path

urlpatterns=[
    path("",views.user_home,name="user_home"),
    path("load_user_signup",views.load_user_signup,name="load_user_signup"),
    path("load_user_login",views.load_user_login,name="load_user_login"),
    path("load_admin_home",views.load_admin_home,name="load_admin_home"),
    path("load_add_product",views.load_add_product,name="load_add_product"),
    path("load_product_page",views.load_product_page,name="load_product_page"),
    path("load_view_product",views.load_view_product,name="load_view_product"),
    path("load_add_service",views.load_add_service,name="load_add_service"),
    path("load_view_service",views.load_view_service,name="load_view_service"),
    path("load_view_user",views.load_view_user,name="load_view_user"),
    path("load_service_page",views.load_service_page,name="load_service_page"),
    path("load_profile_page",views.load_profile_page,name="load_profile_page"),
    path("load_profile_edit",views.load_profile_edit,name="load_profile_edit"),
    path("load_view_book",views.load_view_book,name="load_view_book"),
    path("load_add_book",views.load_add_book,name="load_add_book"),
    path("showbook",views.showbook,name="showbook"),

    path("user_signup",views.user_signup,name="user_signup"),
    path("user_login",views.user_login,name="user_login"),
    path("user_logout",views.user_logout,name="user_logout"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("addservice",views.addservice,name="addservice"),
    path("deleteproduct/<int:pk>",views.deleteproduct,name="deleteproduct"),
    path("editproduct/<int:pk>",views.editproduct,name="editproduct",),
    path("deleteservice/<int:pk>",views.deleteservice,name="deleteservice"),
    path("editservice/<int:pk>",views.editservice,name="editservice"),
    path("userdelete/<int:pk>",views.userdelete,name="userdelete"),
    path("edit_user",views.edit_user,name="edit_user"),
    path("addbook/<int:pk>",views.addbook,name="addbook"),
    path("addbook/<int:pk>",views.addbook,name="addbook")
]