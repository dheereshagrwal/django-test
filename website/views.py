from django.http import JsonResponse


def custom404(request, exception=None):
    data = {"error": "page not found"}
    return JsonResponse(data, status=404)