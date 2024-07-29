from rest_framework import viewsets, generics

from announcement_api.models import Announcement
from announcement_api.serializers import AnnouncementSerializer

#
# class AnnouncementApiView(viewsets.ModelViewSet):
#     http_method_names = ['get']
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# Так как речь в Тестовом Задании шла только о DetailView, я использовал RetrieveAPIView.
# Для Detail + List можно использовать код, закомментированный выше.
class AnnouncementsDetailAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
