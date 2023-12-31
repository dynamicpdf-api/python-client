from .text_barcode_element import TextBarcodeElement
from .element_type import ElementType

class Iata25BarcodeElement(TextBarcodeElement):
    '''
    Represents an IATA 2 of 5 barcode element.
    
    Remarks:
        This class can be used to place an IATA 2 of 5 barcode on a page.
    '''
    
    def __init__(self, value, placement, height, x_offset = 0, y_offset = 0):
        '''
        Initializes a new instance of the Iata25BarcodeElement class.

        Args:
            value (string): The value of the barcode.
            placement (ElementPlacement): The placement of the barcode on the page.
            height (integer): The height of the barcode.
            xOffset (integer): The X coordinate of the barcode.
            yOffset (integer): The Y coordinate of the barcode.
        '''

        super().__init__(value, placement, x_offset, y_offset)
        self._type = ElementType.IATA25Barcode

        # Gets or sets the height of the barcode.
        self.height = height

        # Gets or sets a value indicating if the check digit should be added to the value.
        self.include_check_digit = None

    def to_json(self):
        json = {
            "type": self._type,
            "value": self.value,
            "placement": self.placement,
            "xOffset": self.x_offset,
            "yOffset": self.y_offset,
            "height": self.height
        }
        if self._color_name:
            json["color"] = self._color_name
        if self.even_pages is not None:
            json["evenPages"] = self.even_pages
        if self.odd_pages is not None:
            json["oddPages"] = self.odd_pages
        if self.x_dimension:
            json["xDimension"] = self.x_dimension
        if self.font_size:
            json["fontSize"] = self.font_size
        if self.show_text is not None:
            json["showText"] = self.show_text
        if self._font_name:
            json["font"] = self._font_name
        if self._text_color_name:
            json["textColor"] = self._text_color_name
        if self.include_check_digit:
            json['includeCheckDigit'] = self.include_check_digit
        return json
