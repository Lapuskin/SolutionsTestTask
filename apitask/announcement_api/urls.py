from django.urls import path
from rest_framework.routers import SimpleRouter

from announcement_api.api import AnnouncementsDetailAPIView

# Можно так же использоватть роутер с ViewSets:
#
# from announcement_api.api import AnnouncementApiView
#
# router = SimpleRouter()
# router.register('announcements', AnnouncementApiView)
# urlpatterns = router.urls

urlpatterns = [
    path('announcements/<int:pk>', AnnouncementsDetailAPIView.as_view(), name='announcement'),
]