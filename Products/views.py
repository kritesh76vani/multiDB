from django.shortcuts import render
from django.views import View
from SysProj.settings import DATABASES
from Products.models import Product
# Create your views here.

class ViewAllDB(View):
    def get(self, request):
        return render(request, 'alldb.html', context ={"data": [ key for key in DATABASES ] })

class CreateProduct(View):
    def get(self, request):
        print('db')
        return render(request, 'create_product.html')
    
    # def post(self, request):
    #     Product.objects.using('').create( name = , price = , unit = )