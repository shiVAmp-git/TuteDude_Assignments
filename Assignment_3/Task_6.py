def process_prices(prices):
    discount = lambda prices:prices - prices/10
    discounted_prices = list(map(lambda prices:prices * 0.9,prices))
    filtered_prices = list(filter( lambda prices:prices > 300,discounted_prices))
    print(f"Original Price List: {prices}")
    print(f"Discounted Price List: {discounted_prices}")
    print(f"Filtered Price List: {filtered_prices}")          
process_prices([100,500,900,50,750])