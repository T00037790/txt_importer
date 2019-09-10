from rest_framework import viewsets
from custom_importer.api.serializers import FileSerializer
from custom_importer.models import TextImporter
from django.core.files import File
from custom_importer.importer import TxtImporter


class ImporterViewSets(viewsets.ModelViewSet):
    """
       A viewset for viewing and editing user instances.
    """
    serializer_class = FileSerializer
    queryset = TextImporter.objects.all()

    def create(self, request, *args, **kwargs):
        file = self.request.data.get('file')
        file = File.open(file)

        if file.content_type == 'text/plain':
            TxtImporter(file)
        else:
            raise Exception("only support text files")
