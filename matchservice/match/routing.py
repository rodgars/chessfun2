from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r'ws/matchfinder/u/(?P<user_name>\w+)/s/(?P<score>\w+)/$',
        consumers.MatchFinderConsumer.as_asgi()
    ),
    re_path(r'ws/match/(?P<match_code>\w+)/$', consumers.MatchConsumer.as_asgi())
]
