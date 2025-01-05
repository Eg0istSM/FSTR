from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('id', 'latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'data', 'title',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'fam', 'name', 'otc', 'phone',)


class PerevalSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ('title', 'other_title', 'connect', 'add_time', 'user', 'coords', 'level', 'images', 'status',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        coords_data = validated_data.pop('coords')
        coords_instance = Coords.objects.create(**coords_data)
        level_data = validated_data.pop('level')
        level_instance = Level.objects.create(**level_data)
        images_data = validated_data.pop('images')
        pereval_instance = Pereval.objects.create(user=user_instance, coords=coords_instance, level=level_instance,
                                                  **validated_data, )
        for img in images_data:
            data = img.pop('data')
            title = img.pop('title')
            Images.objects.create(pereval=pereval_instance, title=title, data=data)

        return pereval_instance

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data.get('user')
            validating_user_fields = [
                instance_user.fam != data_user['fam'],
                instance_user.name != data_user['name'],
                instance_user.otc != data_user['otc'],
                instance_user.phone != data_user['phone'],
                instance_user.email != data_user['email'],

            ]

            if data_user is not None and any(validating_user_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data

    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        User.objects.update(**user)
        Coords.objects.update(**coords)
        Level.objects.update(**level)

        for image in images:
            data = image.pop('data')
            title = image.pop('title')
            Images.objects.update(data=data, title=title)

        return super().update(instance, validated_data)



