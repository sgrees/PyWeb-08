from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from myblog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Posts Feeds"
    link = "/posts/rss/"
    description = "New blog posts."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])
