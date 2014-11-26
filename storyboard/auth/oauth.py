
from storyboard.openstack.common.apiclient import auth


class OAuthPlugin(auth.BaseAuthPlugin):

    def _do_authenticate(self, http_client):
        pass

    def __init__(self, api_url=None, access_token=None):
        super(OAuthPlugin, self).__init__()

        self.api_url=api_url
        self.access_token=access_token

    def token_and_endpoint(self, endpoint_type=None, service_type=None):
        return self.access_token, self.api_url
