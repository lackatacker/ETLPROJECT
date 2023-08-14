from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, TransformationBlock
from .serializers import TransactionSerializer, TransformationBlockSerializer
from .service import add_six_percent_to_amounts, subtract_percentage_from_amounts


class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        # Convert the string amount to a decimal number
        if isinstance(data, list):
            for item in data:
                item['amount'] = float(item.get('amount', 0))
        else:
            data['amount'] = float(data.get('amount', 0))

        updated_records = []  # Collect records for update or create

        # Iterate through the data and prepare records for update or create
        for item in data:
            transaction_id = item.get('transactionID')
            if transaction_id:
                try:
                    existing_record = Transaction.objects.get(
                        transactionID=transaction_id)
                    # Update existing record with new data
                    existing_record.amount = item['amount']
                    existing_record.date = item['date']
                    existing_record.merchantName = item['merchantName']
                    updated_records.append(existing_record)
                except Transaction.DoesNotExist:
                    # Create a new record with the given transactionID
                    updated_records.append(Transaction(**item))
            else:
                # Create a new record (no transactionID provided)
                updated_records.append(Transaction(**item))

        # Save the updated or created records
        for record in updated_records:
            record.save()

        # Serialize the updated or created records
        serializer = TransactionSerializer(updated_records, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransformationBlockView(APIView):
    def get(self, request, *args, **kwargs):
        blocks = TransformationBlock.objects.all()
        serializer = TransformationBlockSerializer(blocks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TransformationBlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransformProcess(APIView):
    def post(self, request):
        operation = request.data.get("operation")
        uploaded_data = request.data.get("transactions")
        if (operation == "addFees"):
            transformed_data = add_six_percent_to_amounts(uploaded_data)
        if (operation == "subtractFees"):
            transformed_data = subtract_percentage_from_amounts(uploaded_data)
        serializer = TransactionSerializer(transformed_data, many=True)
        return Response(serializer.data)
