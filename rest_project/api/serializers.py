from rest_framework import serializers
from .models import *

class PurchaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ['name','last_name','email','username','password','password2']

    def save(self, **kwargs):
        account = Account(username=self.validated_data['username'],email=self.validated_data['email'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            return 'password doesnt match'

        account.set_password(password)
        account.save()
        return account