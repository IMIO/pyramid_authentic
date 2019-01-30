# -*- coding: utf-8 -*-

from authomatic.providers.oauth2 import OAuth2

import jwt

__all__ = ['Authentic']


class Authentic(OAuth2):
    """
    Authentic |oauth2| provider.

    Supported :class:`.User` properties:

    * openid
    * email
    * profile
    * roles
    """

    user_authorization_url = 'https://{0}/idp/oidc/authorize/'
    access_token_url = 'https://{0}/idp/oidc/token/'
    user_info_url = 'https://{0}/idp/oidc/user_info/'
    user_info_scope = ['openid', 'email', 'profile', 'roles']

    def __init__(self, *args, **kwargs):
        if 'base_url' in kwargs.keys():
            self.base_url = kwargs['base_url']
            del kwargs['base_url']
        else:
            raise ValueError('base_url parameters should be defined')
        self.set_url(self.base_url)
        super(Authentic, self).__init__(*args, **kwargs)

    def set_url(self, base_url):
        keys = ('user_authorization_url', 'user_info_url', 'access_token_url')
        for key in keys:
            setattr(self, key, getattr(self, key).format(base_url))

    @staticmethod
    def _x_user_parser(user, data):
        encoded = data.get('id_token')
        if encoded:
            payload_data = jwt.decode(
                encoded,
                algorithms=['RS256'],
                options={'verify_signature': False, 'verify_aud': False}
            )
            if 'sub' in payload_data.keys():
                user.id = user.username = payload_data.get('sub')
        if 'sub' in data.keys():
            # user.id = data.get('sub')
            user.id = data.get('email')
            user.first_name = data.get('given_name')
            user.last_name = data.get('family_name')
            fullname = u'{0} {1}'.format(user.first_name, user.last_name)
            if not fullname.strip():
                user.name = user.id
                user.fullname = user.id
            else:
                user.name = fullname
                user.fullname = fullname
                user.username = fullname
            roles = data.get('roles', [])
            if len(roles) > 0:
                if roles[0].get('name') == 'IASmartWeb':
                    user.roles = ['Manager']
        return user


PROVIDER_ID_MAP = [Authentic]
