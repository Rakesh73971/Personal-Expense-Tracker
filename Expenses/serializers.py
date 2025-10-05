from .models import Category,Expense
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

    def validate(self,data):
        name = data.get('name','').strip()
        if not name:
            raise serializers.ValidationError({'name':'category name is required'})
        elif not name.replace(" ","").isalpha():
            raise serializers.ValidationError({'name':'name must be characters'})
        elif len(name) < 3:
            raise serializers.ValidationError({'name':'name must be at least 3 characters'})
        
        return data


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Expense
        fields = ['id','category','category_name','title','amount','date','payment_method','note']
        extra_kwargs = {
            'category': {'write_only': True}
        }

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def validate_category(self,value):
        if not value:
            raise serializers.ValidationError('category is required')
        if not Category.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError('Invalid category is selected')
        return value

    def validate_title(self,value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError('Title is required')
        elif not value.replace(" ","").isalpha():
            raise serializers.ValidationError('Title must be characters')
        elif len(value) < 3:
            raise serializers.ValidationError("Title must be atleast 3 character")
        return value
    
    def validate_amount(self,value):
        if value is None:
            raise serializers.ValidationError('amount is required')
        elif value <= 0:
            raise serializers.ValidationError("amount must be greater than 0")
        return value
    def validate_note(self,value):
        if value and len(value) > 500:
            raise serializers.ValidationError('note can not be more than 500 characters')
        return value

class ExpenseListSerializer(serializers.Serializer):
    Expenses = ExpenseSerializer(many=True)
    total_amount = serializers.FloatField()
        

    
    

