from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        self._pricing = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }

        self._offers = {
            "A": [
                {"quantity": 5, "offer_price": 200},
                {"quantity": 3, "offer_price": 130}
            ],
            "B": [
                {"quantity": 2, "offer_price": 45}
            ]
        }

        self._free_item_offers = [
            {"q_item": "E", "q_quantity": 2, "free_item": "B", "free_quantity": 1}
        ]

        self._self_free_items = {
            "F": {"self_quantity": 3, "pay_for": 2}
        }

        for ch in skus:
            if ch not in self._pricing:
                return -1

        item_counts = Counter(skus)
        free_items = Counter()

        for offer in self._free_item_offers:
            q_item = offer["q_item"]
            q_quantity = offer["q_quantity"]
            free_item = offer["free_item"]
            free_quantity = offer["free_quantity"]

            if q_item in item_counts:
                num_qualifiers = item_counts[q_item] // q_quantity
                free_items[free_item] += num_qualifiers * free_quantity

   
        for item, rule in self._self_free_items.items():
            if item in item_counts:
                total_self_quantity = item_counts[item] // rule["self_quantity"]
                remaining = item_counts[item] % rule["self_quantity"]
                item_counts[item] = total_self_quantity * rule["pay_for"] + remaining

        total = 0
        for item, count in item_counts.items():
            free_count = min(count, free_items[item]) if item in free_items else 0
            payable_count = count - free_count

  
            if item in self._offers:
                offers = self._offers[item]
                for offer in offers:
                    num_offer = payable_count // offer["quantity"]
                    total += num_offer * offer["offer_price"]
                    payable_count = payable_count % offer["quantity"]
            total += payable_count * self._pricing[item]

        return total


