from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.contrib import messages
from .models import Bill, Payment
from django.forms.models import model_to_dict
from .forms import MyBill, MyPayment
from datetime import datetime


class BillView(generic.ListView):
    model = Bill


class BillCreate(generic.CreateView):
    model = Bill
    fields = ('name', 'amount', 'due_date')
    success_url = reverse_lazy('bill-list')


class BillUpdate(generic.UpdateView):
    model = Bill
    fields = ('name', 'amount', 'due_date')
    success_url = reverse_lazy('bill-list')


class BillDelete(generic.DeleteView):
    model = Bill
    success_url = reverse_lazy('bill-list')
    success_message = f"Bill was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BillDelete, self).delete(request, *args, **kwargs)


class PaymentCreate(generic.TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.template_name = "trackingsite/payment_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, **kwargs):
        context = self.get_context_data()
        obj = get_object_or_404(Bill, pk=self.kwargs.get('pk'))
        context['form'] = MyBill(initial=obj.__dict__)
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d')

        bill_name = request.POST.get("name")
        date_paid = formatted_date
        amount = request.POST.get("amount")

        payment = Payment(amount=amount, date_paid=date_paid)
        payment.bill = Bill.objects.get(name=bill_name)
        payment.save()

        messages.success(request, f'Payment for {bill_name} saved successfully!')

        return HttpResponseRedirect(reverse_lazy('bill-list'))

