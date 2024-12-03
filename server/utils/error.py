from fastapi.responses import JSONResponse
from fastapi import status


def create_error_response(message : any) -> JSONResponse:
    # Body 
    content = {
        "error": str(message)
    } 
    return JSONResponse(content = content, status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

