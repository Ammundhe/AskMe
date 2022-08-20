from rest_framework import serializers
from django.contrib.auth.models import User
from question.models import question, questionCategory
from answer.models import answer
from blog.models import blog, PostCategory

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username=validated_data['username']
        instance.first_name=validated_data['first_name']
        instance.last_name=validated_data['last_name']
        instance.email=validated_data['email']
        instance.set_password=validated_data['password']
        instance.save()
        return instance

class questcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=questionCategory
        fields=['name']

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=question
        fields=[
            'category',
            'question',
            'date',
            'author'
        ]
        depth=1

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PostCategory
        fields=['name']

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields=[
            'category',
            'title',
            'slug',
            'cover_image',
            'description',
            'author',
            'date'
        ]

class answerSerializer(serializers.ModelSerializer):
    class Meta:
        model=answer
        fields=[
            'question',
            'image',
            'answer', 
            'author',
            'date'
        ]
