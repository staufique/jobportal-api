from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import *
from jobportal_api.renderer import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# generate tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }



class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},
                                status=status.HTTP_404_NOT_FOUND)
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data,
        context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password changed sucessfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SendPasswordRequestEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordRequestEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset link send. please check your email'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request,uid,token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset successfully'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PersonalInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PersonalInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Data Inserted'},status=status.HTTP_201_CREATED)
            # return Response({'msg':'Data Inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdatePersonalInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def put(self,request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = PersonalInfoSerializer(puser,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = PersonalInfoSerializer(puser,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data Inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateEducationView(APIView):
    renderer_classes = [UserRenderer]
    def put(self,request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = EducationSerializer(puser,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = EducationSerializer(puser,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExperienceView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data Inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateExperienceView(APIView):
    renderer_classes = [UserRenderer]
    def put(self,request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = ExperienceSerializer(puser,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = ExperienceSerializer(puser,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillsView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SkillsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data Inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateSkillsView(APIView):
    renderer_classes = [UserRenderer]
    def put(self,request,pk):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = SkillsSerializer(puser,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk=None):
        puser = PersonalInfo.objects.filter(pk=pk).first()
        serializer = SkillsSerializer(puser,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
