    def get(self, user):
        return {
            'version': API_VERSION,
            'url': '/api/{}/'.format(API_VERSION),
            'documentation': 'http://github.com/Cal-CS-61A-Staff/ok/wiki'
        }

#  Fewer methods/APIs as V1 since the frontend will not use the API
#  TODO Permsisions for API actions


