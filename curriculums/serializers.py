from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Curriculums
from courses.models import Course
from user.serializers import UserSerializer
from rest_framework_recursive.fields import RecursiveField

class CurriculumsSerializer(serializers.ModelSerializer):
	course = RecursiveField('courses.serializers.CoursesSerializerSimple', read_only=True)
	course_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

	class Meta:
		model = Curriculums
		fields = (
			'id',
			'title',
			'attachment_url',
			'type',

			'course_id',
			'course',
			'created_by',
		)

	def create(self, validated_data):
		 # Once you are done, create the instance with the validated data
	    curriculum = Curriculums(**validated_data) 

	    # relate with user
	    course_id = validated_data.get("course_id")
	    validated_data.pop("course_id", None)
	    course = Course.objects.filter(id=course_id).first()
	    curriculum.course = course

	    curriculum.save()

	    return curriculum

class CurriculumsSerializerSimple(serializers.ModelSerializer):
	class Meta:
		model = Curriculums
		fields = (
			'id',
			'title',
			'attachment_url',
			'type',
			'created_by',
		)