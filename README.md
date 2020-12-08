# brads-badass-canary

Azure Logic Apps for integration with Microsoft Teams. Basically, it's infrastructure component that just creates a Logic App that will expose an HTTP endpoint webhook to communicate with Microsoft Teams. Yay


## Testing Canary

Canary is a logic app deployed to azure. To test it we need to get the resource id and endpoint trigger name

```
curl -X POST -d@payload.json https://management.azure.com/{logic-app-resource-ID}/
```