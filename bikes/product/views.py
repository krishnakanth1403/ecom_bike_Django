from django.shortcuts import render
from product.models import Product, CompanyCategory
from django.views import View, generic
# Create your views here.
def index(request):
    return render(request, 'product/index.html')

# def categories(request, id):
#     if CompanyCategory.objects.filter(id = id):
#         posts = Product.objects.all()
#         category = CompanyCategory.objects.all()
        
#     else:
#         posts = Product.objects.all()
#         category = CompanyCategory.objects.filter(id = id)
#         print(category)
#     return render(request, "product/category.html", context = {"posts":posts, "category":category})

def categories(request,id):
    if CompanyCategory.objects.filter(id=id):
        products = Product.objects.filter(company_category_id=id)
        categories = CompanyCategory.objects.all()
        print(categories)
    return render(request,"product/category.html", context={"products": products, "categories": categories}) 

# class ProductDetailView(generic.DetailView):
#     model = Product
#     queryset = Product.objects.get(pk=id)
#     template_name = "product/single.html"

def product_detail(request, id):
    category = CompanyCategory.objects.all()
    products = Product.objects.get(pk=id)
    print(category)
    print(products)
    context = {'products':products, 'category':category}
    return render(request,'product/single.html',context)

