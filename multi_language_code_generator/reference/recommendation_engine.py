from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class Product:
    id: str
    name: str
    category: str
    price: float
    tags: List[str]

class RecommendationEngine:
    def __init__(self, products: List[Product], threshold: float = 0.3):
        self.products = {p.id: p for p in products}
        self.threshold = threshold

    def calculate_similarity(self, p1_id: str, p2_id: str) -> float:
        if p1_id not in self.products or p2_id not in self.products:
            return 0.0
        p1, p2 = self.products[p1_id], self.products[p2_id]
        
        # Category (50%)
        cat_score = 1.0 if p1.category == p2.category else 0.0
        
        # Tags (30%) - Jaccard
        s1, s2 = set(p1.tags), set(p2.tags)
        tag_score = len(s1 & s2) / len(s1 | s2) if s1 | s2 else 0.0
        
        # Price (20%)
        max_p = max(p1.price, p2.price)
        price_score = 1.0 - (abs(p1.price - p2.price) / max_p) if max_p > 0 else 1.0
        
        return (0.5 * cat_score) + (0.3 * tag_score) + (0.2 * price_score)

    def get_recommendations(self, views: List[str], purchases: List[str]) -> List[Tuple[str, float]]:
        scores = {}
        purchased_set = set(purchases)
        for v_id in views:
            if v_id not in self.products: continue
            for p_id in self.products:
                if p_id in purchased_set or p_id == v_id: continue
                sim = self.calculate_similarity(v_id, p_id)
                if sim >= self.threshold:
                    scores[p_id] = max(scores.get(p_id, 0), sim)
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
