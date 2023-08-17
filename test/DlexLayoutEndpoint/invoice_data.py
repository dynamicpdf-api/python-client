import datetime
import json

class InvoiceData:
    class Order:
        def __init__(self):
            self.OrderID = None
            self.OrderDate = None
            self.CustomerID = None
            self.ShippedDate = None
            self.ShipperName = None
            self.ShipTo = None
            self.BillTo = None
            self.Freight = None
            self.OrderDetails = []

        def to_json(self):
            order_details = []
            for detail in self.OrderDetails:
                order_details.append({
                    "ProductID": detail.ProductID,
                    "Quantity": detail.Quantity,
                    "ProductName": detail.ProductName,
                    "UnitPrice": detail.UnitPrice
                })

            json_data = {
                "OrderID": self.OrderID,
                "OrderDate": self.OrderDate.strftime('%d %b %Y'),
                "CustomerID": self.CustomerID,
                "ShippedDate": self.ShippedDate.strftime('%d %b %Y'),
                "ShipperName": self.ShipperName,
                "ShipTo": self.ShipTo,
                "BillTo": self.BillTo,
                "Freight": self.Freight,
                "OrderDetails": order_details
            }

            return json.dumps(json_data)

    class OrderDetail:
        def __init__(self):
            self.ProductID = None
            self.Quantity = None
            self.ProductName = None
            self.UnitPrice = None

    order11077 = Order()
    order11077.OrderID = 11077
    order11077.OrderDate = datetime.datetime(2019, 1, 6)
    order11077.CustomerID = "RATTC"
    order11077.ShippedDate = datetime.datetime(2019, 1, 30)
    order11077.ShipperName = "United Package"
    order11077.ShipTo = "Rattlesnake Canyon Grocery\n2817 Milton Dr.\nAlbuquerque, NM 87110\nUSA"
    order11077.BillTo = "Rattlesnake Canyon Grocery\n2817 Milton Dr.\nAlbuquerque, NM 87110\nUSA"
    order11077.Freight = 8.53
    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 2
    order11077.OrderDetails[-1].Quantity = 24
    order11077.OrderDetails[-1].ProductName = "Chang"
    order11077.OrderDetails[-1].UnitPrice = 19.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 3
    order11077.OrderDetails[-1].Quantity = 4
    order11077.OrderDetails[-1].ProductName = "Aniseed Syrup"
    order11077.OrderDetails[-1].UnitPrice = 10.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 4
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Chef Anton's Cajun Seasoning"
    order11077.OrderDetails[-1].UnitPrice = 22.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 6
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Grandma's Boysenberry Spread"
    order11077.OrderDetails[-1].UnitPrice = 25.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 7
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Uncle Bob's Organic Dried Pears"
    order11077.OrderDetails[-1].UnitPrice = 30.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 8
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Northwoods Cranberry Sauce"
    order11077.OrderDetails[-1].UnitPrice = 40.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 10
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Ikura"
    order11077.OrderDetails[-1].UnitPrice = 31.0
    
    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 12
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Queso Manchego La Pastora"
    order11077.OrderDetails[-1].UnitPrice = 38.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 13
    order11077.OrderDetails[-1].Quantity = 4
    order11077.OrderDetails[-1].ProductName = "Konbu"
    order11077.OrderDetails[-1].UnitPrice = 6.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 14
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Tofu"
    order11077.OrderDetails[-1].UnitPrice = 23.25

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 16
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Pavlova"
    order11077.OrderDetails[-1].UnitPrice = 17.45

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 20
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Sir Rodney's Marmalade"
    order11077.OrderDetails[-1].UnitPrice = 81.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 23
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Tunnbröd"
    order11077.OrderDetails[-1].UnitPrice = 9.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 32
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Mascarpone Fabioli"
    order11077.OrderDetails[-1].UnitPrice = 32.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 39
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Chartreuse verte"
    order11077.OrderDetails[-1].UnitPrice = 18.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 41
    order11077.OrderDetails[-1].Quantity = 3
    order11077.OrderDetails[-1].ProductName = "Jack's New England Clam Chowder"
    order11077.OrderDetails[-1].UnitPrice = 9.65

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 46
    order11077.OrderDetails[-1].Quantity = 3
    order11077.OrderDetails[-1].ProductName = "Spegesild"
    order11077.OrderDetails[-1].UnitPrice = 12.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 52
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Filo Mix"
    order11077.OrderDetails[-1].UnitPrice = 7.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 55
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Pâté chinois"
    order11077.OrderDetails[-1].UnitPrice = 24.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 60
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Camembert Pierrot"
    order11077.OrderDetails[-1].UnitPrice = 34.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 64
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Wimmers gute Semmelknödel"
    order11077.OrderDetails[-1].UnitPrice = 33.25

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 66
    order11077.OrderDetails[-1].Quantity = 1
    order11077.OrderDetails[-1].ProductName = "Louisiana Hot Spiced Okra"
    order11077.OrderDetails[-1].UnitPrice = 17.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 73
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Röd Kaviar"
    order11077.OrderDetails[-1].UnitPrice = 15.0

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 75
    order11077.OrderDetails[-1].Quantity = 4
    order11077.OrderDetails[-1].ProductName = "Rhönbräu Klosterbier"
    order11077.OrderDetails[-1].UnitPrice = 7.75

    order11077.OrderDetails.append(OrderDetail())
    order11077.OrderDetails[-1].ProductID = 77
    order11077.OrderDetails[-1].Quantity = 2
    order11077.OrderDetails[-1].ProductName = "Original Frankfurter grüne Soße"
    order11077.OrderDetails[-1].UnitPrice = 13.0
    
    @staticmethod
    def Order11077():
        return InvoiceData.order11077