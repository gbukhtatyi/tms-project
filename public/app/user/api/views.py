# Django
from django.views.decorators.csrf import csrf_exempt
# Rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Application
from . import serializers
from user.forms import ProfileForm, SettingsForm


@csrf_exempt
@api_view(["GET", "POST"])
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.data, instance=user)
        if form.is_valid():
            user = form.save()
        else:
            return Response(
                {
                    "status": "error",
                    "errors": form.errors
                },
                status=400
            )

    return Response(
        serializers.UserProfileSerializer(instance=user).data
    )


@csrf_exempt
@api_view(["GET", "POST"])
def settings(request):
    user = request.user
    if request.method == 'POST':
        form = SettingsForm(request.data, instance=user)
        if form.is_valid():
            user.is_subscribed = form.cleaned_data.get('is_subscribed')
            user.save()
        else:
            return Response(
                {
                    "status": "error",
                    "errors": form.errors
                },
                status=400
            )

    return Response(
        serializers.UserSettingsSerializer(instance=user).data
    )
