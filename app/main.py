from fastapi import FastAPI,Path,HTTPException,Query
from services.products import get_all_products


app = FastAPI()

@app.get("/")
def root():
    return {"Message":"Welcome to FastAPI course"}


# @app.get("/products/{id}")
# def get_products(id: int):
#     products = ['Brush', 'Colgate', 'Soap', 'cake']

#     if id >= len(products):
#         raise HTTPException(status_code=404, detail="Product not found")

#     return products[id]



# @app.get("/products")
# def get_deail_info_about_products():
#     return get_all_products()

    # NOTE
    # Query = Used for Filtering Results we want
    # Path = Adding rules and protocols in parameter



@app.get("/products")
def list_products(
    name: str | None = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by Product Name(case insensitive)",
        examples="Iphone"
    ),
    sort_by_price:bool = Query(
        default=False,\
        description="Sort  Product by price"
    ),
    order:str = Query(
        default="asc",
        description="Sort Product by price in ASC or DESC order"
    ),
    limit:int = Query(
        default=5,
        ge=1,
        le=100,
        description="No of items to be searched"
    ),
    offset:int = Query(
        default=0,
        ge=0,
        description="Pagination offeset"
    )
):    
    products = get_all_products()
    
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name", "").lower()]
    
        if not products:
            raise HTTPException(
                status_code=404, detail=f"No products found matching name={name}")

    
    if sort_by_price:
        reverse = order == "desc"
        products = sorted(products, key=lambda p:p.get("price",0), reverse=reverse)

    total = len(products)
    products = products[offset: offset + limit]
    
    return {
        "total": total,
        "limit": limit,
        "items" : products
    }


@app.get("/products/{product_id}")
def get_products_by_ID(product_id: str= Path(..., min_length= 36,max_length=36,description="UUID of the Product",examples="0005a4da-ce3f-4dd7-bde0-f4ddc70fea6a")):
    products = get_all_products()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")    

    return products[id]
