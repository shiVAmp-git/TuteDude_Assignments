def process_prices(prices):
    discount = lambda price:price - price/10
    print(discount(prices))
    for price in prices:
        if price<300:
            pass
        else:
            prices.remove(price)
    print(prices)        