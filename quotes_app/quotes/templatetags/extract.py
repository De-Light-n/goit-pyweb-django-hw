from bson.objectid import ObjectId
from django import template

from quotes.models import Author

register = template.Library()

def get_author(id_):
    author = Author.objects.filter(pk=id_).first()
    return author.fullname

register.filter("author", get_author)
