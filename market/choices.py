from django.utils.translation import gettext_lazy as _

HARD_COVER = 'HC'
SOFT_COVER = 'SC'
SPECIAL_COVER = 'SPC'

COVER_CHOICES = [
    (HARD_COVER, _('Hard cover')),
    (SOFT_COVER, _('Soft cover')),
    (SPECIAL_COVER, _('Special cover'))
]