from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import LicenseKeyModel


class LicenseAPIView(APIView):
    def post(self, request):
        data = request.data
        license_key = data.get('license_key')
        hw_id = data.get('hw_id')
        try:
            hw_id = int(hw_id)
        except ValueError:
            pass
        license_obj = LicenseKeyModel.objects.filter(license_key=license_key).first()
        if license_obj is None:
            return Response(status=400)
        if license_obj.license_hw_id is None:
            license_obj.license_hw_id = str(hw_id)
            license_obj.save()
            return Response(status=201)
        if license_obj.license_hw_id == hw_id:
            return Response(status=200)
        return Response(status=406)
