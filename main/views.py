from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
def show_main(request):
    prod_list = Product.objects.all()
    context = {
        'title': 'Solcaster United',
        'npm' : '2406496233',
        'name': 'Razan Muhammad Salim',
        'class': 'PBP B',
        'prod_list': prod_list
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method =="POST":
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request,id):
    prod = get_object_or_404(Product, pk = id)
    
    context = {
        'prod' : prod
    }
    return render(request, "show_product.html", context)

def show_xml(request):
     prod_list = Product.objects.all()
     xml_data = serializers.serialize("xml", prod_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_xml_by_id(request, prod_id):
   try:
       prod_item = Product.objects.filter(pk=prod_id)
       xml_data = serializers.serialize("xml", prod_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    prod_list = Product.objects.all()
    json_data = serializers.serialize("json", prod_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, prod_id):
   try:
       prod_item = Product.objects.get(pk=prod_id)
       json_data = serializers.serialize("json", [prod_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
# def add_employee(request):
#     employee = Employee.objects.create(name = "razan", age = 19, persona = "persona5")
#     context = {
#         'nama' : employee.name,
#         'umur' : employee.age,
#         'persona' : employee.persona
#     }
#     return render(request,"main.html", context)
    