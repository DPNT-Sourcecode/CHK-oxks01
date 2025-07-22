
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        self._pricing = {"A": 50, "B": 30, "C": 20, "D": 15}
        self._offers = {
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
            if item in self._offers:
                offer = self._offers[item]
                num_offers = count // offer["quantity"]
                remainder = count % offer["quantity"]
                total += num_offers * offer["offer_price"] + remainder * self._pricing[item]
            else:
                total += count * self._pricing[item]

        return total





