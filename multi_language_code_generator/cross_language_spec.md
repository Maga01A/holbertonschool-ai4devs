# Cross-Language Specification - Recommendation Engine

## Algorithm
The algorithm calculates a recommendation score for items based on a weighted hybrid similarity. It considers three main factors:
1. **Category Match**: Exact match between user preference and item category.
2. **Tag Overlap**: Jaccard similarity between user interest tags and item tags.
3. **Price Score**: Normalized score based on the item's price relative to the user's budget.

## Input Format
The input is a JSON object containing:
- `user_profile`: { `preferred_category`: string, `interests`: string[], `max_budget`: number }
- `items`: Array of { `id`: string, `category`: string, `tags`: string[], `price`: number }

## Output Format
The output is a JSON array of item IDs, sorted by their calculated recommendation score in descending order.

## Edge Cases
- **Empty Item List**: Should return an empty array.
- **Budget Zero**: Items with price > 0 should receive a score of 0 or be excluded.
- **No Overlapping Tags**: Score should rely solely on category and price.
- **Malformed Tags**: Tags with empty strings or null values should be ignored.
- **Equal Scores**: If scores are identical, items should be sorted alphabetically by ID.

## Test Cases
1. **Perfect Match**: User likes "Tech" and item is "Tech" with 100% tag overlap and fits budget -> Score: 1.0.
2. **Empty Input**: `items: []` -> Output: `[]`.
3. **Budget Exclusion**: Item price is 2x `max_budget` -> Item should appear at the end of the list or have lowest score.
4. **No Category Match**: User likes "Books", item is "Fashion", but has overlapping tags -> Should return score > 0 but < "Tech" match.
5. **Diverse Catalog**: 10 items with varying prices and tags -> Should return a list of 10 IDs correctly sorted by weight.
