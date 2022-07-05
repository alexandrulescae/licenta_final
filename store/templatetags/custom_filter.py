from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return str(number)+" LEI"



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1
