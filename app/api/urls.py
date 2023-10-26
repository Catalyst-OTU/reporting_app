from fastapi import APIRouter
from fastapi import Depends
from router.main import report_app
from router.auth import auth_router
from security.rbac import check_if_is_admin









router = APIRouter()
router.include_router(auth_router)
router.include_router(report_app, dependencies=[Depends(check_if_is_admin)])


