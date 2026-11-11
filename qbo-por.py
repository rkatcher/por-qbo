from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from dotenv import load_dotenv
import os


# load .env file 
load_dotenv() 
my_client_id = os.environ.get("CLIENT_ID")
my_client_secret = os.environ.get("CLIENT_SECRET")
my_refresh_token = os.environ.get("REFRESH_TOKEN")
my_realm_id = os.environ.get("REALM_ID")
 
auth_client = AuthClient(
    client_id=my_client_id,
    client_secret=my_client_secret,
    environment='production',  # Switch to 'production' when ready
    redirect_uri='https://www.example.com',
)

client = QuickBooks(
    auth_client=auth_client,
    refresh_token=my_refresh_token,
    company_id=my_realm_id,
)

# Query all customers from your QuickBooks company
customers = Customer.all(qb=client)

for customer in customers:
    print(f"Customer Name: {customer.DisplayName}")

