from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializers import DataSerializer

@api_view(['GET'])
def get_data(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)
