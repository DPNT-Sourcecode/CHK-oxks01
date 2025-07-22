from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        self._pricing = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, 
            "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
            "K": 70, "L": 90, "M": 15, "N": 40, "O": 10,
            "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20,
            "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21
        }

        self._offers = {
            "A": [
                {"quantity": 5, "offer_price": 200},
                {"quantity": 3, "offer_price": 130}
            ],
            "B": [
                {"quantity": 2, "offer_price": 45}
            ],
            "H": [
                 {"quantity": 10, "offer_price": 80},
                {"quantity": 5, "offer_price": 45},
            ],
            "K": [
                {"quantity": 2, "offer_price": 150}
            ],
            "P": [
                {"quantity": 5, "offer_price": 200}
            ],
            "Q": [
                {"quantity": 3, "offer_price": 80}
            ],
            "V": [
                {"quantity": 3, "offer_price": 130},
                {"quantity": 2, "offer_price": 90}
            ],
        }

        self._free_item_offers = [
            {"q_item": "E", "q_quantity": 2, "free_item": "B", "free_quantity": 1},
            {"q_item": "N", "q_quantity": 3, "free_item": "M", "free_quantity": 1},
            {"q_item": "R", "q_quantity": 3, "free_item": "Q", "free_quantity": 1},
        ]

        self._self_free_items = {
            "F": {"self_quantity": 3, "pay_for": 2},
            "U": {"self_quantity": 4, "pay_for": 3}
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

        group_items = ["S", "T", "X", "Y", "Z"]
        group_pool = []
        for item in group_items:
            group_pool+= [item] * item_counts[item]
            item_counts[item] = 0

        group_pool.sort(key=lambda i: self._pricing[i], reverse=True)

        total = 0
        while len(group_pool) >= 3:
            total += 45
            for _ in range(3):
                group_pool.pop(0)
        for item in group_pool:
            item_counts[item] += 1

        for item, count in item_counts.items():
            free_count = min(count, free_items[item]) if item in free_items else 0
            payable_count = count - free_count

  
            if item in self._offers:
                offers = sorted(self._offers[item], key=lambda o: -o["quantity"])
                for offer in offers:
                    num_offer = payable_count // offer["quantity"]
                    total += num_offer * offer["offer_price"]
                    payable_count = payable_count % offer["quantity"]
            total += payable_count * self._pricing[item]

        return total


