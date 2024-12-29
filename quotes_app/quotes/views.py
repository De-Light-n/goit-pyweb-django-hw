from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
from .utils import *


# Create your views here.
def main(request, page=1):
    quotes = Quote.objects.filter().all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    tags_top = get_top_10_tags()
    return render(
        request,
        "quotes/index.html",
        context={"quotes": quotes_on_page, "top_tags": tags_top},
    )


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "quotes/author.html", context={"author": author})


def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    quotes = Quote.objects.filter(tags=tag)
    tags_top = get_top_10_tags()
    return render(
        request,
        "quotes/tag.html",
        context={"tag": tag, "quotes": quotes, "top_tags": tags_top},
    )


@login_required
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/tag_input.html", {"form": form})
    return render(request, "quotes/tag_input.html", {"form": TagForm()})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/author_input.html", {"form": form})
    return render(request, "quotes/author_input.html", {"form": AuthorForm()})


@login_required
def add_quote(request):
    tags = Tag.objects.filter().all()
    authors = Author.objects.filter().all()
    
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            
            author_id = request.POST["author"]
            author_choise = Author.objects.filter(pk=author_id).first()
            new_quote.author = author_choise
            
            new_quote.save()
            
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
                
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/quote_input.html", {"form": form, "tags":tags, "authors":authors})
    return render(request, "quotes/quote_input.html", {"form": QuoteForm(), "tags":tags, "authors":authors})
    
