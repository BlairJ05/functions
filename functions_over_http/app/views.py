from django.http.response import HttpResponse

# This function asks for name then returns 'Hey, (name)'.
def hello_view(request, name):
    return HttpResponse(f"Hey, {name}!")
    
# This has three arguments. one is the standard https request and the other two are asking for a random year then your birth year. it will return the sum of the random year minus your birth year.
def age_view(request, end, birthyear):
    sum = end - birthyear
    return HttpResponse(sum)
#  This will calculate and return the total of burgers, drinks, or fried inputed throught the url.  
def order_total(request, burgers, fries, drinks):
    GoodBurgers1 = (4.50 * burgers)
    FrenchFries1 = (1.50 * fries)
    Drinks1 = (1.00 * drinks)
    Total = GoodBurgers1 + FrenchFries1 + Drinks1
    return HttpResponse(Total)