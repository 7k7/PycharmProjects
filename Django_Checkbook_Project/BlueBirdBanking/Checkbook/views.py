from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.
def home(request):
    # create an Account Form to pass along
    # to index.html to create a dropdown list
    # of accounts
    form = TransactionForm(data=request.POST or None)
    if request.method == "POST":
        pk = request.POST['account']
        return balance(request, pk)
    content = {
        'form': form
    }
    return render(request, 'checkbook/index.html', content)


def create_account(request):
    # Retrieve the Account form
    form = AccountForm(data=request.POST or None)
    # Checks if the request method is POST
    if request.method == 'POST':
        # Proceeds to save the Account form if and only if
        # the submitted form is valid
        if form.is_valid():
            form.save()
            return redirect('index')
    # Store Account form data in a dictionary variable
    content = {'form': form}
    # Adds content (if any) of form to the page
    return render(request, 'checkbook/CreateNewAccount.html', content)


def balance(request, pk):
    # Retrieves Account by primary key
    account = get_object_or_404(Account, pk=pk)
    # Retrieves all transactions with primary key
    transactions = Transaction.Transactions.filter(account=pk)
    # Retrieves the account's initial deposit balance
    current_total = account.initial_deposit
    # Dictionary contains all transactions
    table_contents = {}
    # Loop through transactions and determines which are deposit
    # or withdrawal type
    for t in transactions:
        # Add to total amount if 'Deposit'
        if t.type == 'Deposit':
            current_total += t.amount
            # Add transaction and amount to the dictionary
            table_contents.update({t: current_total})
        # Subtract from current_total if type is 'withdrawal'
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    # Pass account, account total balance, and transaction information to the template
    content = {
        'account': account,
        'table_contents': table_contents,
        'balance': current_total
    }
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    # Retrieve the Transaction form input if none, just instantiate an empty one
    form = TransactionForm(data=request.POST or None)
    # Checks if method is POST
    if request.method == 'POST':
        # Saves given form if and only if the form has been validated
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    # Adds Transaction form to this dictionary variable
    content = {'form': form}
    # Passes along form content and request along with rendering the web page
    return render(request, 'checkbook/AddTransaction.html', content)
