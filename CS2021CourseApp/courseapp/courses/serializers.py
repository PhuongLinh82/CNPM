from courses.models import Category, Course
from rest_framework import serializers

class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri()
        return '/static/%s' % course.image.name
    class Meta:
        model = Course
        fields = '__all__'