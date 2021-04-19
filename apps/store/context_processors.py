from .models import Category

def Menu_Categories(request):
    categories = Category.objects.filter(parent=None)
    context = {
        'categories': categories
    }
    return context