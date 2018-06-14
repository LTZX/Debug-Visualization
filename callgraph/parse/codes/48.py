    def make_response(self, data, *args, **kwargs):
        data = {'data': data}
        return super().make_response(data, *args, **kwargs)

