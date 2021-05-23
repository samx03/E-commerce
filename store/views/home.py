from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.topSelling import top_Products
from store.models.category import Category
from django.views import View


# Create your views here.
def index(request):
    top = top_Products.get_all_top_Products();
    print(top)
    return render(request, 'index.html', {'top': top})


class Items(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('Cart: ', request.session['cart'])
        return redirect('productpage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('You are: ', request.session.get('username'))
        return render(request, 'product.html', data)


# def product_detail(request):
#     return render(request, 'product-detail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product-detail.html', {'product': product})


def about_us(request):
    return render(request, 'About-us.html')


def contact_us(request):
    return render(request, 'Contact-us.html')
