from datetime import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from blog.models import News
from blog.models import Story
from blog.models import StoryPage
from blog.models import Sketch
from blog.models import Comment
from blog.models import Item
from blog.models import Animation
from blog.models import MakingOf
from blog.models import MakingOfItem
from blog.models import MakingOfText
from blog.models import MakingOfFigure

from blog.forms import CommentForm



def view_home(request):
    page = request.GET.get('page')
    news =  News.objects.order_by('-date')
    list_news = make_page(request, news, 5)

    return render(request, 'blog/home.html', {
        'items_list': list_news,
        })


def view_redirect_home(request):
    return redirect('home')


def view_sketches(request):
    sketches = Sketch.objects.order_by('-date')
    sketches_list = make_page(request, sketches, 5)

    return render(request, 'blog/sketches.html', {
        'items_list': sketches_list,
        })


def view_animations(request):
    animations =  Animation.objects.order_by('-date')
    animations_list = make_page(request, animations, 5)

    return render(request, 'blog/animations.html', {
                  'items_list': animations_list,
    })


def view_contact(request):
    return render(request, 'blog/contact.html', locals())


def view_stories(request):
    stories = Story.objects.order_by('-date')
    stories_list = make_page(request, stories, 5)

    return render(request, 'blog/stories.html', {
        'items_list': stories_list,
        })


def view_show_story(request, id_title):
    story = Story.objects.get(title=id_title)
    pages = story.storypage_set.all()
    pages_list = make_page(request, pages, 2)

    return render(request, 'blog/show_story.html', {
        'items_list': pages_list,
        'story_title': story.title,
        })


def view_comment(request, id_title):
    form = CommentForm(request.POST or None)
    bool_sent = False
    item = Item.objects.get(title=id_title)
    comments_list = item.comment_set.all()

    if form.is_valid():
        comment = form.save(commit=False)
        comment.item = item
        comment.save()
        bool_sent = True

    return render(request, 'blog/comment.html', locals())


def make_page(request, list, num_item):
    page = request.GET.get('page')
    paginator = Paginator(list, num_item)

    return paginator.get_page(page)

def making_of(request):
    making_of_list = MakingOf.objects.all()
    return render(request, 'blog/making_of.html', {
        'items_list': making_of_list,
        })

def show_making_of(request, id_title):
    making_of = MakingOf.objects.get(title=id_title)
    making_of_items = making_of.makingofitem_set.all()
    making_of_texts = MakingOfText.objects.filter(making_of__title=making_of.title)
    making_of_figures = MakingOfFigure.objects.filter(making_of__title=making_of.title)
    items_list = []

    # This block is sorting texts and figures
    for k in range(0, len(making_of_items)):
        q_item_text = making_of_texts.filter(item_nb=k)
        q_item_figure = making_of_figures.filter(item_nb=k)
        if q_item_text.exists():
            items_list.append(q_item_text[0])
        if q_item_figure.exists():
            items_list.append(q_item_figure[0])

    return render(request, 'blog/show_making_of.html', locals())
