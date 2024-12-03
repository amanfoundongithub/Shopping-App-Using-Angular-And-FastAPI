from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.user_router import user_router
from router.item_router import item_router
from router.image_router import image_router

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins 
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router, prefix = "/user", tags = ["user"])
app.include_router(item_router, prefix = "/item", tags = ["item"])
app.include_router(image_router, prefix="/image", tags = ["image"])
