import json
import os
from haikunator import Haikunator
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import Deployment
from azure.mgmt.resource.resources.models import DeploymentMode
from azure.mgmt.resource.resources.models import DeploymentProperties
from collections import namedtuple
from types import SimpleNamespace


class Deployer(object):
    """Initialize the deployer class with subscription and resource group to deploy a logic app

    :raises KeyError: If AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, or AZURE_TENANT env variables are not defined
    """

    def __init__(self, subscription_id, resource_group):
        self.subscription_id = subscription_id
        self.resource_group = resource_group

        self.name_generator = Haikunator()
        self.name = self.name_generator.haikunate()

        credentials = ClientSecretCredential(
            client_id=os.environ['AZURE_CLIENT_ID'],
            client_secret=os.environ['AZURE_CLIENT_SECRET'],
            tenant_id=os.environ['AZURE_TENANT_ID']
        )
        self.client = ResourceManagementClient(credentials, subscription_id)

    def get_template_path(self):
        return self.template_path

    def deploy(self, parameters):
        """Deploy resource to resource group"""

        with open(self.get_template_path(), "r") as tfd:
            template = json.load(tfd)
        print("PARAMETERS={}".format(parameters))
        print("TEMPLATE={}".format(template))

        # Deployment is an asynchronous operation
        deployment = self.client.deployments.begin_create_or_update(
            self.resource_group,
            self.name,
            Deployment(
                properties=DeploymentProperties(
                    mode=DeploymentMode.incremental,
                    template=template,
                    parameters={
                        k: {"value": v}
                        for k, v in parameters.items()
                    }
                )
            )
        )
        deployment.wait()
        

    def destroy(self):
        """Break down the resource"""
        pass
        