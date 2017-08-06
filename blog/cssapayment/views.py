# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cssapayment.models import Payment
from django import forms
from django.http import HttpResponseRedirect
def paymentdetail(request, pk):
    pay = Payment.objects.get(pk=int(pk))

    return render(request, "paymentdetail.html", {'pay': pay})


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'uid','gender','paymentway','choicecamp','money' ]
# Create your views here.


def createpayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_pay = form.save()
            return HttpResponseRedirect('/payment/' + str(new_pay.pk))

    form = PaymentForm()
    return render(request, 'create_payment.html', {'form': form})

def totalpayment(request):
    pay =  Payment.objects.all()
    if request.user.is_authenticated:
        return render(request, "total.html", {'pay': pay})
    else:
         return HttpResponseRedirect('/admin/login/?next=%s' % request.path)        
