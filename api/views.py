from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post, BlogComment
from .serializers import PostSerializer, BlogCommentSerializer, CourseSerializer, SectionSerializer, LectureSerializer, \
                         LectureCommentSerializer, LessonStatusSerializer, CourseSubscriptionSerializer, \
                         StudentInfoSerializer, PaymentProcessSerializer
from mysite.models import Course, Section, Lecture, LectureComment, LessonStatus
from student.models import CourseSubscription, StudentInfo, PaymentProcess
import json



class AllPostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

@api_view(['POST'])
def add_comment(request):
    if request.method == 'POST':
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_reply(request):
    if request.method == 'POST':
        serializer = BlogCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class LectureListView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class LectureCommentListView(generics.ListCreateAPIView):
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer

class LectureCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer

class LessonStatusListView(generics.ListCreateAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer
    permission_classes = [IsAuthenticated]

class LessonStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonStatus.objects.all()
    serializer_class = LessonStatusSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SectionListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class LectureListView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class LectureCommentListView(generics.ListCreateAPIView):
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer
    permission_classes = [IsAuthenticated]

class LectureCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LectureComment.objects.all()
    serializer_class = LectureCommentSerializer

class CourseSubscriptionListView(generics.ListCreateAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseSubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer

class StudentInfoListView(generics.ListCreateAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer

class PaymentProcessListView(generics.ListCreateAPIView):
    queryset = PaymentProcess.objects.all()
    serializer_class = PaymentProcessSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentProcessDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentProcess.objects.all()
    serializer_class = PaymentProcessSerializer

class CheckoutView(generics.CreateAPIView):
    serializer_class = PaymentProcessSerializer

    def create(self, request, slug):
        if not Course.objects.filter(course_slug=slug).exists():
            return Response({"detail": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            if not request.user.is_authenticated:
                return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

            course = Course.objects.get(course_slug=slug)
            student = StudentInfo.objects.filter(username=request.user).first()

            if course.course_price == 0:
                return Response({"detail": "Course is free."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                with open("secret key.json", 'r') as secret:
                    key = json.load(secret)['QIWI']

                client = QIWI.Client(auth=(key['key id'], key['key secret']))
                payment_id = client.order.create({'amount': course.course_price * 100, 'currency': 'INR', 'payment_capture': '1'})
                new_payment = PaymentProcess(student=student, course=course, order_id=payment_id['id'])
                new_payment.save()

                return Response({"order_id": payment_id['id'], "amount": course.course_price * 100, "currency": "INR"})



