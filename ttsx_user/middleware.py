class UrlMiddleware():
    def process_view(self, request, view_name, view_args, view_kwargs):
        if request.path not in ['/user/login/',
                                '/user/logout/',
                                '/user/login_handle/',
                                '/user/register_handle',
                                '/user/register/',
                                '/user/register_valid/',
                                '/user/islogin/',
                                ]:
            request.session['url_path'] = request.get_full_path()
