from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('Admin', views.Admin, name="Admin"),
           path('AdminHome', views.AdminHome, name="AdminHome"),
           path('UserHome', views.UserHome, name="UserHome"),
	       path('AdminLoginAction', views.AdminLoginAction, name="AdminLoginAction"),
	       path('Login', views.Login, name="Login"),
	       path('UserLoginAction', views.UserLoginAction, name="UserLoginAction"),	   
	       path('Register', views.Register, name="Register"),
	       path('RegisterAction', views.RegisterAction, name="RegisterAction"),	    
	       path('Delete', views.Delete, name="Delete"),
	       path('DeleteAction', views.DeleteAction, name="DeleteAction"),	
	       path('UpdatePrice', views.UpdatePrice, name="UpdatePrice"),
	       path('UpdatePriceAction', views.UpdatePriceAction, name="UpdatePriceAction"),	
	       path('ViewPurchase', views.ViewPurchase, name="ViewPurchase"),
           path('AvgRatings', views.AvgRatings, name="AvgRatings"),
           path('AvgRatingsDownload', views.AvgRatingsDownload, name="AvgRatingsDownload"),
           path('CopiesSold', views.CopiesSold, name="CopiesSold"),
           path('CopiesSoldDownload', views.CopiesSoldDownload, name="CopiesSoldDownload"),
           path('Topsales', views.Topsales, name="Topsales"),
           path('TopSalesDownload', views.TopSalesDownload, name="TopSalesDownload"),
	       path('ViewBooks', views.ViewBooks, name="ViewBooks"),
	       path('ViewRatings', views.ViewRatings, name="ViewRatings"),
	       path('ManageOrders', views.ManageOrders, name="ManageOrders"),
	       path('CompleteOrder', views.CompleteOrder, name="CompleteOrder"),
	       path('SearchBook', views.SearchBook, name="SearchBook"),
	       path('SearchBookAction', views.SearchBookAction, name="SearchBookAction"),
	       path('AddCart', views.AddCart, name='AddCart'),
	       path('ViewCart', views.ViewCart, name="ViewCart"),
	       path('Payment', views.Payment, name="Payment"),
	       path('BackToCart', views.BackToCart, name="BackToCart"),
	       path('PaymentAction', views.PaymentAction, name="PaymentAction"),
	       path('ViewShippingDetails', views.ViewShippingDetails, name="ViewShippingDetails"),
	       path('ReviewOrders', views.ReviewOrders, name="ReviewOrders"),
	       path('CancelOrder', views.CancelOrder, name="CancelOrder"),
	       path('Ratings', views.Ratings, name="Ratings"),
	       path('RatingsAction', views.RatingsAction, name="RatingsAction"),
	       path('AddBook', views.AddBook, name="AddBook"),
	       path('AddBookAction', views.AddBookAction, name="AddBookAction"),
]
