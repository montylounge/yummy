from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _

class Bookmark(models.Model):
    title = models.CharField(_('title'), max_length=255)
    url = models.URLField(_('url'), verify_exists=False, max_length=255)
    owner = models.ForeignKey('auth.user')
    pub_date = models.DateTimeField(_('pub_date'), auto_now_add=True)
    edit_date = models.DateTimeField(_('edit_date'), auto_now=True)
    description = models.TextField(_('description'), blank=True)
    private = models.BooleanField(_('private'), default=False)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
