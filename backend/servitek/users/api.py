from ninja import Router, Schema
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth.models import User

router = Router()
User = get_user_model()

class RegisterSchema(Schema):
    username: str
    password: str
    email: str

class LoginSchema(Schema):
    username: str
    password: str

@router.post("/register")
def register(request, payload: RegisterSchema):
    if User.objects.filter(username=payload.username).exists():
        return {"error": "this username is already taken"}
    
    user = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password
    )

    return {"id": user.id, "username": user.username}

@router.post("/login")
def login(request, payload: LoginSchema):
    user = authenticate(request, username=payload.username, password=payload.password)
    
    if user is None:
        return {"error": "invalid credentials"}
    
    login(request, user)

    return {"id": user.id, "username": user.username}

@router.post("/logout")
def logout_user(request):
    logout(request)
    return {"message": "logged out"}

@router.get("/me")
def me(request):
    user = request.user
    return {"id": user.id, "username": user.username}