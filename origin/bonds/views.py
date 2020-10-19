from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, permissions, filters
from bonds.models import Bond
from bonds.serializers import BondSerializer


class HelloWorld(APIView):
    def get(self, request):
        return Response("Hello World!")

    
class Bond_view(generics.ListCreateAPIView):
    serializer_class = BondSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bond.objects.all()
    
    def get_queryset(self):

        queryset = super(Bond_view, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)

        codes = ['isin', 'size', 'currency', 'maturity', 'lei', 'legal_name']
        for key_, value in self.request.query_params.items():
            if key_ in codes:
                  filters[key_] = value
                 
        return queryset.filter(**filters)


    def perform_create(self, serializer):

        serializer.save(user=self.request.user)