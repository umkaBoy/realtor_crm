from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from crm.serializers import ProfileSerializer, ComplexesShortSerializer, LotsShortSerializer
from crm.models.complexes import Complex
from crm.models.lots import Lot


class ProfileRest(APIView):
    ser = ProfileSerializer

    def get(self, request, *args, **kwargs):
        ser_data = self.ser(request.user)
        return Response(ser_data.data)


class LoadDataRest(APIView):
    ser1 = LotsShortSerializer
    ser2 = ComplexesShortSerializer

    def post(self, request, *args, **kwargs):
        page = request.data.get('page')
        counter = request.data.get('counter')
        if page == 'complexes':
            objs = Complex.objects.all().order_by('developer')
            ser_data = self.ser2(objs, many=True)
        if page == 'lots':
            objs = Lot.objects.all()
            ser_data = self.ser1(objs, many=True)

        paginator = Paginator(objs, 20)
        try:
            cart_details = paginator.page(counter)
        except Exception:
            return Response([])
        return Response(ser_data.data)