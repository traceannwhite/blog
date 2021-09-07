from .models import BlogPost
from rest_framework import viewsets, permissions
from .serializers import BlogPostSerializers
# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [permissions.AllowAny]
