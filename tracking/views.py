from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car, Location
from .serializers import CarSerializer, LocationSerializer
from .models import Location

# ✅ صفحه HTML (Dashboard)
def index(request):
    return render(request, 'index/index.html')

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Location

def map(request,id):
    locations = Location.objects.filter(car__id=id).order_by('-timestamp')
    paginator = Paginator(locations, 10)  # هر صفحه ۱۰ رکورد
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "map/map.html", {"page_obj": page_obj})

# ✅ دریافت موقعیت از آردوینو یا اپ اندروید
class UpdateLocationView(APIView):
    """
    دریافت موقعیت از آردوینو یا اپ اندروید
    """
    def post(self, request):
        name = request.data.get("name")
        imei = request.data.get("imei")
        lat  = request.data.get("latitude")
        lon  = request.data.get("longitude")

        if not all([imei, lat, lon]):
            return Response(
                {"error": "imei, latitude, longitude الزامی است."},
                status=status.HTTP_400_BAD_REQUEST
            )

        car, _ = Car.objects.get_or_create(imei=imei, defaults={"name": f"Car_{name}"})
        location = Location.objects.create(name=name,car=car, latitude=lat, longitude=lon)

        return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED)


# ✅ دریافت آخرین موقعیت با imei
class LastLocationView(APIView):
    """
    دریافت آخرین موقعیت خودرو (برای نمایش در اپ یا LCD)
    """
    def get(self, request, imei):
        try:
            car = Car.objects.get(imei=imei)
            last_loc = Location.objects.filter(car=car).order_by('-timestamp').first()
            if not last_loc:
                return Response({"message": "موقعیتی یافت نشد."}, status=status.HTTP_404_NOT_FOUND)
            return Response(LocationSerializer(last_loc).data)
        except Car.DoesNotExist:
            return Response({"error": "ماشین یافت نشد."}, status=status.HTTP_404_NOT_FOUND)


# ✅ دریافت آخرین موقعیت با id (بر اساس رکورد)
class LastLocationIdView(APIView):
    """
    برمی‌گرداند آخرین رکورد موقعیت (Location) برای یک ماشین با imei مشخص.
    GET /api/last_id/<str:imei>/
    """
    def get(self, request, imei):
        car = get_object_or_404(Car, imei=imei)
        last_location = Location.objects.filter(car=car).order_by('-id').first()

        if not last_location:
            return Response({"message": "هیچ موقعیتی یافت نشد."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LocationSerializer(last_location)
        return Response(serializer.data, status=status.HTTP_200_OK)
