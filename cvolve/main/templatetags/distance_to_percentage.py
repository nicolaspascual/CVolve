from django import template
from cvolve.main.services import calculate_percentage_distance

register = template.Library()

@register.filter(name='distance_to_percentage')
def distance_to_percentage(distance):
    return calculate_percentage_distance(distance)