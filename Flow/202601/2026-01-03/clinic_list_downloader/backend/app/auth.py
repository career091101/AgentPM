"""
認証システム
"""

from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

from .database import verify_user

security = HTTPBasic()

class LoginRequest(BaseModel):
    username: str
    password: str

class User(BaseModel):
    user_id: int
    username: str

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    """
    現在のユーザーを取得（ベーシック認証）

    Args:
        credentials: HTTPベーシック認証の資格情報

    Returns:
        User: 認証されたユーザー

    Raises:
        HTTPException: 認証失敗時
    """
    user_id = verify_user(credentials.username, credentials.password)

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return User(user_id=user_id, username=credentials.username)

def verify_credentials(username: str, password: str) -> Optional[User]:
    """
    認証情報を検証（ログインAPI用）

    Args:
        username: ユーザー名
        password: パスワード

    Returns:
        User: 認証成功時のユーザー情報、失敗時はNone
    """
    user_id = verify_user(username, password)

    if user_id is None:
        return None

    return User(user_id=user_id, username=username)
