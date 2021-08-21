import requests
import xml.etree.ElementTree as et


# Exercise 4.1
# Create a function create_xml_body_from_string()
# that returns a docstring (with triple double quotes)
# containing the following XML document:
# <payee>
#     <name>John Smith</name>
#     <address>
#         <street>My street</street>
#         <city>My city</city>
#         <state>My state</state>
#         <zipCode>90210</zipCode>
#     </address>
#     <phoneNumber>0123456789</phoneNumber>
#     <accountNumber>12345</accountNumber>
# </payee>
def use_xml_string_block_body():
    return """
    <payee>
        <name>John Smith</name>
        <address>
            <street>My street</street>
            <city>My city</city>
            <state>My state</state>
            <zipCode>90210</zipCode>
        </address>
        <phoneNumber>0123456789</phoneNumber>
        <accountNumber>12345</accountNumber>
    </payee>
    """


# Exercise 4.2
# Write a test that POSTs the object created in 4.1
# to http://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500
# Set the request header 'Content-Type' to 'application/xml'
# Then check that the response status code is 200
# and that the value of the response header 'Content-Type' is also equal to 'application/xml'
def test_send_xml_body_from_docstring_check_status_code_is_200_and_name_is_correct():
    response = requests.post(
        "http://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
        headers={"Content-Type": "application/xml"},
        data=use_xml_string_block_body(),
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"


# Exercise 4.3
# Write a method create_xml_body_using_elementtree() that returns
# the same request body as in Exercise 4.1, but now uses the
# ElementTree library (I've imported that for you already, it's available as 'et')
# Make your life a little easier by specifying all element values as strings

def create_xml_body_from_string():
    payee = et.Element("payee")
    name = et.SubElement(payee, "name")
    name.text = "John Smith"
    address = et.SubElement(payee, "address")
    address_street = et.SubElement(address, "street")
    address_street.text = 'My street'
    address_city = et.SubElement(address, "city")
    address_city.text = 'My city'
    address_state = et.SubElement(address, "state")
    address_state.text = 'My state'
    address_zipCode = et.SubElement(address, "zipCode")
    address_zipCode.text = '90210'
    phoneNumber = et.SubElement(payee, "phoneNumber")
    phoneNumber.text = "0123456789"
    accountNumber = et.SubElement(payee, "accountNumber")
    accountNumber.text = "12345"

    return payee

# Exercise 4.4
# Repeat Exercise 4.2, but now use the XML document created in Exercise 4.3
# Don't forget to convert the XML document to a string before sending it!


def test_send_xml_body_from_elementtree_check_status_code_is_200_and_name_is_correct():
    xml = create_xml_body_using_elementtree()
    xml_as_string = et.tostring(xml)
    response = requests.post(
        "http://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500",
        headers={"Content-Type": "application/xml"},
        data=xml_as_string,
    )
    print(response.request.body)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
