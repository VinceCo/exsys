from django.conf.urls import url
from django.urls import path
from django.contrib.sitemaps.views import sitemap

from blog import views
from blog.sitemap import SketchSitemap
from blog.sitemap import StorySitemap
from blog.sitemap import StoryPageSitemap
from blog.sitemap import AnimationSitemap
from blog.sitemap import NewsSitemap
from blog.sitemap import StaticViewSitemap


sitemaps = {'sketch': SketchSitemap,
            'story': StorySitemap,
            'story_page': StoryPageSitemap,
            'animation': AnimationSitemap,
            'News': NewsSitemap,
            'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', views.view_redirect_home),
    url(r'^home/?$', views.view_home, name ='home'),
    url(r'^stories/?$', views.view_stories, name='stories'),
    url(r'^animations/?$', views.view_animations, name='animations'),
    url(r'^story/(?P<id_title>[\w\s]*)/?$', views.view_show_story, name='show_story'),
    url(r'^sketches/?$', views.view_sketches, name='sketches'),
    url(r'^contact/?$', views.view_contact, name='contact' ),
    url(r'^comment/(?P<id_title>[\w\s]+)/?$', views.view_comment, name='comment'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
