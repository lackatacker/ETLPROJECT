-run
and use my transactions_example.csv

python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py createsuperuser

and then in the http://127.0.0.1:8000/admin/

create two transformationBlocks

Operation:subtractFees
Percentage:5
Label:Subtract fees

Operation:addFees
Percentage:5
Label:Mastercard Fees
⌢䔠䱔剐䩏䍅≔ഠ�