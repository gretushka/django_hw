from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    ab_test=request.GET.get('from-landing','noname')
    if ab_test == 'original':
        counter_click[1]+=1
    else:
        if ab_test == 'test':
            counter_click[2]+=1
    return render_to_response('index.html')


def landing(request):
    ab_test=request.GET.get('ab_test_arg','noname')
    if ab_test == 'original':
        counter_show[1]+=1
    else:
        if ab_test == 'test':
            counter_show[2]+=1
            return render_to_response('landing_alternate.html')
    return render_to_response('landing.html')


def stats(request):
    if counter_show[1] == 0:
        stat_original = 0
    else:
        stat_original=counter_click[1]/counter_show[1]

    if counter_show[2] == 0:
        stat_test = 0
    else:
        stat_test=counter_click[2]/counter_show[2]

    return render_to_response('stats.html', context={
        'test_conversion': stat_test,
        'original_conversion': stat_original,
    })
