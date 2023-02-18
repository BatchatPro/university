from django.urls import path
from .views import NewsList, SitateList, PhotosList, AboutKaferda, ProffessorsList, Maqolalar, Kitoblar, Presentations, Projects, Event, KafedraPhotosList, KafedraVideosList, BakalavrLessonsList, MagistLessonsList, StudentsList, IndependentWorksList, ControlWorksList, GraduateStudiesList

urlpatterns = [
    path('news/', NewsList.as_view()),
    path('sitates/', SitateList.as_view()),
    path('photos/', PhotosList.as_view()),
    path('about/', AboutKaferda.as_view()),
    path('professors/', ProffessorsList.as_view()),
    path('maqolalar/', Maqolalar.as_view()),
    path('kitoblar/', Kitoblar.as_view()),
    path('presentations/', Presentations.as_view()),
    path('projects/', Projects.as_view()),
    path('event/', Event.as_view()),
    path('kafedra-photos/', KafedraPhotosList.as_view()),
    path('kafedra-videos/', KafedraVideosList.as_view()),
    path('bakalavr-lessons/', BakalavrLessonsList.as_view()),
    path('magist-lessons/', MagistLessonsList.as_view()),
    path('students/', StudentsList.as_view()),
    path('independent-works/', IndependentWorksList.as_view()),
    path('control-works/', ControlWorksList.as_view()),
    path('graduate-studies/', GraduateStudiesList.as_view()),
]
