from django.http import JsonResponse
from .tasks import add

# Create your views here.
def index(request):
    add.delay(2, 9)
    return JsonResponse({"message":"Hello, world! You're at the main index. Shortly you will receive the sum of 2 and 9"})
