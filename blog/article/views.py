# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django import forms
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'uid','filldate','applycost','content', ]
        widgets = {
          'title': forms.Textarea(attrs={'rows':4, 'cols':60}),
          'content': forms.Textarea(attrs={'rows':2, 'cols':60}),
        }

def detail(request, pk):
    article = Article.objects.get(pk=int(pk))
    return render(request, "detail.html", {'article': article})
# Create your views here.

from django.http import HttpResponseRedirect
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))

    form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})
