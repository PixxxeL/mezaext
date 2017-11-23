# -*- coding: utf-8 -*-

from django import forms

class ContactsForm(forms.Form):
    name = forms.CharField(
        label=u'Имя',
        max_length=64,
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=100,
    )
    phone = forms.CharField(
        label=u'Телефон для связи',
        max_length=32,
        required=False,
    )
    text = forms.CharField(
        label=u'Сообщение',
        widget=forms.Textarea,
    )
