from django.shortcuts import render
def home(requests):
    return render(requests,"calc/home.html")


def calc(requests):
    field1=int(requests.GET["field1"])
    field2=int(requests.GET["field2"])
    operation=requests.GET["optradio"]
    if operation is '+':
        res=field1+field2
    elif operation is '-':
        res=field1-field2
    elif operation is '/':
        res=field1/field2
    else:
        res=field1*field2
    return render(requests,"calc/calc.html",{"result":res})
