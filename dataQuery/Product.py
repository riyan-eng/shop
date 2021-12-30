from main import models as mainModels
from django.http import JsonResponse

def dataProducts(req):
    dataProduct = mainModels.Product.objects.all()
    querySetProduct = []
    for x in dataProduct:
        querySetProduct.append(
            {
                'product_name': x.product_name,
                'product_price': x.product_price,
            }
        )
    return JsonResponse({'data': querySetProduct}, safe=False)