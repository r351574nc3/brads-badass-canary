import os
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '11111111-1111-1111-1111-111111111111') # your Azure Subscription Id
credentials = ClientSecretCredential(
    client_id=os.environ['AZURE_CLIENT_ID'],
    client_secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant_id=os.environ['AZURE_TENANT_ID']
)
location = os.environ.get('LOCATION', 'centralus')
client = ResourceManagementClient(credentials, subscription_id)

def print_item(group):
    """Print a ResourceGroup instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    print("\tLocation: {}".format(group.location))
    print("\tTags: {}".format(group.tags))
    print_properties(group.properties)


def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")

def run():
    print("List all of the resources within the group")
    for item in client.resources.list_by_resource_group("cde-nonprod"):
        print_item(item)