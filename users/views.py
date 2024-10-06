from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render

# 获取所有用户
@api_view(['GET'])
def get_users(request):
    # limit ****@gmail.com
    #1"sle(*"
    #2.api
    users = User.objects.all().order_by('-id')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# 获取单个用户
@api_view(['GET'])
def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

# 创建用户
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 更新用户
@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 删除用户
@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#筛选邮箱结尾是gmail的用户
@api_view(['GET'])
def gmail_users_api(request):
    # gmail_users = User.objects.filter(email__endswith='@gmail.com')
    # serializer = UserSerializer(gmail_users, many=True)
    # return Response(serializer.data)
    gmail_users = User.objects.raw("SELECT * FROM users WHERE email LIKE %s", ['%@gmail.com'])
  #除了以上两种方法，如果数据量大，还可以直接用代码实现，先把数据按照某些条件先过滤出来，再做处理  if(){}
    serializer = UserSerializer(gmail_users, many=True)
    return Response(serializer.data)
# Create your views here.

from users.producers import UserProducer
from users.models import User
from django.http import JsonResponse

@api_view(['POST'])
def update_user_kafka(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=id)
            user.name = request.data.get('name', user.name)
            user.email = request.data.get('email', user.email)
            # user.salary = request.data.get('salary', user.salary)
            user.save()

            # 发送更新消息到 Kafka
            producer = UserProducer()
            producer.send_user_update({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                # 'salary': user.salary
            })

            return JsonResponse({'status': 'success'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid method'}, status=405)
