# Cross-Language Specification - Recommendation Engine

## Algorithm
The algorithm calculates a recommendation score for items based on a weighted hybrid similarity. It considers three main factors:
1. **Category Match**: Exact match between user preference and item category (Weight: 0.4).
2. **Tag Overlap**: Jaccard similarity between user interest tags and item tags (Weight: 0.4).
3. **Price Score**: Normalized score based on the item's price relative to the user's budget (Weight: 0.2).

Score Formula:
`Score = (0.4 * CategoryMatch) + (0.4 * TagJaccard) + (0.2 * PriceScore)`

- `CategoryMatch`: 1 if `item.category == user.preferred_category` else 0.
- `TagJaccard`: `|user.interests ∩ item.tags| / |user.interests ∪ item.tags|` (ignoring empty or null tags).
- `PriceScore`: `1 - (item.price / user.max_budget)` if `item.price <= user.max_budget` else 0.

## Input Format
The input is a JSON object containing:
- `user_profile`: `{ "preferred_category": string, "interests": string[], "max_budget": number }`
- `items`: Array of `{ "id": string, "category": string, "tags": string[], "price": number }`

## Output Format
The output is a JSON array of item IDs (strings), sorted by their calculated recommendation score in descending order. If scores are equal, sort items alphabetically by `id`.

## Edge Cases
- **Empty Item List**: Returns an empty array `[]`.
- **Budget Zero / Exceeded**: Items with `price > max_budget` receive a `PriceScore` of 0.
- **No Overlapping Tags**: `TagJaccard` evaluates to 0; total score relies on category match and price score.
- **Malformed Tags**: Tags containing empty strings `""` or `null` values must be filtered out before Jaccard calculation.
- **Equal Scores**: Ties are broken deterministically by sorting item IDs in ascending alphabetical order.

## Test Cases

### Test Case 1: Perfect Match
**Input:**
```json
{
  "user_profile": {
    "preferred_category": "Tech",
    "interests": ["ai", "coding"],
    "max_budget": 100
  },
  "items": [
    {
      "id": "item1",
      "category": "Tech",
      "tags": ["ai", "coding"],
      "price": 0
    }
  ]
}
