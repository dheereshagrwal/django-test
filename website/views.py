from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @csrf_exempt
@api_view(["POST"])
def create_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    # Check if username and password are provided
    if not username or not password:
        return Response(
            {"error": "Username and password are required."},
            status=400,
        )

    # Check if the user already exists
    user_exists = User.objects.filter(username=username).exists()

    if user_exists:
        return Response(
            {"error": "Username already taken.", "user_exists": True}, status=400
        )

    # Create the user
    user = User.objects.create_user(username=username, password=password)

    return Response(
        {"message": "User created successfully.", "user_exists": False}, status=201
    )
