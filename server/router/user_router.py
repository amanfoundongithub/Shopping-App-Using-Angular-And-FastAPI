from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from model.user import UserAuthenticate, UserCreate, UserUpdate 

from db.user import createUser, fetchUser, updateUser, authenticateUser

from utils.error import create_error_response

user_router = APIRouter()

# ------------------------ AUTHENTICATE ----------------------------------
@user_router.post("/authenticate")
async def login_user_route(user : UserAuthenticate):
    try: 
        verification, id = authenticateUser(user) 
        content = {
            "verified" : verification,
            "id" : id
        }
        return JSONResponse(content = content, status_code = status.HTTP_200_OK)
    except Exception as e:
        return create_error_response(e) 
        
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
@user_router.post("/create")
async def create_user_route(user : UserCreate):
    try:
        id = createUser(user)
        content = {
            "user" : id
        }
        return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)
    
    except Exception as e:
        return create_error_response(e) 
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
@user_router.get("/fetch/{user_id}")
async def fetch_user_route(user_id : str):
    try: 
        user = fetchUser(user_id)
        content = {
            "user" : user 
        }
        return JSONResponse(content=content, status_code=status.HTTP_200_OK)
        
    except Exception as e:
        return create_error_response(e) 
# ------------------------------------------------------------------------
        

# ------------------------------------------------------------------------
@user_router.put("/update/{user_id}")
async def update_user_route(user_id : str, user : UserUpdate):
    try: 
        user = updateUser(user_id, user) 
        content = {
            "updated" : "OK"  
        }
        return JSONResponse(content=content, status_code=status.HTTP_200_OK)
        
    except Exception as e:
        return create_error_response(e) 
# ------------------------------------------------------------------------
        