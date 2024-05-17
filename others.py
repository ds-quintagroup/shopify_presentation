import shopify

# Код для отримання списку колекцій
def get_collections():
    collections = shopify.CustomCollection.find()
    return collections

# Приклад виклику функції
collections = get_collections()
for collection in collections:
    print(collection.title)

# Код для додавання тегів до товару
def add_tags_to_product(product_id, tags):
    product = shopify.Product.find(product_id)
    product.tags = tags
    if product.save():
        print("Tags added successfully")
    else:
        print("Failed to add tags")

# Приклад виклику функції
add_tags_to_product(product_id="123456", tags="auction, exclusive")

# Код для фільтрації товарів за ціною:

def filter_products_by_price(min_price, max_price):
    products = shopify.Product.find(price_min=min_price, price_max=max_price)
    return products

# Приклад виклику функції
products = filter_products_by_price(min_price=50, max_price=200)
for product in products:
    print(product.title, product.variants[0].price)

# Код для сортування замовлень
def get_recent_orders():
    orders = shopify.Order.find(order="created_at DESC")
    return orders

# Приклад виклику функції
orders = get_recent_orders()
for order in orders:
    print(order.name, order.created_at)

# Код для створення знижки:
def create_discount(code, value_type, value):
    discount = shopify.PriceRule({
        "title": code,
        "value_type": value_type,
        "value": -value,
        "customer_selection": "all",
        "target_type": "line_item",
        "target_selection": "all",
        "allocation_method": "across",
        "starts_at": "2023-01-01T00:00:00Z"
    })
    if discount.save():
        print("Discount created successfully")
    else:
        print("Failed to create discount")

# Приклад виклику функції
create_discount(code="DISCOUNT10", value_type="fixed_amount", value=10)

# обробка метаполів
def add_metafield_to_product(product_id, namespace, key, value, value_type):
    product = shopify.Product.find(product_id)
    metafield = shopify.Metafield({
        "namespace": namespace,
        "key": key,
        "value": value,
        "value_type": value_type
    })
    product.add_metafield(metafield)
    if product.save():
        print("Metafield added successfully")
    else:
        print("Failed to add metafield")

# Приклад виклику функції
add_metafield_to_product(product_id="123456", namespace="custom", key="auction_winner", value="John Doe", value_type="string")
