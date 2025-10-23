from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    title = request.POST.get("title")
    price = request.POST.get("price")
    content = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_prod = Product(
        name=title, 
        description=content,
        price = price,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_prod.save()

    return HttpResponse(b"CREATED", status=201)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "all":
        prod_list = Product.objects.all()
    else:
        prod_list = Product.objects.filter(user=request.user)

    context = {
        'title': 'Solcaster United',
        'npm' : '2406496233',
        'name': 'Razan Muhammad Salim',
        'class': 'PBP B',
        'prod_list': prod_list,
        'username' : request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        prod_entry = form.save(commit = False)
        prod_entry.user = request.user
        prod_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

@login_required(login_url='/login')
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
    data = [
        {
            'id': str(prod.id),
            'name': prod.name,
            'price': prod.price,
            'category': prod.category,
            'thumbnail': prod.thumbnail,
            'description': prod.description,
            'is_featured': prod.is_featured,
            'user_id': prod.user_id,
        }
        for prod in prod_list
    ]

    return JsonResponse(data, safe=False)

def show_json_by_id(request, prod_id):
    try:
        prod = Product.objects.select_related('user').get(pk=prod_id)
        data = {
            'id': str(prod.id),
            'name': prod.name,
            'price': prod.price,
            'category': prod.category,
            'thumbnail': prod.thumbnail,
            'description': prod.description,
            'is_featured': prod.is_featured,
            'user_id': prod.user_id,
        }
        return JsonResponse(data)
    
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def edit_product(request, id):
    prod = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=prod)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)


def delete_product(request, id):
    prod = get_object_or_404(Product, pk=id)
    prod.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
