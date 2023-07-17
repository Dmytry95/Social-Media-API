from rest_framework import serializers

from social_media.models import Comment, Like, Post, Profile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "author",
            "post",
            "content",
            "created_at",
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "author",
            "post",
            "created_at",
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "status",
            "profile_pic",
            "bio",
        )


class ProfileListSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "status",
            "profile_pic",
            "bio",
            "followers",
            "following",
        )


class ProfileDetailSerializer(ProfileSerializer):
    class Meta:
        model = Profile
        fields = (
            "username",
            "status",
            "profile_pic",
            "bio",
            "followers",
            "following",
        )


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("profile_pic",)


class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "author",
            "content",
            "created_at",
            "comments",
            "likes",
        )
