from rest_framework import viewsets, generics
from courses import serializers, paginators
from courses.models import Category, Course


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerialzer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePagination