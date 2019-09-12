from django.utils.encoding import force_text


class BaseImporter:
    """
    Base Importer method to create simples importes files.
    set_reader: can be override to create new importers files
    """

    def __init__(self, file, *args, **kwargs):
        self.file = file
        self.delimiter = self.set_reader()
        self.headers = []
        self._cleaned_data = ()

    @staticmethod
    def to_unicode(bytestr):
        """
        Receive string bytestr and try to return a utf-8 string.
        """
        decoded = bytestr.decode('utf-8', 'ignore')
        return decoded

    def process_row(self, lines):
        """
        Read clean functions from importer and return tupla with row number, field and value
        """
        values_encoded = [self.to_unicode(i) for i in lines]
        return values_encoded

    def exclude_fields(self):
        """
        Exclude fields
        """

    def is_valid(self):
        """
        Clear content and return False if have errors
        """

    def set_reader(self):
        """
        Method responsable to convert file content into a list with same values that
        have fields
        """
        raise NotImplementedError('No reader implemented')

    def _read_file(self):
        """
        Create cleaned_data content
        """

        if hasattr(self.file, 'readlines'):
            enconded_data = self.process_row(self.file.readlines())
            return enconded_data

    def split_content(self, data):
        data = data.replace(" ", "").split(self.delimiter)
        if data.__len__() > 10:
            # return [data[3], data[4], data[5], data[7], data[9]]
            data.pop(0)
            data.pop()
            return data

    def cleaned_data(self):
        """
        Return tupla with data cleaned
        """

        # create clean content
        for i, data in enumerate(self._read_file()):
            if i == 12:
                self.headers = self.split_content(data)
            else:
                data = self.split_content(data)
                if data:
                    data = dict(zip(self.headers, data))
                    self._cleaned_data += (data,)

        return self._cleaned_data

    def save(self, instance=None):
        """
        Save all contents
        """

