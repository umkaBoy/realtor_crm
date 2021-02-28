from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from crm.serializers import ProfileSerializer, ComplexesShortSerializer, OldBuildingsShortSerializer, \
    NewBuildingsShortSerializer
from crm.models.complexes import Complex
from crm.models.lots import OldBuildingLot, NewBuildingLot
from itertools import chain



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
        if page == 'lots':
            new_buildings = NewBuildingLot.objects.all().order_by('complex')
            old_buildings = OldBuildingLot.objects.all().order_by('complex')
            objs = list(
                sorted(
                    chain(new_buildings, old_buildings),
                    key=lambda objects: objects.id
                ))

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