from django.db import models


# Account model
class Account(models.Model):
    # attributes:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # Model Manager instance to perform operations on our database
    Accounts = models.Manager()

    # Customization of how these objects are named in the admin panel
    # Each record/object should be identified by the first and last name
    # of the account holder
    def __str__(self):
        return "{0.first_name} {0.last_name}".format(self)


# Choices for a transaction type
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# Transaction model
class Transaction(models.Model):
    # Attributes:
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Model Manager instance to perform operations on our database
    Transactions = models.Manager()
