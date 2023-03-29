from django.shortcuts import render, redirect
from product.models import *
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def common_data(request,getProduct=None):
    sizes = []
    size = product_variants.objects.filter(variant_id=1)
    for sz in size:
        sizes.append(sz.variant_title.upper())
    my_set = set(sizes)
    size = list(my_set)
    colors = []
    color = product_variants.objects.filter(variant_id=2)
    for clr in color:
        colors.append(clr.variant_title.capitalize())
    my_set = set(colors)
    color = list(my_set)
    styles = []
    style = product_variants.objects.filter(variant_id=3)
    for stl in style:
        styles.append(stl.variant_title.capitalize())
    my_set = set(styles)
    style = list(my_set)

    if getProduct is None:
        all_products = products.objects.all()
    else:
        all_products = getProduct
    variant_list = {}
    records_all = {}

    paginator = Paginator(all_products, 5)
    page = request.GET.get('page')
    my_data = paginator.get_page(page)
    all_products = products.objects.all()

    count = products.objects.all().count()
    for product in all_products:
        start = 0
        prod_info = {}
        vairent_price_info = []
        vairent_price_info.append(product.title)
        vairent_price_info.append(product.description)
        start = start + 1
        prod_info[start] = vairent_price_info
        vairent_price_info = []
        vairent_price = product_variants_prices.objects.filter(product=product.id)
        for price in vairent_price:
            prod_variants1 = product_variants.objects.get(id=price.product_variant_one_id)
            prod_variants2 = product_variants.objects.get(id=price.product_variant_two_id)
            prod_variants3 = product_variants.objects.get(id=price.product_variant_three_id)
            vairent_price_info.append(prod_variants1.variant_title.upper())
            vairent_price_info.append(prod_variants2.variant_title.capitalize())
            vairent_price_info.append(prod_variants3.variant_title.capitalize())
            vairent_price_info.append(price.price)
            vairent_price_info.append(price.stock)
            start = start+1
            prod_info[start]=vairent_price_info
            vairent_price_info = []
        records_all[product.id] =  prod_info
    context = {
        'all_variants': variant_list,
        'records_all':records_all,
        'color':color,
        'size': size,
        'style': style,
        'count': count,
        'my_data':my_data,
    }
    return context
def product_list(request):
    return render(request,'products/list.html',common_data(request))

def find_product(request):
    if request.method == 'POST':
        title = request.POST['title']
        variant = request.POST['variant']
        price_from = request.POST['price_from']
        price_to = request.POST['price_to']
        date = request.POST['date']

        variant_list =[]
        prod = []
        variant = product_variants.objects.filter(variant_title=str(variant).lower())
        for var in variant:
            variant_list.append(str(var.id))

        prod_variants_prices = product_variants_prices.objects.filter(Q(product_variant_one__in= variant_list) | Q(product_variant_two__in= variant_list) | Q(product_variant_three__in= variant_list))
        for prods in prod_variants_prices:
            prod.append(prods.product_id)
        my_set = set(prod)
        prod = list(my_set)
        try:
            prod_variants_prices = product_variants_prices.objects.filter(Q(price__gte= int(price_from)) & Q(price__lte= int(price_to)))
            for prods in prod_variants_prices:
                prod.append(prods.product_id)
        except:
            print('Error')
        my_set = set(prod)
        prod_price = list(my_set)
        print(prod_price)
        all_products = products.objects.filter(
           Q(title__icontains= title) & Q(id__in= prod) & Q(id__in= prod_price)  & ( Q(created_at__icontains= date) | Q(updated_at__icontains= date))
        )
        return render(request,'products/list.html',common_data(request,all_products))


def add_product(request):
    pass


