from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Slugged


class BaseBlockCategory(Slugged):
    """Base Category
    """
    class Meta:
        abstract = True


class BlockCategory(BaseBlockCategory):
    """Block Category
    """
    class Meta:
        verbose_name = _('Block category')
        verbose_name_plural = _('Block categories')
