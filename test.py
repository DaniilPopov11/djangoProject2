def what_to_buy(item, *args, **kwargs):
    if 'store' in kwargs:
        return f"Buy {item} in {kwargs['store']}"
    else:
        return f"Buy {item} in any store"
    return item

what_to_buy('Laptop',store="Best Buy")