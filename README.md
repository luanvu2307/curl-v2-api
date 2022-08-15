# curl-v2-api
## Running as a container in Local
Step 1: Config Port
+ open Dockerfile and specify ENV PORT - line 44 (default 2307).
+ open bash file run.sh and specify EXPOSE_PORT - line 1, line 6, line 11 (default 2307).

Step 2: Config Json File

+ Config json file in Dockerfile - line 46, this json file would support to write log in Google Cloud Run.

Step 3: Run bash file
"bash run.sh"

## Build and deploy API to Google Cloud Run
# Build
$TAG="gcr.io/$PROJECT_ID/$NAME" - defaultL "gcr.io/brand-insight-testing/curl-v2-api"
If timeout param was not set, the build process have to be completed in 10 mins.
+ gcloud builds submit --tag $TAG --timeout=3600s

# Deploy
+ gcloud run deploy --image $TAG --platform managed --region asia-northeast1 --allow-unauthenticated