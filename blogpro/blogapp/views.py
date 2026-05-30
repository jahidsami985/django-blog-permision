from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Category


def category_list(request):
    qs = Category.objects.all().order_by('-created_at')
    q = request.GET.get('q')
    if q:
        qs = qs.filter(name__icontains=q)

    paginator = Paginator(qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': page_obj.object_list,
        'is_paginated': page_obj.has_other_pages(),
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'blogapp/category_list.html', context)


def category_create(request):
    # Placeholder: redirect to list for now
    return redirect('blogapp:category_list')


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blogapp/category_detail.html', {'category': category})


def category_edit(request, pk):
    # Placeholder: redirect back to detail
    return redirect('blogapp:category_detail', pk=pk)


def category_delete(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=pk)
        category.delete()
    return redirect('blogapp:category_list')
