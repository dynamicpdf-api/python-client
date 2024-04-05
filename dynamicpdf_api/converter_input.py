import uuid
from .input import Input
from .unit_converter import UnitConverter
from .page_orientation import PageOrientation

class ConverterInput(Input):
    '''
    Represents the base class for inputs
    '''

    def __init__(self, resource, size, orientation, margins):

        super().__init__(resource)
        self._page_size = size
        self._page_orientation = orientation

         # Gets or sets the top margin.
        self.top_margin = margins

        # Gets or sets the bottom margin.
        self.bottom_margin = margins

        # Gets or sets the right margin.
        self.right_margin = margins

        # Gets or sets the left margin.
        self.left_margin = margins

        # Gets or sets the width of the page.
        self.page_width = None

        # Gets or sets the height of the page.
        self.page_height = None
        
    @property
    def page_size(self):
        '''
        Gets the page size.
        '''
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        '''
        Sets the page size.
        '''
        self._page_size = value
        smaller, larger = UnitConverter._get_paper_size(value)
        if self._page_orientation == PageOrientation.Portrait:
            self.page_height = larger
            self.page_width = smaller
        else:
            self.page_height = smaller
            self.page_width = larger

    @property
    def page_orientation(self):
        '''
        Gets page orientation.
        '''
        return self._page_orientation

    @page_orientation.setter
    def page_orientation(self, value):
        '''
        Sets page orientation.
        '''
        self._page_orientation = value
        smaller, larger = UnitConverter._get_paper_size(self.page_size)
        if self.page_width > self.page_height:
            smaller, larger = self.page_height, self.page_width
        if self._page_orientation == PageOrientation.Portrait:
            self.page_height = larger
            self.page_width = smaller
        else:
            self.page_height = smaller
            self.page_width = larger
    

   