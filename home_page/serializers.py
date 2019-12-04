from rest_framework import serializers
from home_page.models import HomePage

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
