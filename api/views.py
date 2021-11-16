# from django.shortcuts import render
# from rest_framework.views import APIView
# from database.models import User, WorkPlan, UserHistory
# from rest_framework.response import Response

# from django.contrib.auth import authenticate

# from datetime import datetime

# class get_userdata(APIView):
#     #show work history
#     def get(self, request):
#         print('get_userdata + post')
#         user = User.objects.get(username=request.data['username'])
#         work_date = UserHistory.objects.all(user=user)
#         data = {"user":user,
#                 "work_data":work_date}
#         return Response(data)

# class login(APIView):
#     # login logout
#     def post(self, request):
#         user = authenticate(request,username=request.body['username'],password=request.body['password'])
#         if user is not None:
#             user = User.objects.get(username=request.body['username'])
#             checkin = UserHistory.objects.latest(user=user)
#             checkin.datetime_checkin = datetime.now()
#             return Response({'method':'checkin',
#                             'status':'complete'})
#         else:
#             return Response({'method':'checkin',
#                             'status':'error',
#                             'message':'User is None'})


# class CheckInCheckOut(APIView):
#     def post(self, request):
#         # check in
#         if (request.body['method'] == "checkin"):
#             user = authenticate(request, 
#                 username=request.body['username'],
#                 password=request.body['password'])
#             if user is not None:
#                 user = User.objects.get(username=request.body['username'])
#                 checkin = UserHistory.objects.latest(user=user)
#                 checkin.datetime_checkin = datetime.now()
#                 return Response({'method':'checkin',
#                                 'status':'complete'})
#             else:
#                 return Response({'method':'checkin',
#                                 'status':'error',
#                                 'message':'User is None'})

#         # checkout
#         elif (request.body['method'] == "checkout"):
#             user = authenticate(request, 
#                 username=request.body['username'],
#                 password=request.body['password'])
#             if user is not None:
#                 user = User.objects.get(username=request.body['username'])
#                 checkin = UserHistory.objects.latest(user=user)
#                 checkin.datetime_checkout = datetime.now()
#                 return Response({'method':'checkout',
#                                 'status':'complete'})
#             else:
#                 return Response({'method':'checkout',
#                                 'status':'error',
#                                 'message':'User is None'})

