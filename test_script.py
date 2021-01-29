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

BaseMeaning.objects.all().delete()


word_file = 'words.txt'
items = []
with open('word_list.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    items = [item.split()[0] for item in lines]

# exit(0)

parser = wdp.get_parser('pl')
for item in items:
    print(item)
    try:
        word_data = parser.fetch_by_meaning(item)
    except Exception:
        print('Could not parse %s' % item)
        continue
    for key in word_data:
        # print(key)
        bm = word_data[key]
        new_base_meaning = BaseMeaning(global_id=bm['global_id'], part_of_speech=bm['część_mowy/part_of_speech'], text=bm['tekst/text'])
        new_base_meaning.save()
        if (bm['odmiana']=='nieodmienny' or bm['odmiana']=='specjalne' or bm['odmiana'] is None):
            new_word = Word(word=item, basemeaning=new_base_meaning, labels='nieodmienny/specjalne')
            new_word.save()
        else:
            # print(bm['odmiana'])
            for col_key in bm['odmiana']:
                for row_key in bm['odmiana'][col_key]:
                    if isinstance(bm['odmiana'][col_key][row_key], list):
                        label = col_key + '+' + row_key
                        for word in bm['odmiana'][col_key][row_key]:
                            new_word = Word(word=word, basemeaning=new_base_meaning, labels=label)
                            new_word.save()
