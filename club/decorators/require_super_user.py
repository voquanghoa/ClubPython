from django.core.exceptions import PermissionDenied


def superuser_only(function):
    def _inner(api_view, *args, **kwargs):
        if not api_view.request.user.is_superuser:
            raise PermissionDenied()
        return function(api_view, *args, **kwargs)

    return _inner
