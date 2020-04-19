from rest_framework import status

course_assign = {
    'operation_summary': "Assign student to specific course",
    'responses': {
        status.HTTP_204_NO_CONTENT: ''
    }
}

course_unassign = {
    'operation_summary': "Unassign student from specific course",
    'responses': {
        status.HTTP_204_NO_CONTENT: ''
    }
}
