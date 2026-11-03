from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse(
        {
            "message": "Url Shortener API is running. Use the /shorten endpoint to shorten URLs.",
            "status": "success",
        }
    )