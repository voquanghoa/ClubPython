from django.core.exceptions import PermissionDenied

from club.models.user import Profile


def superuser_only(fnc):
    def _inner(api_view, *args, **kwargs):
        if not api_view.request.user.is_superuser:
            raise PermissionDenied()
        return fnc(api_view, *args, **kwargs)

    return _inner


def has_profile(fnc):
    def _inner(api_view, *args, **kwargs):
        user = api_view.request.user

        if user is None or not user.is_active:
            raise PermissionDenied()

        profile = Profile.objects.get(user=user)

        if profile is None:
            raise PermissionDenied()

        api_view.request.profile = profile

        return fnc(api_view, *args, **kwargs)

    return _inner
