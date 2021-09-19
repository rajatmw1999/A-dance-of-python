import msgpack

# Define data
data = {
  "PushRateRequest": {
    "Envelope": {
      "SenderID": "string",
      "ReceiverID": "string",
      "AccessToken": "string",
      "Type": "string",
      "Version": "string",
      "RequestID": -22801399999999.8
    },
    "RateDetails": {
      "RateHeader": {
        "Customer": "string",
        "MemberSCAC": "AB",
        "MemberOfficeCode": "string",
        "OriginRegion": "string",
        "OriginInlandCFS": "ABCD",
        "OriginConsolCFS": "AB",
        "PortOfLoading": "AB",
        "Transhipment_1": "ABCD",
        "Transhipment_2": "AB",
        "Transhipment_3": "A",
        "DestinationRegion": "string",
        "PortOfDischarge": "AB",
        "DestinationConsolCFS": "ABC",
        "DestinationInlandCFS": "ABC",
        "QuotingRegion": "string",
        "DeleteAllRate": "Y/N"
      },
      "ChargeDetails": [
        {
          "ChargeName": "string",
          "ChargeCode": "string",
          "Aspect": "string",
          "Currency": "ABC",
          "Rate": 11716500000000.2,
          "Basis": "string",
          "Minimum": -31641799999999.8,
          "Maximum": -41910699999999.8,
          "EffectiveDate": "2004-04-18",
          "ExpirationDate": "2001-08-21",
          "ScaleUom": "W/M",
          "From": 10409300000000.2,
          "To": 28200000000000.2,
          "Notes": "string",
          "Delete": "",
          "IsMandatory": "Y/N"
        },
        {
          "ChargeName": "string",
          "ChargeCode": "string",
          "Aspect": "string",
          "Currency": "ABC",
          "Rate": 11716500000000.2,
          "Basis": "string",
          "Minimum": -31641799999999.8,
          "Maximum": -41910699999999.8,
          "EffectiveDate": "2004-04-18",
          "ExpirationDate": "2001-08-21",
          "ScaleUom": "W/M",
          "From": 10409300000000.2,
          "To": 28200000000000.2,
          "Notes": "string",
          "Delete": "",
          "IsMandatory": "Y/N"
        }
      ]
    }
  }
}

# Write msgpack file
with open("data.msgpack", "wb") as outfile:
    packed = msgpack.packb(data)
    outfile.write(packed)

# Read msgpack file
with open("data.msgpack", "rb") as data_file:
    byte_data = data_file.read()

data_loaded = msgpack.unpackb(byte_data)
print(data == data_loaded)