from .models import BlogPost
from rest_framework import serializers

class BlogPostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "body"]
