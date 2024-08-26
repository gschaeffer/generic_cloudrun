export PROJECT=$(gcloud config get-value project | tr ':' '/')

gcloud run deploy testing_app \
    --cpu=2000m \
    --allow-unauthenticated \
    --max-instances=1 \
    --memory=2Gi \
    --region=us-central1 \
    --source .

    # --service-account=SA_NAME@$PROJECT.iam.gserviceaccount.com \
    # --ingress internal-and-cloud-load-balancing \
    # --cpu-boost%