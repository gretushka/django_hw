from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    session_key = 'reviewed_products'
    review_list = request.session.get(session_key, False)
    print(review_list)
    if review_list:
        #request.session[session_key] = None
        is_review_exist = bool(review_list.count(pk))
    else:
        is_review_exist = False
    context = {
        'product': product,
        'is_review_exist': is_review_exist,
        'reviews': product.review_set.all()
    }
    if request.method == 'POST':
        # логика для добавления отзыва
        form = ReviewForm(request.POST)

        if form.is_valid():
            frm = form.save(commit=False)
            frm.product = product
            frm.save()

            if review_list:
                review_list.append(pk)
                request.session[session_key] = review_list
            else:
                request.session[session_key] = [pk]

            context['is_review_exist'] = True
    else:
        context['form'] = ReviewForm()

    return render(request, template, context)
