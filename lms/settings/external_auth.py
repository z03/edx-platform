import os

############################ OpenID Provider  ##################################
if os.getenv('TESTING'):
    OPENID_PROVIDER_TRUSTED_ROOTS = ['*']
else:
    OPENID_PROVIDER_TRUSTED_ROOTS = ['cs50.net', '*.cs50.net']


OPENID_CREATE_USERS = False
OPENID_UPDATE_DETAILS_FROM_SREG = True
OPENID_USE_AS_ADMIN_LOGIN = False