@endpoints.record
def record_params(setup_state):
    """ Load used app configs into local config on registration from
    server/__init__.py """
    app = setup_state.app
    endpoints.config['tz'] = app.config.get('TIMEZONE', 'utc')  # sample config


api = restful.Api(endpoints, catch_all_404s=True)

API_VERSION = 'v3'


