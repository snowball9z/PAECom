from django.shortcuts import render
from apps.store.models import Product, Category

# Create your views here.


def Frontpage(request):
    products = Product.objects.filter(is_featured = True)
    featuredCategories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_view_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'products': products,
        'featuredCategories': featuredCategories,
        'popular_products': popular_products,
        'recently_view_products': recently_view_products
    }

    return render(request, 'frontpage.html', context)

def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')