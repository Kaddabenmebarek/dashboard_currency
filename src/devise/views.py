from django.shortcuts import render, redirect
import api


# Create your views here.

def redirect_home(request):
    return redirect("home", days_range=30, currencies="CHF")
def dashboard(request, days_range=30, currencies="USD"):
    days, rates = api.get_rates(currencies=currencies.split(","), since_days=days_range)
    page_label = {7:"Week", 30:"Month", 365:"Year"}.get(days_range, "Custom")
    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "page_label": page_label,
                                                         "currencies": currencies})
