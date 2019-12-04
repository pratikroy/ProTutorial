from rest_framework import generics
from home_page.models import HomePage
from home_page.serializers import HomePageSerializer

# Create your views here.
class HomePageListView(generics.ListAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
