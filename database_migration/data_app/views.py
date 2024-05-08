from django.http import JsonResponse
from .models import User, Address, Item

def combined_data_view(request):
    combined_data = User.objects.values('name', 'address__email_address', 'item__name', 'item__description')

    return JsonResponse(list(combined_data), safe=False)
