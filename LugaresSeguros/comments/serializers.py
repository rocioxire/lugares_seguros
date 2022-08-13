from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

def to_representation(self, instance):
    return{
        'id': instance.id,
        'place': {
            'id': instance.place.id,
            'name': instance.place.name
        },
        'comment': instance.commet,
        'created': instance.created
    }


class CommentPlaceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
