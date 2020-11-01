from django.shortcuts import render
from rest_framework.views import APIView
import pandas as pd
from django.http import JsonResponse
from .models import Vendor, Invoice


class Upload(APIView):
    def save(self, data):
        for index, row in data.iterrows():
            if Vendor.objects.filter(code=row["Vendor Code"]).exists():
                vendor = Vendor.objects.get(code=row["Vendor Code"])
            else:
                vendor = Vendor.objects.create(
                    code=row["Vendor Code"],
                    name=row["Vendor name"],
                    type=row["Vendor type"],
                )

            if Invoice.objects.filter(document_number=row["Document Number"]).exists():
                continue
            else:
                Invoice.objects.create(
                    vendor=vendor,
                    document_number=row["Document Number"],
                    invoice_numbers=row["Invoice Numbers"],
                    type=row["Type"],
                    due_date=row["Net due dt"],
                    doc_date=row["Doc. Date"],
                    posting_date=row["Pstng Date"],
                    amount_in_loc=row["Amt in loc.cur."],
                )

    def post(self, request):
        breakpoint()
        xls = request.FILES.get("doc")
        data = pd.read_excel(xls)
        self.save(data)
        return JsonResponse({"file": True})
