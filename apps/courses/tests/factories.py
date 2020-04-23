import datetime
import factory

from django.utils.timezone import now
from apps.courses.models import Course, Lecture, CourseParticipant
from apps.students.models import Student


class CourseFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=2)
    description = factory.Faker('text')
    start_date = factory.LazyAttribute(lambda i: now() - datetime.timedelta(days=4))
    end_date = factory.LazyAttribute(lambda i: now() + datetime.timedelta(days=3))

    class Meta:
        model = Course


class StudentFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('sentence')
    last_name = factory.Faker('sentence')
    email = factory.Faker('sentence')

    class Meta:
        model = Student


class CourseParticipantFactory(factory.DjangoModelFactory):
    course = factory.SubFactory(CourseFactory)
    student = factory.SubFactory(StudentFactory)
    is_completed = True

    class Meta:
        model = CourseParticipant


class LectureFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence')
    topic = factory.Faker('text')
    course = factory.SubFactory(CourseFactory)

    class Meta:
        model = Lecture

