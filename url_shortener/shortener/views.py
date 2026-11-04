import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
        return JsonResponse(
            {
                "message": "URL received for shortening.",
                "url": data.get("url", ""),
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
