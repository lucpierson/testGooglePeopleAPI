import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
GLOBAL_SCOPES = ['https://www.googleapis.com/auth/contacts']
GLOBAL_CONNECTION_LIST = None
GLOBAL_CREDS=None
GLOBAL_CONTACT_TO_UPDATE=None

def SetGoogleCredentials():

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # credentials.json file placed at root is downloaded from your
    # https://console.cloud.google.com/apis/credentials OAuth 2.0 Client IDs
    creds = None
    global GLOBAL_CONNECTION_LIST
    global GLOBAL_CREDS

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', GLOBAL_SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', GLOBAL_SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.json', 'w') as token:
            token.write(creds.to_json())

    GLOBAL_CREDS=creds

    try:
        # Find all contacts and gather list
        service = build('people', 'v1', credentials=creds)
        connections_Name= service.people().connections().list(resourceName='people/me', personFields='names', pageSize=500).execute().get('connections', [])
    except Exception as e:
        print(f"Error while getting Google contacts : {e}")
        return(False)
   
    GLOBAL_CONNECTION_LIST=connections_Name
    return(True)



def Recherche_main(query):
    global GLOBAL_CONNECTION_LIST
    global GLOBAL_CREDS
    global GLOBAL_CONTACT_TO_UPDATE
    # Find contact on DisplayName or on GivenName
    contact_bool_found=False
    for contact in GLOBAL_CONNECTION_LIST:
        names = contact.get('names', [])
        try:
            display_name = names[0].get('displayName')+' '+names[0].get('givenName')
        except Exception as e:
            print("Contact Exception on the " + str(contact) + " of the list")
        Contact_Found = display_name.lower().find(query.lower())
        if Contact_Found != -1:
            contact_bool_found=True
            GLOBAL_CONTACT_TO_UPDATE=contact
            return(contact_bool_found)
    return(contact_bool_found)

def  update_contact(Nouveau_nom,email_add,tel_num,mob,compagnie):
    global GLOBAL_CREDS
    global GLOBAL_CONTACT_TO_UPDATE
    try:
        service = build('people', 'v1', credentials=GLOBAL_CREDS)
        contact_id = GLOBAL_CONTACT_TO_UPDATE['resourceName']
        etag_id = GLOBAL_CONTACT_TO_UPDATE['etag']
        update_Metadata = 'names,emailAddresses,phoneNumbers,organizations'
        ToBeUpdated_contact = {
            'names': [
                {
                    'givenName': Nouveau_nom,
                    'unstructuredName': Nouveau_nom,
                }
            ],
            'emailAddresses': [
                {
                    'value': email_add,
                    "type": "home"
                }
            ],
            "phoneNumbers": [
                {
                    "value": mob,
                    "type": "Mobile"
                },
                {
                    "value": tel_num,
                    "type": "Work"
                }
            ],
            "organizations": [
                {
                    "name": compagnie,
                }
            ],
            "etag":etag_id
        }
        # contact update
        service.people().updateContact(resourceName=f'{contact_id}', updatePersonFields=update_Metadata, body=ToBeUpdated_contact).execute()
        print('Contact updated:', ToBeUpdated_contact)
    except Exception as err:
        print(err)    



def create_contact(Nouveau_nom,email_add,tel_num,mob,compagnie):
    global GLOBAL_CREDS
    try:
        service = build('people', 'v1', credentials=GLOBAL_CREDS)
        ToBeCreated_contact = {
            'names': [
                {
                    'givenName': Nouveau_nom,
                    'unstructuredName': Nouveau_nom,
                }
            ],
            'emailAddresses': [
                {
                    'value': email_add,
                    "type": "home"
                }
            ],
            "phoneNumbers": [
                {
                    "value": mob,
                    "type": "Mobile"
                },
                {
                    "value": tel_num,
                    "type": "Work"
                }
            ],
            "organizations": [
                {
                    "name": compagnie,
                }
            ]
        }
        # Launch Contact Creation
        created_contact = service.people().createContact(body=ToBeCreated_contact).execute()
        print('Contact created:', ToBeCreated_contact)
    except Exception as err:
        print(err)    

    
if __name__ == '__main__':
    BOUL_MAIN=SetGoogleCredentials()
    if BOUL_MAIN:
        Contact_recherche = "tutu"
        Contact_email = "duschmol_tutu@toto.com"
        Contact_mobile="+88990"
        Contact_cie="Federation of bullshit"
        Contact_tel="+9999"
        if Recherche_main(Contact_recherche):
            update_contact(Contact_recherche,Contact_email,Contact_tel,Contact_mobile,Contact_cie)
        else:
            create_contact(Contact_recherche,Contact_email,Contact_tel,Contact_mobile,Contact_cie)
