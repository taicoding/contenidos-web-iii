from zeep import Client

client = Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')
result = client.service.NumberToWords(5)
print(result)
result_dollars  = client.service.NumberToDollars(5)
print(result_dollars)
