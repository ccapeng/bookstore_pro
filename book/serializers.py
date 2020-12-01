from rest_framework import serializers

from book.models import Category, Publisher, Author, Book


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        #read_only_fields = ('last_name', 'first_name')


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)

    class Meta:
        model = Book
        fields = (
            'id', 
            'title', 
            'category', 
            'category_name', 
            'publisher', 
            'publisher_name', 
            'author', 
            'author_last_name', 
            'author_first_name'
        )
