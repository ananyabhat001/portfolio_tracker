from django.shortcuts import render, redirect
from .models import Stock
from .alpha_vantage import get_stock_price

def portfolio_list(request):
    stocks = Stock.objects.all()
    computed_stock_data = []
    for stock in stocks:
        live_price = get_stock_price(stock.symbol)
        gain_loss = None
        if live_price is not None:
            gain_loss = (live_price - stock.purchase_price) * stock.quantity
        computed_stock_data.append({
            'user': stock.user,
            'symbol': stock.symbol,
            'quantity': stock.quantity,
            'purchase_price': stock.purchase_price,
            'current_price': live_price,
            'gain_loss': gain_loss,
        })
    return render(request, 'tracker/portfolio.html', {'stock_data': computed_stock_data})

def add_stock(request):
    error_message = None
    if request.method == "POST":
        user = request.POST['user']
        symbol = request.POST['symbol'].upper().strip()
        try:
            quantity = int(request.POST['quantity'])
            purchase_price = float(request.POST['purchase_price'])
            if quantity <= 0 or purchase_price <= 0:
                raise ValueError()
        except ValueError:
            error_message = "Invalid quantity or purchase price."
        live_price = get_stock_price(symbol)
        if not error_message and live_price is None:
            error_message = f"Stock symbol '{symbol}' not found."
        if not error_message:
            Stock.objects.create(user=user, symbol=symbol, quantity=quantity, purchase_price=purchase_price)
            return redirect('portfolio_list')
    return render(request, 'tracker/add_stock.html', {'error': error_message})
