from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# Create your views here.


def order_create(request):
    if not request.user.is_authenticated:
        # Можно вернуть сообщение или редирект
        return redirect('login')  # или render с сообщением
    # остальной код
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request=request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'order/created.html',
                          {'order': order,
                           'form': form})
    else:
        form = OrderCreateForm(request=request)
    return render(request, 
                  'order/create.html',
                  {'cart': cart,
                   'form': form})
