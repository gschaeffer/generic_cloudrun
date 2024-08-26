<h1 align="center">
<img src="img/warning.png" alt="SCC Alerts" width="100px">
<br>Cloud Run Testing App
</h1>
<h5 align="center">A very simple Google Cloud Run app for testing.</h5>
<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Using the App</a> •
  <a href="#cleanup">Cleanup</a>
</p>

## Features

An app that accepts args or json and then logs the data and limited request calling info into Google Cloud Logging. The logged data will show under the jsonPayload rather than textPayload as it uses structured logging.

## Installation

### Clone the repository 

[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/gschaeffer/generic_cloudrun.git&cloudshell_git_branch=main)

Clone the repo to Cloud Shell. Optionally, clone to a VM or your local machine if you prefer.
```bash
git clone https://github.com/gschaeffer/generic_cloudrun.git
```

#### Enable services

Enable the services as needed. 

```bash
# Cloud Run API 
gcloud services enable run.googleapis.com
```

#### Edit variables

Feel free to edit the file 'deploy_cloudrun.sh' as needed.
Ensure your gcloud project value is set to the project you'd like to deploy to.
```bash 
gcloud config set core/project YOUR_PROJECT_ID
```
#### Run setup

Execute the deploy_cloudrun.sh file.

```bash
./deploy_cloudrun.sh

# if prompted with 'API [run.googleapis.com] not enabled 
#   on project. Would you like to enable and retry?', select 'y'.
```

This will install the simple Python Cloud Run app. 


## Using the App

Call the app as you wish. 

### via web
Navigate the url provided by the Cloud Run deployment. Curl instructions are provided at the roon ('/') url.

### via curl

``` bash
# using args
curl "HOST/exec?type=road-runner&speed=10"

# using json
curl HOST/exec -d '{"type": "coyote", "speed": "5"}' -H 'Content-Type: application/json'
```

## Cleanup

To remove the app use the web console to delete or gcloud commands.

```bash
# get the app (service) name
gcloud run services list

gcloud run services delete SERVICE-NAME
```