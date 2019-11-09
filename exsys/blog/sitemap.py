from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Sketch
from blog.models import Story
from blog.models import StoryPage
from blog.models import Animation
from blog.models import News


class SketchSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Sketch.objects.filter()

    def lastmod(self, obj):
        return obj.date


class StorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Story.objects.filter()

    def lastmod(self, obj):
        return obj.date


class StoryPageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return StoryPage.objects.filter()

    def lastmod(self, obj):
        return obj.story.date


class AnimationSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Animation.objects.filter()

    def lastmod(self, obj):
        return obj.date


class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return News.objects.filter()

    def lastmod(self, obj):
        return obj.date


class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['contact']

    def location(self, item):
        return reverse(item)
