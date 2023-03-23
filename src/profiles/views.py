from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from .models import UserNet
from .serializers import GetUserNetSerializer


class GetUserNetView(RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetSerializer


class UpdateUserNetView(UpdateAPIView):
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]
