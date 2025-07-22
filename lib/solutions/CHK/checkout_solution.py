
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        our_pricing = {"A": 50, "B": 30, "C": 20, "D": 15}
        our_offers = {
            "A": {"quantity" : 3, "offer_price": 130},
            "B": {"quantity" : 2, "offer_price": 45}
        }
        for i in skus:
            if i not in our_pricing:
                return -1
            
        from collections import Counter
        item_counts = Counter(skus)

        total = 0
        for item, count in item_counts.items():
            for item in our_offers:
                offer = our_offers[item]
                num_offers = count // our_offers["quantity"]
                remainder = count % our_offers["quantity"]
                total += num_offers * our_offers["price"] + remainder + our_pricing["item"]
            else:
                total += count * our_pricing["item"]

        return total




