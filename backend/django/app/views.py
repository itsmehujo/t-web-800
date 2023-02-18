from django.http import JsonResponse

def index(request):

    data = {
        'message': "Hello from the backend"
    }

    return JsonResponse(data)
