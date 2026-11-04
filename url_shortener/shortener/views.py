from django.http import JsonResponse


# Create your views here.
def home(request):
    return JsonResponse(
        {
            "message": "Url Shortener API is running. Use the /shorten endpoint to shorten URLs.",
            "status": "success",
        }
    )


def shorten_url(request):
    return JsonResponse(
        {
            "message": "This endpoint will shorten URLs. Please provide a URL to shorten.",
            "status": "success",
        }
    )
