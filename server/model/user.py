from pydantic import BaseModel

# Base class contains only username
class UserBase(BaseModel):
    # 
    username : str 

# Authentication class 
class UserAuthenticate(UserBase):
    # 
    password : str 

# Account creation class
class UserCreate(UserAuthenticate):
    type : str 
    # Name
    firstName : str 
    lastName : str 
    
    # 
    dob : str 
    # 
    gender : str 
    
    profilePic : str = "https://www.tenforums.com/geek/gars/images/2/types/thumb_15951118880user.png"

# Account update class 
class UserUpdate(UserBase):
    # Name
    firstName : str 
    lastName : str 
    
    # 
    dob : str 
    # 
    gender : str 
    
    profilePic : str = "https://www.tenforums.com/geek/gars/images/2/types/thumb_15951118880user.png"
    