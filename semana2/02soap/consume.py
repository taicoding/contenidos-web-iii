from zeep import Client

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = client.service.NumberToWords(5)
print(result)