# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse, Response
# from fastapi.middleware.cors import CORSMiddleware
# from app import routes
# import app.auth as auth

# app = FastAPI(title="Ecommerce API ")

# # CORS Configuration
# origins = [
#      "http://localhost:5173",   #  React dev server
#      "http://127.0.0.1:5173",   # sometimes React runs on 127.0.0.1
#      "https://2822a62f46d8.ngrok-free.app",
    
    
# ],

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],       # Allowed domains
#     allow_credentials=True,      # Allow cookies/auth headers
#     allow_methods=["*"],         # Allow all HTTP methods
#     allow_headers=["*"],         # Allow all headers
# )


# # Router include karna
# app.include_router(routes.app)


# # JWT middleware
# @app.middleware("http")
# async def jwt_middleware(request: Request, call_next):

#     public_paths = [
#         "/api/login",
#         "/api/signup",
#         "/login",
#         "/signup", 
#         "/docs", 
#         "/openapi.json", 
#         "/forgot-password",
#         "/reset-password",
#         "/",
#         "/redoc"
        
#         ]
    
#     # Always allow preflight (OPTIONS) requests
#     if request.method == "OPTIONS":
#         return await call_next(request)
    
#     # Get the current request path 
#     path = request.url.path 
    
#     # Allow request if path matches or starts with any public route (token check skip)
#     if any(path == p or path.startswith(p + "/") for p in public_paths):
#         return await call_next(request)
    
    

#     auth_header = request.headers.get("authorization") 
#     if not auth_header or not auth_header.lower().startswith("bearer "):
#         return JSONResponse(status_code=401, content={"detail": "Missing or invalid token"})
    
#     # Token print in terminal
#     #print("Token:", auth_header) 

#     token = auth_header.split(" ", 1)[1].strip()
#     try:
#         payload = auth.decode_access_token(token)
#         request.state.user = payload
        
#         # For User data from token print in Terminal
#        # print(" User Data from Token:", payload)  

#     except Exception as e:
#         # Check token in terminal
#         print(" Token decode error:", str(e)) 
#         return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

#     return await call_next(request)


#-----------------------

from fastapi import FastAPI

from app.api.routes import (
    auth_routes,
    product_routes,
    cart_routes,
    order_routes,
    profile_routes
)

app = FastAPI(title="Ecommerce API")


app.include_router(auth_routes.router)
app.include_router(product_routes.router)
app.include_router(cart_routes.router)
app.include_router(order_routes.router)
app.include_router(profile_routes.router)


@app.get("/")
def home():
    return {"msg": "Welcome to Ecommerce API"}

