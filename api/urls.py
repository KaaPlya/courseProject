from django.urls import path
from validation import views
from api.views import AllPostsListView, BlogPostDetailView, add_comment, add_reply, CourseListView, CourseDetailView, SectionListView, SectionDetailView, \
    LectureListView, LectureDetailView, LectureCommentListView, LectureCommentDetailView, \
    CourseSubscriptionListView, CourseSubscriptionDetailView, StudentInfoListView, StudentInfoDetailView, \
    PaymentProcessListView, PaymentProcessDetailView, LessonStatusListView, LessonStatusDetailView, CheckoutView


urlpatterns = [
    path('api/all-posts/', AllPostsListView.as_view(), name='all-posts-list'),
    path('api/blog-post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('api/add-comment/', add_comment, name='add-comment'),
    path('api/add-reply/', add_reply, name='add-reply'),
    path('api/courses/', CourseListView.as_view(), name='course-list'),
    path('api/courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('api/sections/', SectionListView.as_view(), name='section-list'),
    path('api/sections/<int:pk>/', SectionDetailView.as_view(), name='section-detail'),
    path('api/lectures/', LectureListView.as_view(), name='lecture-list'),
    path('api/lectures/<int:pk>/', LectureDetailView.as_view(), name='lecture-detail'),
    path('api/comments/', LectureCommentListView.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', LectureCommentDetailView.as_view(), name='comment-detail'),
    path('api/lesson-status/', LessonStatusListView.as_view(), name='lesson-status-list'),
    path('api/lesson-status/<int:pk>/', LessonStatusDetailView.as_view(), name='lesson-status-detail'),
    path('api/courses/', CourseListView.as_view(), name='course-list'),
    path('api/courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('api/sections/', SectionListView.as_view(), name='section-list'),
    path('api/sections/<int:pk>/', SectionDetailView.as_view(), name='section-detail'),
    path('api/lectures/', LectureListView.as_view(), name='lecture-list'),
    path('api/lectures/<int:pk>/', LectureDetailView.as_view(), name='lecture-detail'),
    path('api/comments/', LectureCommentListView.as_view(), name='comment'),
    path('api/studentInfo/', StudentInfoListView.as_view(), name='studentinfo-list'),
    path('api/studentInfo/<int:pk>/', StudentInfoDetailView.as_view(), name='studentinfo-detail'),
    path('api/CourseSubscription/', CourseSubscriptionListView.as_view(), name='coursesubscription-list'),
    path('api/CourseSubscription/<int:pk>/', CourseSubscriptionDetailView.as_view(), name='coursesubscription-detail'),
    path('api/PaymentProcess/', PaymentProcessListView.as_view(), name='paymentprocess-list'),
    path('api/PaymentProcess/<int:pk>/', PaymentProcessDetailView.as_view(), name='paymentprocess-detail'),
    path('checkpayment/', views.checkpayment, name='checkpayment'),
    path('freecheckout/<str:slug>/', views.FreeCheckout, name='freecheckout'),
    path('currentpassvalidation/', views.currentPassvalidation, name='currentpassvalidation'),
    path('usernamevalidation/', views.Usernamevalidation, name='usernamevalidation'),
    path('emailvalidation/', views.Emailvalidation, name='emailvalidation'),
    path('loginusernamevalidation/', views.LoginUsernamevalidation, name='loginusernamevalidation'),
    path('handlesignup/', views.handleSignup, name='handlesignup'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('handlelogout/', views.handlelogout, name='handlelogout'),
]
