from django.shortcuts import render, redirect
from .models import Portfolio
from .alpha_vantage import get_stock_price

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    stock_data = []
    for p in portfolios:
        current_price = get_stock_price(p.stock_symbol)
        gain_loss = ((current_price - p.purchase_price) * p.quantity) if current_price else None
        stock_data.append({
            'symbol': p.stock_symbol,
            'quantity': p.quantity,
            'purchase_price': p.purchase_price,
            'current_price': current_price,
            'gain_loss': gain_loss,
        })
    return render(request, 'tracker/portfolio.html', {'stock_data': stock_data})

def add_stock(request):
    if request.method == 'POST':
        user = request.POST['user']
        symbol = request.POST['symbol']
        quantity = int(request.POST['quantity'])
        purchase_price = float(request.POST['purchase_price'])
        Portfolio.objects.create(
            user=user, 
            stock_symbol=symbol, 
            quantity=quantity, 
            purchase_price=purchase_price
        )
        return redirect('portfolio_list')
    return render(request, 'tracker/add_stock.html')
