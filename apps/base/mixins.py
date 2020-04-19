from rest_framework.response import Response
from rest_framework import status


class ActionMixin:

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_action(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_action(self, serializer):
        raise NotImplementedError()

    def get_serializer(self, *args, **kwargs):
        raise NotImplementedError()
