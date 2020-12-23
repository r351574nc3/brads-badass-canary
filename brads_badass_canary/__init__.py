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

def deploy(
    name,
    teams_override=None,
    sms_override=None,
    office365_override=None,
    ):
    """Deploys necessary API connections and Logic App

    :param name: Name of the logic app to build and deploy
    :type string: 
    """

    # Only deploy API Connections if not overriding
    if teams_override is None:
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
    if teams_override is not None:
        retval = la_deployer().deploy(
            {
                "subscription_id": subscription_id,
                "resource_group": resource_group,
                "workflows_notification_app_name": name,
                "teams_connector_override": teams_override,
                "sms_connector_override": sms_override,
                "office365_connector_override": office365_override,
            }
        )
    else:
        retval = la_deployer().deploy(
            {
                "subscription_id": subscription_id,
                "resource_group": resource_group,
                "workflows_notification_app_name": name
            }
        )
        
    print("Deployment complete.")
    return retval