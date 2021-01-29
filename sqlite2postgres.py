# -*- coding: utf-8 -*-
import os
import django
import wikidictparser as wdp

import logging

# logging.basicConfig(level=logging.DEBUG)

#  you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rws.settings")
django.setup()


from home.models import BaseMeaning, Word




meanings = BaseMeaning.objects.all()
for meaning in meanings[:10]:
    meaning.save(using='pg')