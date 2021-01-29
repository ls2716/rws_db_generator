from django.shortcuts import render
from.models import Word, BaseMeaning
# Create your views here.
def word_view(request, query):
    result = Word.objects.filter(word=query)
    print(result)
    if result==None:
        result = {}
    context = {'query': query,
                'result': result,}
    return render(request, 'home/word_view.html', context)

def meaning_view(request, query):
    result = Word.objects.filter(word=query)
    meanings = {}
    for q in result:
        if q.basemeaning.global_id in meanings.keys():
            meanings[q.basemeaning.global_id].append(q)
        else:
            meanings[q.basemeaning.global_id]=[q]
    print(meanings)
    if result==None:
        result = {}
    context = {'query': query,
                'result': result,
                'meanings': meanings}
    return render(request, 'home/meaning_view.html', context)