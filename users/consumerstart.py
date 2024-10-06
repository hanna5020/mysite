from users.producers import UserProducer
from users.models import User
from django.http import JsonResponse

def update_user_view(request,id):
    try:
        user = User.objects.get(id=id)
        user_producer = UserProducer()
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }
        user_producer.send_user_update(user_data)
        return JsonResponse({"status": "User update message sent"})
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    #hhn

