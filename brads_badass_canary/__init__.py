import os
from brads_badass_canary import api_connections
from brads_badass_canary import logic_app

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '11111111-1111-1111-1111-111111111111') # your Azure Subscription Id
resource_group = os.environ.get(
    'AZURE_DEFAULT_RESOURCE_GROUP',
    'my-resource-group') # Resource group to deploy to
location = os.environ.get('LOCATION', 'centralus')

def la_deployer():
    return logic_app.deployer.Deployer(subscription_id, resource_group)

def conn_deployer():
    return api_connections.deployer.Deployer(subscription_id, resource_group)

def deploy(name):
    """Deploys necessary API connections and Logic App

    :param name: Name of the logic app to build and deploy
    :type string: 
    """
    print("Deploying API Connections to subscription {}...".format(subscription_id))
    for params in [
        {   
            "provider_name": "azurecommunicationservicessms",
            "connection_name": "sms-service",
            "subscription_id": subscription_id,
        },
        {
            "provider_name": "office365",
            "connection_name": "office365-service",
            "subscription_id": subscription_id,
        },
        {
            "provider_name": "teams",
            "connection_name": "teams-service",
            "subscription_id": subscription_id,
        },
    ]:
        conn_deployer().deploy(params)
    print("Deployment complete.")

    print("Deploying Canary...")
    retval = la_deployer().deploy(
        {
            "subscription_id": subscription_id,
            "resource_group": resource_group,
            "workflows_notification_app_name": name
        }
    )
    print("Deployment complete.")
    return retval