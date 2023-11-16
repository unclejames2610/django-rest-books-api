# from rest_framework import serializers
# from books_api.models import Book

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.quantity = data.get('quantity', instance.quantity)

#         instance.save()
#         return instance


from django.forms import ValidationError
from rest_framework import serializers
from books_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField() #adding another field
    class Meta:
        model = Book
        fields = "__all__"  #get all fields

    def validate_title(self, value):  #to validate a field 
        if value == "Da Vinci Code":
            raise ValidationError("No Da Vinci Code please")
        return value
    
    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Too heavy for inventory")
        return data
    
    def get_description(self, data):  #the name after the get is the same name as the field that was added above
        return "This book is called " + data.title + " and it is " + str(data.number_of_pages) + " pages long."