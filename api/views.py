from rest_framework import generics
from .models import News, Sitate, Photo, About, Professor, Maqola, Kitob, Presentation, Project, Event, KafedraPhoto, KafedraVideo, BakalavrLesson, MagistLesson, Student, IndependentWork, ControlWork, GraduateStudy
from .serializers import NewsSerializer, SitateSerializer, PhotoSerializer, AboutSerializer, ProfessorSerializer, MaqolaSerializer, KitobSerializer, PresentationSerializer, ProjectSerializer, EventSerializer, KafedraPhotoSerializer, KafedraVideoSerializer, BakalavrLessonSerializer, MagistLessonSerializer, StudentSerializer, IndependentWorkSerializer, ControlWorkSerializer, GraduateStudySerializer

class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class SitateList(generics.ListAPIView):
    queryset = Sitate.objects.all()
    serializer_class = SitateSerializer

class PhotosList(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class AboutKaferda(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProffessorsList(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class Maqolalar(generics.ListAPIView):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSerializer

class Kitoblar(generics.ListAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer

class Presentations(generics.ListAPIView):
    queryset = Presentation.objects.all()
    serializer_class = PresentationSerializer

class Projects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Event(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class KafedraPhotosList(generics.ListAPIView):
    queryset = KafedraPhoto.objects.all()
    serializer_class = KafedraPhotoSerializer

class KafedraVideosList(generics.ListAPIView):
    queryset = KafedraVideo.objects.all()
    serializer_class = KafedraVideoSerializer

class BakalavrLessonsList(generics.ListAPIView):
    queryset = BakalavrLesson.objects.all()
    serializer_class = BakalavrLessonSerializer

class MagistLessonsList(generics.ListAPIView):
    queryset = MagistLesson.objects.all()
    serializer_class = MagistLessonSerializer

class StudentsList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class IndependentWorksList(generics.ListAPIView):
    queryset = IndependentWork.objects.all()
    serializer_class = IndependentWorkSerializer

class ControlWorksList(generics.ListAPIView):
    queryset = ControlWork.objects.all()
    serializer_class = ControlWorkSerializer

class GraduateStudiesList(generics.ListAPIView):
    queryset = GraduateStudy.objects.all()
    serializer_class = GraduateStudySerializer
