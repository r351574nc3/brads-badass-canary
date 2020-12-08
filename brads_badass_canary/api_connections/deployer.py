import os
from brads_badass_canary import deployer


class Deployer(deployer.Deployer):
    """Initialize the deployer class with subscription and resource group to deploy a logic app

    :raises KeyError: If AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, or AZURE_TENANT env variables are not defined
    """

    def __init__(self, subscription_id, resource_group):
        super().__init__(subscription_id, resource_group)
        template_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "templates",
            "api-connection-deployment-tpl.json"
        )
        self.template_path = template_path
