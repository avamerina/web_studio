from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from authentication.serializers import CustomUserSerializer, CustomUserPhotoUpdateSerializer
from utils.uploaders import Uploader


class CustomUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'patch']
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    serializer_action_classes = {
        'photo_update': CustomUserPhotoUpdateSerializer
    }

    @action(methods=['PATCH'], detail=True)
    def set_photo(self, request, *args, **kwargs):
        try:
            image = request.FILES['image']
        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        profile = self.get_object()
        public_uri = Uploader.image_upload(image, image.name)
        serializer = CustomUserPhotoUpdateSerializer(profile, data={"image": public_uri})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "status": "success",
                "data": {"image": serializer.data},
            },
            status=status.HTTP_200_OK,
        )
