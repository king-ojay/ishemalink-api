from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

class APIRootView(APIView):
    def get(self, request):
        return Response({
            "name": "IshemaLink API",
            "version": "v1"
        })

class HealthCheckView(APIView):
    def get(self, request):
        try:
            connection.ensure_connection()
            return Response({"status": "ok"})
        except Exception:
            return Response({"status": "error"}, status=500)
