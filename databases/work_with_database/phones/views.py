from django.shortcuts import render
from phones.models import Phone
from phones.management.commands.import_phones import Command

def show_catalog(request):
    template = 'catalog.html'
    Command.handle(request)
    context = {'phones': Phone.objects.all()}
    if request.GET.get('sort')=="name":
        context = {'phones': Phone.objects.order_by("name")}
    else:
        if request.GET.get('sort')=="min_price":
            context = {'phones': Phone.objects.order_by("price")}
        else:
            if request.GET.get('sort')=="max_price":
                context = {'phones': Phone.objects.order_by("-price")}


    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    if Phone.objects.filter(slug=slug):
        phone = Phone.objects.get(slug=slug)
    else:
        phone = None
    context = {'phone':phone}
    return render(request, template, context)
