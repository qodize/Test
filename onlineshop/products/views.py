from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Parameter


class ProductsView(APIView):
    def get(self, request):
        filter_by = request.data.get("filter_by", None)
        value = request.data.get("value", None)
        if filter_by is None:
            products = Product.objects.all()
        elif filter_by == "name":
            products = Product.objects.filter(name=value)
        else:
            products_raw = Product.objects.all()
            products = []
            for product in products_raw:
                f = False
                for param in product.params:
                    if param["key"] == filter_by:
                        if param["value"] == value:
                            f = True
                        break
                if f:
                    products.append(product)
        return Response(
            {
                "products": list([
                    {
                        "id": product.pk,
                        "name": product.name
                    } for product in products
                ])
            }
        )

    def post(self, request):
        try:
            params = request.data.get("params", dict())
            product = Product(
                name=request.data.get("name"),
                description=request.data.get("description", ''),
                params=list([
                    {
                        'key': key,
                        'value': params[key],
                        'new': '12'
                    } for key in params.keys()
                ])
            )
            product.save()
            return Response(
                {
                    "success": True,
                    "errors": []
                }
            )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "errors": ["some error"]
                },
                status=500
            )


class OneProductView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(pk=int(id))
            print(product.params)
            return Response(
                {
                    "product": {
                        "id": product.pk,
                        "name": product.name,
                        "desctiption": product.description,
                        "params": {
                            param["key"]: param["value"]
                            for param in product.params
                        }
                    }
                }
            )
        except Product.DoesNotExist as e:
            return Response(
                {
                    "errors": ["Product does not exist"]
                },
                status=404
            )
