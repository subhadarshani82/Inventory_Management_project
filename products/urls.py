from django.urls import path
from. import views
urlpatterns=[
    path('add_product',views.add_product,name='add_product'),
    path('product_list/',views.productsList,name='product_list'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('delete_product/<int:id>',views.deleteProduct,name='delete_product'),
]