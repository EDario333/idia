from django.utils.translation import gettext as _

MIN_LENGTH_TEXT_FIELDS=3
MAX_LENGTH_TEXT_FIELDS=1024
MIN_LENGTH_VARCHAR_FIELDS=3
MAX_LENGTH_VARCHAR_FIELDS=254
MIN_LENGTH_PHONE_FIELDS=10
MAX_LENGTH_PHONE_FIELDS=13

UNDEFINED_LBL = "-- " + _("Prefer not to say") + " --"

GENDERS = (
	(' ', UNDEFINED_LBL),
  ('M', _("Male")),
  ('F', _("Female")),
)

SOCIAL_NETWORKS = (
  ('1', _("Facebook")),
  ('2', _("Twitter")),
  ('3', _("Instagram")),
  ('4', _("Snapchat")),
)