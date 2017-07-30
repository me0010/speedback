# speedback
Entered Govhack 2017

Speedback is a new app that is designed to engage the community in road safety and safer speed limits on their roads. By providing a tool that allows them to provide feedback to the government and other interested agencies about the their expectation on the speed limits on the roads surrounding them.

We downloaded the raw sign data from data.gov.au which came to us in a number of different formats, which were converted to a csv format for easy data extraction. Then the speed sign data was extracted from the list of all the other sign data. The data from all the states were merged together, then uploaded to a NoSQL datastore for high speed extraction.

Then this app will create new data from the users clicking to increase/decrease the speed limits on the roads that they drive on every day, which will be stored in a NoSQL datastore. This data will be available for download in a convenient csv format or be viewed on a map on the speedback website.
