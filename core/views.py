from django.shortcuts import render
from django.http import HttpResponse

from core.models import (
    Category,
    Tags,
    Vendor,
    Product,
    ProductImages,
    CartOrder,
    CartOrderItem,
    ProductReview,
    WishList,
    Address,
)


def index(request):

    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(
        featured=True, product_status="published"
    ).order_by("-id")

    context = {"user": request.user, "products": products}
    return render(request, "core/index.html", context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    context = {"products": products}
    return render(request, "core/product-list.html", context)