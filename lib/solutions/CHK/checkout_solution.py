
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        self._pricing = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        self._offers = {
            "A": {"quantity" : 3, "offer_price": 130},
            "B": {"quantity" : 2, "offer_price": 45}
        }

        self._free_items = {
            "q_item": "E", "q_quantity": 2, "free_item": "B", "free_quantity": 1
        }

        for i in skus:
            if i not in self._pricing:
                return -1
            
        from collections import Counter
        item_counts = Counter(skus)

        for offer in self._free_items:
            q_item = offer["q_item"]
            q_quantity = offer["q_quantity"]
            free_item = offer["free_item"]
            free_quantity = offer["free_quantity"]

            if q_item in item_counts:
                num_qualifiers = item_counts["q_items"] // q_quantity
                num_free = num_qualifiers * free_quantity
                if free_item in item_counts:
                    item_counts = max(0, item_counts[free_item] - num_free)

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






