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
    def __init__(self, products: List[Product]):
        self.products = {p.id: p for p in products}
    
    def calculate_similarity(self, p1_id, p2_id):
        p1, p2 = self.products[p1_id], self.products[p2_id]
        cat_score = 1.0 if p1.category == p2.category else 0.0
        return cat_score # Sad?l?sdirilmis versiya
