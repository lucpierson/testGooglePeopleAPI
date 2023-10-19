# testGooglePeopleAPI
Test how to use the People API from Google to manipulate my account's contacts.

Guide to setup you' OAuth consent : https://developers.google.com/people/quickstart/python

# Install

- Clone the project.
- Add your credentials.json you've downloaded from your OAuth configuration.
- Then:
```
> pip install -r requirements.txt
...
> python main.py
>>>>>>>> List 10 connection names
        contact@test1.fr
        contact@test2.fr
        contact@test3.fr
        contact@test4.fr
        contact@test5.fr
        contact@test6.fr
        contact@test7.fr
        contact@test8.fr
        contact@test9.fr
        contact@test10.fr

 >>>>>>>> Add  new contact John Duschmol

>>>>>>>>New Contact created >>> {'resourceName': 'people/c6945380952345793733', 'etag': '%EigBAgMEBQYHCAkKCwwNDg8QERITFBUWFxkfISIjJCUmJy40NTc9Pj9AGgQBAgUHIgw5bWc0b3BGanplaz0=', 'metadata': {'sources': [{'type': 'CONTACT', 'id': '6062f32d8e55d4c5', 'etag': '#9mg4opFjzek=', 'updateTime': '2023-10-19T19:51:29.115366Z'}], 'objectType': 'PERSON'}, 'photos': [{'metadata': {'primary': True, 'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'url': 'https://lh3.googleusercontent.com/cm/AH_dcDn0HNMN7mV8yB2U7R9biaPtjZbW5iauZN11n-IKsbZ3oxEnkXWEhlNIlDPUIkoi=s100', 'default': True}], 'addresses': [{'metadata': {'primary': True, 'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'formattedValue': 'rue des Grouettes\n26\n78790 Courgent, Yvelines, Ile de France\nFrance', 'type': 'work', 'formattedType': 'Work', 'poBox': '26', 'streetAddress': 'rue des Grouettes', 'city': 'Courgent', 'region': 'Yvelines, Ile de France', 'postalCode': '78790', 'country': 'France', 'countryCode': 'FR'}], 'emailAddresses': [{'metadata': {'primary': True, 'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'value': 'john.duschmol@temlab.fr', 'type': 'home', 'formattedType': 'Home'}], 'phoneNumbers': [{'metadata': {'primary': True, 'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'value': '+33766886312', 'canonicalForm': '+33766886312', 'type': 'work', 'formattedType': 'Work'}, {'metadata': {'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'value': '+33766886312', 'canonicalForm': '+33766886312', 'type': 'home', 'formattedType': 'Home'}], 'memberships': [{'metadata': {'source': {'type': 'CONTACT', 'id': '6062f32d8e55d4c5'}}, 'contactGroupMembership': {'contactGroupId': 'myContacts', 'contactGroupResourceName': 'contactGroups/myContacts'}}]}

>>>>>>>> DELETE ResourceName  people/c6945380952345793733
```

