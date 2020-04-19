from django.db.models import QuerySet, Count


class CourseQuerySet(QuerySet):

    def participators_count(self):
        return self.annotate(students_count=Count('participants_set', distinct=True))


CourseManager = CourseQuerySet.as_manager
