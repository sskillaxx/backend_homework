from fastapi import APIRouter, Depends, HTTPException, status

from core.auth import get_auth_service, get_current_user
from schemas import LoginUser, RegisterUser, TokenResponse, UserResponse
from services import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: RegisterUser, service: AuthService = Depends(get_auth_service)):
    user = service.register(user_data)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="user already exists",
        )

    return user


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(credentials: LoginUser, service: AuthService = Depends(get_auth_service)):
    access_token = service.login(credentials)
    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
        )

    return TokenResponse(access_token=access_token)


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_me(current_user=Depends(get_current_user)):
    return current_user
