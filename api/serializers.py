from rest_framework import serializers
from blog.models import Post, BlogComment
from mysite.models import Course, Section, Lecture, LectureComment, LessonStatus
from student.models import CourseSubscription, StudentInfo, PaymentProcess

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class LectureCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureComment
        fields = '__all__'

class LessonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStatus
        fields = '__all__'



class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'

class PaymentProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProcess
        fields = '__all__'



