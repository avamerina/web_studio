from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.models import Order, File
from orders.serializers import OrderSerializer, FileSerializer
from utils.uploaders import Uploader
from orders.services import get_order_by_slug


class OrderViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = OrderSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            queryset = Order.objects.filter(user__isnull=True)
        else:
            queryset = Order.objects.filter(Q(user__isnull=True) | Q(user_id=self.request.user))
        return queryset

    @action(methods=['GET'], detail=False)
    def my_orders(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user_id=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class FileViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('url')
        order_slug = request.data.get('order')
        try:
            order = get_order_by_slug(order_slug)
        except Exception as e:
            return Response(data={"error": f' {e}'}, status=status.HTTP_404_NOT_FOUND)

        created_files = []

        if images:
            for image in images:
                public_uri = Uploader.image_upload(image, image.name)
                file = {
                    "order": order.slug,
                    "url": public_uri
                }
                created_files.append(file)
            serializer = self.get_serializer(
                data=created_files,
                many=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                data={
                    "status": "success",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                data={
                    "error": "No file uploaded",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
