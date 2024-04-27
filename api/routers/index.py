from . import (cust_info_router, cust_login_router, resource_router, menuItems_router, order_details_router, orders_router,
               promotions_router)

def load_routes(app):
    app.include_router(cust_info_router.router)
    app.include_router(cust_login_router.router)
    app.include_router(resource_router.router)
    app.include_router(menuItems_router.router)
    app.include_router(order_details_router.router)
    app.include_router(orders_router.router)
    app.include_router(promotions_router.router)