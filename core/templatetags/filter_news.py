from django import template

register = template.Library()


@register.filter(name='filter_sapo')
def filter_sapo(value):
	return value[:100] + '...'
