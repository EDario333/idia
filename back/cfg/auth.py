AUTH_USER_MODEL = 'users.Users'
# LOGIN_REDIRECT_URL='/dashboard'

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework_simplejwt.authentication.JWTAuthentication',
		# 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication'
	],
}

from datetime import timedelta

JWT_AUTH = {
	'JWT_ALLOW_REFRESH': True,
	'JWT_EXPIRATION_DELTA': timedelta(hours=1),
	'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}