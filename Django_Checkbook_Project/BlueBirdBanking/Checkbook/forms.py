from django.forms import ModelForm
from .models import Account, Transaction


# Account Form based on the Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Transaction Form based on the Transaction Model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
