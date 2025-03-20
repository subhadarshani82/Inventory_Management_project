from django.shortcuts import render,redirect
from . models import Product,category_choices
# Create your views here.
def add_product(request):
    if request.method == 'POST':
        name=request.POST['name']
        price=request.POST['price']
        description=request.POST['description']
        category=request.POST['category']
        image=request.FILES.get('image')
        data=Product(name=name,description=description,price=price,category=category,image=image)
        data.save()
        print(name,description,price,image,category)
    return render(request,'product/add_product.html',{'categories':category_choices})
#  retrive products
def productsList(request):
    products=Product.objects.all()
    return render(request,'product/product_list.html',{'products':products})
# update product
def update_product(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        category=request.POST.get('category')
        if request.FILES.get('image'):
            product.image=request.FILES.get('image')
            
        product.name=name
        product.description=description
        product.price=price
        product.category=category
        
        product.save()
        return render(request,'product/update_product.html')
    return render(request,'product/update_product.html',{'product':product,'categories':category_choices})

def deleteProduct(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')