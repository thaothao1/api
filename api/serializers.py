from rest_framework.serializers import ModelSerializer , SerializerMethodField
from .models import Category , Course , Lesson , Tag , User , Comment, Action , Rating , LessonView
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CourseSerializer(ModelSerializer):
    image = SerializerMethodField()
    def get_image(self , course):
        request = self.context['request']
        name = course.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name
        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = ["id","subject","image","created_date","category"]

class LessonSerializers(ModelSerializer):
      class Meta:
          model = Lesson
          fields = ["id"  , "subject" , "image" , "course" , "created_date",
          "updated_date" ]
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class LessonDetailSerializer(LessonSerializers):
    tags =  TagSerializer(many= True)
    class Meta:
        model = LessonSerializers.Meta.model
        fields = LessonSerializers.Meta.fields + ['content' , 'tags']

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id'  , 'creator','created_date' , 'updated_date' , 'content']

class UserSerializer(ModelSerializer):
    def create(self , validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user
    class Meta:
        model = User
        fields= ["id","first_name","last_name","username",
        "password", "email" , "date_joined"]
    extra_kwargs ={
        'password' : {'write_only' : 'true'}
    }
class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields=["id" , "type" , "created_date"]

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields=["id" , "rate" , "created_date"]

class LessonViewSerializer(ModelSerializer):
    class Meta:
        model= LessonView
        fields =["id" , "views" , "lesson"]