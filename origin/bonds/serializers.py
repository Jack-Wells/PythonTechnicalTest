from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers
from bonds.models import Bond


class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")


class BondSerializer(serializers.ModelSerializer):
    
    legal_name = serializers.ReadOnlyField()

    class Meta:
        model = Bond
        fields = ("isin", "size", "currency", "maturity", "lei", "legal_name")