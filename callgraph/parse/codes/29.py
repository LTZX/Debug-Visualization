class Resource(restful.Resource):
    version = 'v3'
    method_decorators = [authenticate, check_version]
    # applies to all inherited resources

