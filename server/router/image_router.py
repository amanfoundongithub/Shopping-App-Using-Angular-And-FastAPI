from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse
from firebase_admin import storage
import os

import firebase_admin
from firebase_admin import credentials

# Firebase configuration
firebase_config = {
  "type": "service_account",
  "project_id": "gotrip-a4fbd",
  "private_key_id": "7f1d5466f1c833e4752f5bb6b7856c9ac437b1e2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC+hvsqQAGCjfz/\nYfrj6AQPFosKZTPsfEhYJrwC5UwIFJC1lBK4HgOy/as1aOm2ax3+pKib2JPHOuVK\ndDhiqVtt3UBaJ3yr+p9KpA7Ot0vWMjK/+/MDTjXxaXnN8EFcs5UKgBxd2t/vrylS\nM9LNPHHW3kbnFKg1ad1XjbpS3HEYqe3QbLSjgbXKF4P13woE7bOoOc57GbeUBiSc\nAhgm8ewvj7cxa0cDYNyckCWwx13YggepD1caSmfqYNNdIq6U177S9WoBRa1o6PWj\nbwE00WiLR9tStoJJZodKsbMrsBQp/TMRfmCxyw301xf11nWlORoeMjw+1DygR81X\nB0LwMsPtAgMBAAECggEAGLJ4F9W0rGb56uPZSRYwAoGuU9JjDO5eVVjuCaUN+kUq\nLfNsCsRPP/I8cX+wPfZ8LKBM/+iu3UY/5ysSDQ39fUwPFbClK0jhQaRrC/Y8JR+c\nLwE6kszeVrUQtjaEzn6z3OjW5H6lBRWMUmzH0FVbv1nQUI9/r27R45HKW4faPDM/\nBDszswbfV93vHy+hJyRgMuIglk/+sre7PPGQR+yaoh9CjpjegJfQT0LfO+6wIYYH\nhKdOhP55pvl4ozckIvJHlG0OXYyO8K1khkPA5oVNxPZqscaUh0QLT5IXpwnp68eR\niPcMeEcGMPadkgh6ug3uAqywarixcXkNfaLeMuU8YQKBgQDAYBKQd2CwlJywLnI+\n6Bq3aK+CyH/cnjjQGjTOYG7X/4HSlJuKlifsfNMxNfes3IvCw5ZZd+ZVBMQoQvNq\nCmPiF82YCPN5A7fui4ZiH+/FiS4u4OpF+skFgFLHYTkkbYSaCNVIIgBZH6mJgXd2\nS2OHmeItVlIh1Ig3vs7yjqJkoQKBgQD9inEmrJcTfEW8+Jq7Eqck+3L1Gbns9Yhx\nqhcUrchZSWxWLbzr7WHkyJs2SMZ7vNzyhpl2hlvEcXwqOf2gKX9VzDcRJrzw/CAI\nhw8TWOOGx3use+JzWjUS2NDOwJng7UREbiS3lD6PMfPqa6kkoFJXm7qO7BdF4CwR\n0X6s6orPzQKBgQC/axktzMtWCRn8KMsfEx76Xt09Gjo4EOvhDiJ7M/M3VBMesSYv\n+QdSxkXy0otW4sDilHF3Jtn2wN5aXXwNiLcokpzNaiKxyGRtpUGbQ8H2YXClzsDt\nzwPVSIGVyITuXVczWhS3SLXl+J5ep4dyGsO3ewRWLm1dIjhEl8UeD5VA4QKBgQC8\n5Tc2JCIOr2jZyLKnK9eBsyFLwNYH2ErGvH2jt3HsK8reTgdSEzL7HAafpArUx7op\nquSNLL8UFaT3ZOs0N5aaGqLwUVc1h/JpyA4QUQp7MQZQVKA7Zvrhxs2TLGW48a0J\n+rG6YGVXlFTw0zNaiWOvx+NvdjBErCbJQ7bIJ5oyBQKBgQCmCyH2+T5szoDqjhfr\nIYhspGNWVT1im/YMt0v3ciMDK0hqaAQ1kcQQ52gH82WbIEfQlaNhFXGFc/BxS0VU\nvGUNc71qwBvGei/oSG5SkmmUO8R0OsPCzL+JT6aZ1qfpJlvlxP80MCcv9XgAPmsd\nMU/NCvAjq4ymp6lxbbW1Tun5JA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-oaesx@gotrip-a4fbd.iam.gserviceaccount.com",
  "client_id": "108261705287777278789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-oaesx%40gotrip-a4fbd.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    "storageBucket": "gotrip-a4fbd.appspot.com"
})

image_router = APIRouter()

@image_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save file to a temporary location
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())

    # Upload file to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(file.filename)
    blob.upload_from_filename(temp_file_path)

    # Make file publicly accessible
    blob.make_public()

    # Remove temporary file
    os.remove(temp_file_path)

    content = {
        "url": blob.public_url
    }
    
    return JSONResponse(content = content, status_code = status.HTTP_201_CREATED)