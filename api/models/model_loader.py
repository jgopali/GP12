from . import orders, customers, ratings_review, payment_info, resource_management,menu_items,promotions,staff_login,staff_info,cust_login,cust_info

from ..dependencies.database import engine

#Creating tables
def index():
    orders.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    ratings_review.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    staff_login.Base.metadata.create_all(engine)
    staff_info.Base.metadata.create_all(engine)
    cust_login.Base.metadata.create_all(engine)
    cust_info.Base.metadata.create_all(engine)