from . import (cust_info_router, cust_login_router, resource_router, menuItems_router, order_details_router, orders_router,
               promotions_router, rating_routers, staff_info_routers, staff_login_router,recipes_router,payment_info_router)

def load_routes(app):
    app.include_router(cust_info_router.router)
    app.include_router(cust_login_router.router)
    app.include_router(resource_router.router)
    app.include_router(menuItems_router.router)
    app.include_router(order_details_router.router)
    app.include_router(orders_router.router)
    app.include_router(promotions_router.router)
    app.include_router(rating_routers.router)
    app.include_router(staff_info_routers.router)
    app.include_router(staff_login_router.router)
    app.include_router(recipes_router.router)
    app.include_router(payment_info_router.router)