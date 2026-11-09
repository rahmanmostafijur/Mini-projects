import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .utils import generate_short_code


def home(request):
    return JsonResponse(
        {
            "message": "Url Shortener API is running. Use the /shorten endpoint to shorten URLs.",
            "status": "success",
        }
    )


@csrf_exempt
def shorten_url(request):
    if request.method == "POST":
        # Handle the POST request to shorten a URL
        data = json.loads(request.body)
        url = data.get("url", "").strip()
        if not url:
            return JsonResponse(
                {
                    "message": "No URL provided for shortening.",
                    "status": "error",
                },
                status=400,
            )
        validator = URLValidator()
        try:
            validator(url)
        except ValidationError:
            return JsonResponse(
                {
                    "message": "Invalid URL provided.",
                    "status": "error",
                },
                status=400,
            )
        short_code = generate_short_code()
        return JsonResponse(
            {
                "message": "URL received for shortening.",
                "url": url,
                "short_code": short_code,
                "status": "success",
            }
        )
    else:
        return JsonResponse(
            {
                "message": "Invalid request method. Please use POST to shorten URLs.",
                "status": "error",
            },
            status=405,
        )
