from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from django.views.decorators.csrf import csrf_exempt
from store.PayTm import Checksum
from store.templatetags.cart import cart_count, total_cart_price

MERCHANT_KEY = 'Cy%tG6gzMHNLueH%';


class CheckOut(View):
    def post(self, request):
        yourName = request.POST.get('yourName')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        streetName = request.POST.get('address')
        city = request.POST.get('town_city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(yourName, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          firstName=firstName,
                          lastName=lastName,
                          streetName=streetName,
                          city=city,
                          state=state,
                          pincode=pincode,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            request.session['cart'] = {}
        param_dict = {
            'MID': 'wfrtdQ62096624314391',
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(total_cart_price(products, cart)),
            'CUST_ID': firstName,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
        #
        # return redirect('cart')


class CashOnDelivery(View):
    def post(self, request):
        yourName = request.POST.get('yourName')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        streetName = request.POST.get('address')
        city = request.POST.get('town_city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(yourName, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          firstName=firstName,
                          lastName=lastName,
                          streetName=streetName,
                          city=city,
                          state=state,
                          pincode=pincode,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            request.session['cart'] = {}
            return redirect('cart')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('Order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})
