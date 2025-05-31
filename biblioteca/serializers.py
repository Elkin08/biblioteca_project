from rest_framework import serializers
from .models import Author, Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','book', 'rating', 'comment', 'created_at']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'year', 'publication_date', 'recent_reviews']

    def get_recent_reviews(self, obj):
        reviews = obj.reviews.order_by('-created_at')[:5]
        return ReviewSerializer(reviews, many=True).data

class AuthorSerializer(serializers.ModelSerializer):
    nationality = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Author
        fields = ['id', 'name', 'nationality']
