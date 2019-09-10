

class BaseImporter:
    """
    Base Importer method to create simples importes files.
    set_reader: can be override to create new importers files
    """

    def __init__(self, file, *args, **kwargs):
        self.file = file

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

    def save(self, instance=None):
        """
        Save all contents
        """
