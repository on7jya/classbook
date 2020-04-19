from django.db.models import QuerySet, Count, Q


class StudentQuerySet(QuerySet):

    def assigned_courses_count(self):
        return self.annotate(assigned_courses=Count('courses_set', distinct=True))

    def completed_courses_count(self):
        return self.annotate(
            completed_courses=Count('courses_set', filter=Q(courses_set__is_completed=True), distinct=True))


StudentManager = StudentQuerySet.as_manager
