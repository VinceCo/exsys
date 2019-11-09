from django import template
from urllib import parse


register = template.Library()


@register.filter(name='citation')
def citation(texte):
    return "&laquo; {} &rlaquo;".format(texte)


@register.filter(name="youtu_url_embeb")
def youtu_url_embeb (url):
    url_data = parse.urlparse(url)
    query = parse.parse_qs(url_data.query)

    try:
        video_id = query["v"][0]
        url_embeb = 'http://youtube.com/embed/%s' % video_id
    except keyError:
        pass

    return url_embeb
