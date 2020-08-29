from django import forms
from trackingsite.models import Bill, Payment


class MyBill(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'amount', 'due_date']


class MyPayment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bill', 'amount', 'date_paid']
