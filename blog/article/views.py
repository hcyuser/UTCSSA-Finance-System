# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from article.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'uid','filldate','applycost','content', 'upload',]
        widgets = {
          'title': forms.Textarea(attrs={'rows':4, 'cols':60}),
          'content': forms.Textarea(attrs={'rows':2, 'cols':60}),
        }

def detail(request, pk):
    article = Article.objects.get(pk=int(pk))
    return render(request, "detail.html", {'article': article})
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))

    form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})


def home(request):
    article =  Article.objects.all()
    return render(request, "index.html", {'article': article})
