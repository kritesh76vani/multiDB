from django.shortcuts import render
from django.views import View
from SysProj.settings import DATABASES
from Products.models import Product
# Create your views here.

class ViewAllDB(View):
    def get(self, request, slug):
        db = request.user.databases
        return render(request, 'alldb.html', context ={"data": [ key for key in db ] })

class CreateProduct(View):
    def get(self, request, slug):
        return render(request, 'create_product.html' , context = {"db":slug})
    
    def post(self, request, slug):
        data = request.POST
        user_id = request.user.id
        print('user_id',user_id)
        Product.objects.using(slug).create( name = data['name'], price = data['price'], unit = data['unit'])
        return render(request, 'create_product.html' , context = {"db":slug})

class AllProduct(View):
    def get(self, request):
        db1 = Product.objects.using('database1').all()
        db2 = Product.objects.using('database2').all()
        db3 = Product.objects.using('database3').all()
        db4 = Product.objects.using('database4').all()
        db5 = Product.objects.using('database5').all()

        data = {
            "database1":db1,
            "database2":db2,
            "database3":db3,
            "database4":db4,
            "database5":db5,
        }
        
        return render(request, 'all_product.html', context = data)
        