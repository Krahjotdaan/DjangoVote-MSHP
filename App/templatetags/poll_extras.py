from django import template
from django import setup

setup()

from App.models import VotedVoting, VoteFact

register = template.Library()

@register.simple_tag
def is_voted(user, voting):
    if VotedVoting.objects.filter(author=user, voting=voting):
        return True
    else:
        return False

@register.simple_tag
def count_voices(variant):
    return len(VoteFact.objects.filter(variant=variant))
