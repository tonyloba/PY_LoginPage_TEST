import requests
import xml.etree.ElementTree as ET


def test_soap_add_operation():
    url = "http://www.dneonline.com/calculator.asmx"

    # SOAP Envelope (XML Body)
    body = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <Add xmlns="http://tempuri.org/">
          <intA>5</intA>
          <intB>7</intB>
        </Add>
      </soap:Body>
    </soap:Envelope>
    """

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://tempuri.org/Add"
    }

    response = requests.post(url, data=body, headers=headers)

    assert response.status_code == 200

    # Parse XML Response
    root = ET.fromstring(response.text)
    result = root.find(".//{http://tempuri.org/}AddResult").text

    assert result == "12"
