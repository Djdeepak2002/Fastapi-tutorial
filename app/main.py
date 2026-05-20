from fastapi import FastAPI,Path,HTTPException,Query
from services.products import get_all_products,add_product,remove_product,change_product
from schema.products import Product,ProductUpdate
from uuid import uuid4, UUID
from datetime import datetime




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
def get_products_by_ID(
    product_id: str= Path(..., 
    min_length= 36,
    max_length=36,
    description="UUID of the Product",examples="0005a4da-ce3f-4dd7-bde0-f4ddc70fea6a")):
    products = get_all_products()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")    

    return products[id]



# ==========POST METHOD ==============
@app.post("/products",status_code=201)
def create_product(product:Product):
 
    # return product.json

    # saving product in dictionary of json
    product_dict = product.model_dump(mode="json")
    product_dict["id"] = str(uuid4())
    product_dict["created_at"] = datetime.utcnow().isoformat() + "z"

    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return product.model_dump(mode="json")


# ========== DELETE METHOD =================
@app.delete("/products/{product_id}")
def delete_product(
    product_id: UUID = Path(...,description="Product ID")):
    
    try:
        response = remove_product(str(product_id))
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return product.model_dump(mode="json")



# ========== UPDATE [PUT] METHOD =================
# Here we are using Custom payload model (ProductUpdate)

@app.put("/products/{product_id}")
def update_product(
    product_id: UUID = Path(...,description="Product UUID"),
    payload :ProductUpdate = ...):
    
    try:
        update_product = change_product(
        str(product_id),
        payload.model_dump(mode="json",exclude_unset=True))
        return update_product
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))