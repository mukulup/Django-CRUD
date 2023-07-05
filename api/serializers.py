from dataclasses import field
from rest_framework import serializers
from .models import Articles

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        exclude = ['created_on']
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('__all__')
        