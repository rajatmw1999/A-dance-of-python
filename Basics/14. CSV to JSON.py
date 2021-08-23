import csv
import json

# ------------------------------------------------------------
# TODO: FIND A EFFICIENT WAY TO INCLUDE HEADERS IN EACH ROW
# ------------------------------------------------------------

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['Status']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'SHPT_PLC_BALTRANS_20210702_145035824_1.csv'
jsonFilePath = r'Names.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)


{
  "PushRateRequest": {
    # "Envelope": {
    #   "SenderID": "string",
    #   "ReceiverID": "string",
    #   "AccessToken": "string",
    #   "Type": "string",
    #   "Version": "string",
    #   "RequestID": -22801399999999.8
    # },
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
        "DeleteAllRate": "Y/N",
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