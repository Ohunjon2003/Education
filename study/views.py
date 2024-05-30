from django.shortcuts import render
from .models import Teacher,Students,Course
# Create your views here.
from .serializers import CourseSerializers,TeacherSerializers,StudentSerializers
from rest_framework import generics
from rest_framework import mixins
from  rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)


class CourseApiList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


    def get(self,*args,**kwargs):
        return self.list(*args,**kwargs)

    def post(self,*args,**kwargs):
        return self.create(*args,**kwargs)

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)

    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)


class CourseApiDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin):
    queryset = Course
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]



class TeacherApiList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


    def get(self,*args,**kwargs):
        return self.list(*args,**kwargs)

    def post(self,*args,**kwargs):
        return self.create(*args,**kwargs)

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)

    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)


class TeacherApiDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin):
    queryset = Teacher
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentApiList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


    def get(self,*args,**kwargs):
        return self.list(*args,**kwargs)

    def post(self,*args,**kwargs):
        return self.create(*args,**kwargs)

    def put(self,*args,**kwargs):
        return self.update(*args,**kwargs)

    def delete(self,*args,**kwargs):
        return self.destroy(*args,**kwargs)


class StudentApiDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin):
    queryset = Students
    serializer_class = StudentSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]