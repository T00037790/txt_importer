from rest_framework import viewsets, status
from rest_framework.response import Response
from custom_importer.api.serializers import FileSerializer
from django.core.files import File
from custom_importer.importer.TxtImporter import TxtImporter
from custom_importer.models import TextImporter


class ImporterViewSets(viewsets.ModelViewSet):
    """
       A viewset for viewing and editing user instances.
    """
    serializer_class = FileSerializer
    queryset = TextImporter.objects.all().order_by('-id')[:5]

    def create(self, request, *args, **kwargs):
        file = self.request.data.get('files')
        file = File.open(file)

        if file.content_type == 'text/plain':
            file = TxtImporter(file)
            file.cleaned_data()
            file.save(TextImporter)
            return Response({'Success!': 'file processed with no errors'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'file must be txt'}, status=status.HTTP_200_OK)

