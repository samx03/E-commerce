from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        phone = postData.get('phone')
        username = postData.get('username')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'phone': phone,
            'username': username,
            'email': email,
        }
        error_message = None

        customer = Customer(phone=phone,
                            email=email,
                            username=username,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            print(phone, username, email, password)
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('productpage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if not customer.phone:
            error_message = "Phone NO. required.."
        elif len(customer.phone) < 10:
            error_message = 'Invalid Phone No.'
        elif not customer.username:
            error_message = "Username Required.."
        elif len(customer.username) < 4:
            error_message = 'Username must be greater than 4 characters'
        elif not customer.email:
            error_message = "Email Required.."
        elif not customer.password:
            error_message = "Password Required.."
        elif len(customer.password) < 4:
            error_message = 'Password should contain more than 4 characters'
        elif customer.isEmailExists():
            error_message = 'Email address already registered..'
        elif customer.isPhoneExists():
            error_message = 'Phone No. already registered..'
        elif customer.isUsernameExists():
            error_message = 'Username already registered'

        return error_message
