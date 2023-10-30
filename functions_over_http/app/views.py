from django.http.response import HttpResponse

# Create your views here.
def hello_view(request, name):
    return HttpResponse(f"Hey, {name}!")
    

def age_view(request, end, birthyear):
    sum = end - birthyear
    return HttpResponse(sum)
    
def order_total(request, burgers, fries, drinks):
    GoodBurgers1 = (4.50 * burgers)
    FrenchFries1 = (1.50 * fries)
    Drinks1 = (1.00 * drinks)
    Total = GoodBurgers1 + FrenchFries1 + Drinks1
    return HttpResponse(Total)