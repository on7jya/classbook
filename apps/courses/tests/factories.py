import datetime
import factory

from django.utils.timezone import now
from apps.courses.models import Course, Lecture


class CourseFactory(factory.DjangoModelFactory):
    id = factory.Faker('sentence', nb_words=1)
    name = factory.Faker('sentence', nb_words=2)
    description = factory.Faker('text')
    start_date = factory.LazyAttribute(lambda i: now() - datetime.timedelta(days=4))
    end_date = factory.LazyAttribute(lambda i: now() + datetime.timedelta(days=3))

    class Meta:
        model = Course


class LectureFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence')
    topic = factory.Faker('text')
    course = factory.SubFactory(CourseFactory)

    class Meta:
        model = Lecture
