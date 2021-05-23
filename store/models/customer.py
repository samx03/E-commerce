from django.db import models


class Customer(models.Model):
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=15, default='')
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def __str__(self):
        return self.username


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False

    def isEmailExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def isPhoneExists(self):
        if Customer.objects.filter(phone=self.phone):
            return True

        return False

    def isUsernameExists(self):
        if Customer.objects.filter(username=self.username):
            return True

        return False
