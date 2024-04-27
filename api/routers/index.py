from . import cust_info_router
from . import cust_login_router
from . import resource_router

def load_routes(app):
    app.include_router(cust_info_router.router)
    app.include_router(cust_login_router.router)
    app.include_router(resource_router.router)