from rest_framework import serializers
from .models import News, Sitate, Photo, About, Professor, Maqola, Kitob, Presentation, Project, Event, KafedraPhoto, KafedraVideo, BakalavrLesson, MagistLesson, Student, IndependentWork, ControlWork, GraduateStudy

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'image', 'title', 'description', 'date')

class SitateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitate
        fields = ('id', 'image', 'author', 'text')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'description')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'text')

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'fullname', 'job_position', 'description', 'fakultet', 'kafedra', 'degree', 'email', 'google_h_index', 'scopus_h_index', 'wos_h_index', 'facebook', 'instagram', 'telegram', 'youtube')

class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = ('id', 'files')

class KitobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob
        fields = ('id', 'files')

class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ('id', 'files')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'images', 'videos')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'images', 'videos', 'files')

class KafedraPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafedraPhoto
        fields = ('id', 'image')

class KafedraVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafedraVideo
        fields = ('id', 'video')

class BakalavrLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakalavrLesson
        fields = ('id', 'text')

class MagistLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagistLesson
        fields = ('id', 'text')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'description')

class IndependentWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndependentWork
        fields = ('id', 'file')

class ControlWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlWork
        fields = ('id', 'file')

class GraduateStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduateStudy
        fields = ('id', 'file')
