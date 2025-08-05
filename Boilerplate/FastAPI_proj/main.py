from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

import uuid


## General requirements
# auth: user needs to provide API key in the authorization header: Authorization: Bearer <your_api_key>
# get data as payload --> send to an alert destination (i.e. SMS gateway)

app = FastAPI()

# security scheme
security = HTTPBearer()
API_KEY =  "".join(str(uuid.uuid4()).split('-'))

@app.on_event("startup")
async def startup_event():
    print(f"🔑 API Key: {API_KEY}")
    print(f"🚀 Application started! Use this API key for authentication.")
print(f"Usage: curl -X POST http://localhost:8000/receive "
      f"-H \"Authorization: Bearer {API_KEY}\" "
      f"-H \"Content-Type: application/json\" "
      f"-d '{{\"message\": \"Hello FastAPI\" }}'")


# only use await inside of functions created with async def
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Define expected request body using Pydantic for Grafana webhooks
class AlertLabel(BaseModel):
    alertname: str
    grafana_folder: str
    instance: str


def create_twilio_client():
    import os
    from twilio.rest import Client

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)


    message = client.messages.create(
        body="test alert",
        from_="+16075364794", # virtual number provided by Twilio
        to="+40728593748",
    )

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify the provided API key"""
    if credentials.scheme.lower() != "bearer" or credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
        )
    return credentials.credentials


# Protected POST endpoint
@app.post("/receive")
async def receive_data(request: Request, token: str = Depends(verify_token)):
    body = await request.json()
    print("Raw incoming webhook:", body)
    print ("Status:", body.get("status", "No status provided"))
    if body.get("status") == "firing":
      create_twilio_client()
    return {"status": "received"}
