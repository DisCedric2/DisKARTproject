from django.urls import path
from . import views
from app.views import ProductRegister, ProductList, ProductDelete, ProductUpdate

urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path(
        "request_password_reset/",
        views.request_password_reset,
        name="request_password_reset",
    ),
    path("reset_password/<uname>/", views.reset_password, name="reset_password"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('mobilelist/', views.mobilelist, name='mobilelist'),
    path('clothslist/', views.clothslist, name='clothslist'),
    path('electronicslist/', views.electronicslist, name='electronicslist'),
    path('shoeslist/', views.shoeslist, name='shoeslist'),
    path('showpricerange/', views.showpricerange, name='showpricerange'),
    path('sortingbyprice/', views.sortingbyprice, name='sortingbyprice'),
    path('searchproduct/', views.searchproduct, name='searchproduct'),
    path('showcarts/', views.showcarts, name='showcarts'),
    path('addtocart/<productid>', views.addtocart, name='addtocart'),
    path('removecart/<productid>', views.removecart, name='removecart'),
    path('updateqty/<int:qv>/<productid>', views.updateqty, name='updateqty'),
    path('addaddress_single/<productid>/', views.addaddress_single, name='addadress_single'),
    path('addaddress_all/', views.addaddress_all, name='addadress_all'),
    path('showaddress/', views.showaddress, name='showaddress'),
    path('payment/', views.payment, name='payment'),
    path('showorders/', views.showorders, name='showorders'),
    path('ProductRegister/', ProductRegister.as_view(), name="ProductRegister"),
    path('ProductList/', ProductList.as_view(), name="ProductList"),
    path('ProductDelete/<int:pk>', ProductDelete.as_view(), name="ProductDelete"),
    path('ProductUpdate/<int:pk>', ProductUpdate.as_view(), name="ProductUpdate"),
]
