from fastapi import Header, HTTPException, status

VALID_API_KEY = {"3d58a556-efa1-4372-a79e-b1af55023d83"}


def verify_api_key(x_api_token: str = Header(...)):
    if x_api_token not in VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API Key",
        )
