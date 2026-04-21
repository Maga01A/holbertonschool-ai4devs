# AI Development Log - EcoRide MVP

## Prompt 1
"Generate a Node.js Express endpoint for /api/calculate-impact that takes distance and vehicleType, calculates carbon savings relative to a standard car, and returns CO2 in kg and eco-points."

## AI Output
A functional Express POST route with logic for different vehicle emission factors (EV, Hybrid, Standard).

## Action
? **Applied**. The logic was sound and easy to integrate. I added a 400 error check for missing parameters.

---

## Prompt 2
"Create a React component for a sustainability dashboard that allows users to input a trip distance and see their carbon impact visualization."

## AI Output
A React functional component with state management and basic inline styling.

## Action
? **Applied**. Minimal edits were made to the styling to match the "Emerald Green" eco-theme established in the design phase.

---

## Prompt 3
"Write a unit test for the carbon calculation logic."

## AI Output
Suggested a Jest/Mocha test suite to verify math accuracy.

## Action
? **Applied**. Created the test file to ensure the calculation logic remains robust.
