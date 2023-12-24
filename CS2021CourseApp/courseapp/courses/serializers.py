from courses.models import Category, Course, Tag, Lesson, User
from rest_framework import serializers

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, course):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri()
        return '/static/%s' % course.image.name

    class Meta:
        model = Course
        fields = '__all__'


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', ]