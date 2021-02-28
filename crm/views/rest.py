from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from crm.serializers import ProfileSerializer, ComplexesShortSerializer, OldBuildingsShortSerializer, \
    NewBuildingsShortSerializer
from crm.models.complexes import Complex
from crm.models.lots import Lot


class ProfileRest(APIView):
    ser = ProfileSerializer

    def get(self, request, *args, **kwargs):
        ser_data = self.ser(request.user)
        return Response(ser_data.data)


class LoadDataRest(APIView):
    ser = OldBuildingsShortSerializer
    ser1 = NewBuildingsShortSerializer
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
            data_page = paginator.page(counter)
        except Exception:
            return Response([])
        if page == 'complexes':
            ser_data = self.ser2(data_page, many=True)
        if page == 'lots':
            ser_data = self.ser1(data_page, many=True)
        return Response(ser_data.data)