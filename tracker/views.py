from django.shortcuts import render, redirect

def portfolio_list(request):
    # Replace with your real data/model
    stock_data = []
    return render(request, 'tracker/portfolio.html', {'stock_data': stock_data})

def add_stock(request):
    if request.method == "POST":
        # Handle saving new stock (implement as needed)
        return redirect('portfolio_list')
    return render(request, 'tracker/add_stock.html')
