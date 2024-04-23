from . import cust_info_router

def load_routes(app):
    app.include_router(cust_info_router.router)