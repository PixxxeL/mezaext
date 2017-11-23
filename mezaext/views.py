# -*- coding: utf-8 -*-

import time
import datetime

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .forms import ContactsForm


SITE_TITLE = settings.SITE_TITLE

def contacts_form(request):
    slug = getattr(settings, 'CONTACTS_FORM_REDIRECT_SLUG', '')
    response = HttpResponseRedirect(reverse('page', kwargs={'slug': slug}))
    key = 'contacts_form_ts'
    session_ts = float(request.session.get(key, 0))
    now_ts = time.mktime(datetime.datetime.now().timetuple())
    if session_ts + 60 * 15 > now_ts:
        return response
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid() and form.cleaned_data['text'].strip():
            recipients = getattr(settings, 'CONTACTS_FORM_EMAILS', [])
            if recipients:
                send_mail(
                    u'Сообщение от пользователя сайта %s' % SITE_TITLE,
                    render_to_string('mezaext/contacts_email.txt', {'form' : form}),
                    settings.DEFAULT_FROM_EMAIL,
                    recipients,
                    #fail_silently=False,
                )
            send_mail(
                u'Ваше сообщение принято на сайт %s' % SITE_TITLE,
                _get_user_notify_text(),
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
                #fail_silently=False,
            )
            request.session[key] = now_ts
    return response


def _get_user_notify_text():
    return u'''Спасибо за обращение в компанию!

Мы подготовим ответ на ваше сообщение в течение трех рабочих дней
и свяжемся по тем контактным данным, которые вы оставили.

С уважением,
%s''' % SITE_TITLE
