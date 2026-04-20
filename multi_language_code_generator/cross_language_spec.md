# Cross-Language Specification - Recommendation Engine

## Algorithm
The engine generates product recommendations using a weighted hybrid similarity score based on category match, tag similarity (Jaccard Index), and price proximity.

## Inputs
1. **Product Database**: A list of objects containing `id`, `name`, `category`, `price`, `rating`, and `tags` (List of Strings).
2. **User Behavior**: An object containing `product_views` (IDs), `purchases` (IDs), and `ratings` (Map/Dict {ID: Value}).
3. **Threshold**: A float (default 0.3) representing the minimum similarity to consider a product.

## Outputs
- A sorted list of recommended `Product` objects with their associated `Score` (Float), excluding products already purchased by the user.

## Calculation Rules
1. **Category Score (50%)**: 1.0 if categories match exactly, 0.0 otherwise.
2. **Tag Score (30%)**: Calculated using the Jaccard Index: `(Intersection of tags) / (Union of tags)`.
3. **Price Score (20%)**: `1.0 - (|price1 - price2| / max(price1, price2))`.

## Edge Cases
- **Empty Product List**: Should return an empty recommendation list.
- **No Views/Ratings**: Should return an empty list as there is no user context.
- **Zero Price**: Handle division by zero when calculating price similarity.
- **Identical Products**: Similarity score should be exactly 1.0.

## Test Cases
1. **Base Case**: User viewed `Electronics` (ID: 1). Database has `Electronics` (ID: 2) with 50% tag overlap. Expected similarity ~0.65.
2. **Already Purchased**: If ID: 2 is in `purchases`, it must be excluded regardless of score.
3. **Low Similarity**: Product with score 0.1 should be filtered out if threshold is 0.3.
4. **Empty Tags**: Jaccard index should return 0.0 without crashing.
5. **Full Boost**: High rating (5.0) on a category should boost other products in that category.