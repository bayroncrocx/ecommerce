from django.shortcuts import render, redirect
from carts.models import CartItem
from .models import Order
from .forms import OrderForm
import datetime
from .models import Order, Payment 
import json

def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered = False, order_number=body['orderID'])
    payment= Payment(
        user=request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_is = order.order_total,
        status = body['status'],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    return render(request,'orders/payments.html')



def place_order(request, total = 0, quantity =0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    gran_total = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity  += cart_item.quantity

    tax = (2 * total) / 100
    gran_total = total + tax 

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['first_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.addres_line_1 = form.cleaned_data['addres_line_1']
            data.addres_line_2 = form.cleaned_data['addres_line_2']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.city = form.cleaned_data['city']
            data.orden_note = form.cleaned_data['orden_note']
            data.orden_total = gran_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            yr=int(datetime.date.today().strftime('%Y'))
            mt=int(datetime.date.today().strftime('%m'))
            dt=int(datetime.date.today().strftime('%d'))
            d =datetime.date(yr, mt, dt)

            current_date = d.strftime("%Y%m%d")

            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            contex = {

                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total':gran_total,
            }

            return render(request,'orders/payments.html', contex)
    else:
        return redirect('checkout')    


