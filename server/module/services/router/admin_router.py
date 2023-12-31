from fastapi import APIRouter, Depends

from auth.api_key_type_authorization_provider import ApiKeyTypeAuthorizationProvider
from auth.auth_provider import AuthProvider
from auth.role_authorization_provider import RoleAuthorizationProvider
from exception.http_error import HttpErrorResponse
from schema.auth.common import ApiKeyType, RoleType
from schema.auth.response import GetAllApiKeysDetailsResponse
from schema.services.request import (
    ModelCreateRequest,
    ModelUpdateRequest,
    ServiceCreateRequest,
    ServiceHeartbeatRequest,
    ServiceUpdateRequest,
)
from schema.services.request.admin_dashboard import ViewAdminDashboardRequest

from ..service import AdminService

router = APIRouter(
    prefix="/admin",
    dependencies=[
        Depends(AuthProvider),
        Depends(RoleAuthorizationProvider([RoleType.ADMIN])),
        Depends(ApiKeyTypeAuthorizationProvider(ApiKeyType.INFERENCE)),
    ],
    responses={
        "401": {"model": HttpErrorResponse},
        "403": {"model": HttpErrorResponse},
    },
)


@router.get("/dashboard")
async def _view_admin_dashboard(
    request: ViewAdminDashboardRequest = Depends(),
    admin_service: AdminService = Depends(AdminService),
) -> GetAllApiKeysDetailsResponse:
    return admin_service.view_dashboard(
        request.page, request.limit, request.target_user_id
    )
    
     # Create a FastAPI Response instance and set cache prevention headers
    #no_cache_response = Response(content=response.json())
    no_cache_response = Response(content=response.model_dump_json())
    no_cache_response.headers["Cache-Control"] = "no-store, must-revalidate"
    no_cache_response.headers["Pragma"] = "no-cache"

    return no_cache_response


@router.post("/create/service")
async def _create_service(
    request: ServiceCreateRequest, admin_service: AdminService = Depends(AdminService)
):
    return admin_service.create_service(request)

# Create a FastAPI Response instance and set cache prevention headers
    
    no_cache_response = Response(content=response.model_dump_json())
    no_cache_response.headers["Cache-Control"] = "no-store, must-revalidate"
    no_cache_response.headers["Pragma"] = "no-cache"

    return no_cache_response


@router.post("/create/model")
async def _create_model(
    request: ModelCreateRequest, admin_service: AdminService = Depends(AdminService)
):
    return admin_service.create_model(request)

# Create a FastAPI Response instance and set cache prevention headers
    
    no_cache_response = Response(content=response.model_dump_json())
    no_cache_response.headers["Cache-Control"] = "no-store, must-revalidate"
    no_cache_response.headers["Pragma"] = "no-cache"

    return no_cache_response


@router.patch("/update/service")
async def _update_service(
    request: ServiceUpdateRequest, admin_service: AdminService = Depends(AdminService)
):
    return admin_service.update_service(request)

# Create a FastAPI Response instance and set cache prevention headers
    
    no_cache_response = Response(content=response.model_dump_json())
    no_cache_response.headers["Cache-Control"] = "no-store, must-revalidate"
    no_cache_response.headers["Pragma"] = "no-cache"

    return no_cache_response


@router.patch("/update/model")
async def _update_model(
    request: ModelUpdateRequest, admin_service: AdminService = Depends(AdminService)
):
    return admin_service.update_model(request)


@router.delete("/delete/service")
async def _delete_service(id: str, admin_service: AdminService = Depends(AdminService)):
    return admin_service.delete_service(id)


@router.delete("/delete/model")
async def _delete_model(id: str, admin_service: AdminService = Depends(AdminService)):
    return admin_service.delete_model(id)


@router.patch("/health")
def _update_service_health(
    request: ServiceHeartbeatRequest,
    admin_service: AdminService = Depends(AdminService),
):
    return admin_service.inference_service_status(request)
