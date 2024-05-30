from .models import Course,Teacher,Students
from rest_framework import serializers

class CourseSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=7,decimal_places=2)
    davomiyligi = serializers.IntegerField(default=0)
    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)
        instance.davomiyligi = validated_data.get('davomiyligi',instance.davomiyligi)
        instance.save()
        return instance



class TeacherSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
    tajriba = serializers.IntegerField(default=0)
    subject = serializers.CharField(max_length=50)
    course_id = serializers.IntegerField()
    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        instance.status = validated_data.get('status',instance.status)
        instance.tajriba = validated_data.get('tajriba',instance.tajriba)
        instance.subject = validated_data.get('subject',instance.subject)
        instance.course_id = validated_data.get('course_id',instance.course_id)
        instance.save()
        return instance








class StudentSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=13)
    parents_phone = serializers.CharField(max_length=30)
    telegram = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    course_id = serializers.IntegerField()
    teacher_id = serializers.IntegerField()

    def create(self, validated_data):
        return Students.objecta.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        instance.phone = validated_data.get('phone',instance.phone)
        instance.parents_phone = validated_data.get('parents_phone',instance.parents_phone)
        instance.telegram = validated_data.get('telegram',instance.telegram)
        instance.address = validated_data.get('address',instance.address)
        instance.course_id = validated_data.get('course_id',instance.course_id)
        instance.teacher_id = validated_data.get('teacher_id',instance.teacher_id)
        instance.save()
        return instance
