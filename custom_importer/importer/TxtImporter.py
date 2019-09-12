from .Base import BaseImporter


class TxtImporter(BaseImporter):

    def set_reader(self):
        """
        :return: delimiter
        """
        self.delimiter = '|'

        return self.delimiter

    def save(self, instance=None):
        """
            Save all contents
        """
        for row in self._cleaned_data:
            to_save = instance()
            try:
                to_save.posting_period = row.get('PostingPeriod')
                to_save.fiscal_year = row.get('FiscalYear')
                to_save.customer = row.get('Customer')
                to_save.sales_order = row.get('SalesOrder')
                to_save.bill_document = row.get('Billdocument')
                to_save.save()
            except Exception as e:
                print(e)
