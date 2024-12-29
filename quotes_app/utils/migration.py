import os
import django

from quotes.utils import get_mongodb

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_app.settings")
django.setup()

from quotes.models import Tag, Quote, Author

db = get_mongodb()

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"],
    )
    
quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exists_quote = bool(len(Quote.objects.filter(quote=quote["quote"])))
      
    if not exists_quote:
        author = db.authors.find_one({"_id":quote["author"]})
        a = Author.objects.get(fullname=author["fullname"]) 
        q = Quote.objects.create(
            quote = quote["quote"],
            author = a
        )

        for tag in tags:
            q.tags.add(tag)    
        