# Reflection: API Prototyping with AI

## Introduction
The integration of Artificial Intelligence into the API prototyping process represents a paradigm shift in how developers transition from abstract ideas to functional backend systems. In this project, which focused on the "RentFlow" rental equipment API, AI acted as both an architect and a quality assurance engineer.

## Where AI Helped Most
AI was most effective during the initial scaffolding phase. Defining the five core CRUD (Create, Read, Update, Delete) operations in Express.js was near-instantaneous. By providing a simple description of the business logic, AI generated a syntactically correct structure that would have otherwise required manual boilerplate writing. 

Furthermore, AI's role in "cross-discipline" tasks was invaluable. Creating a Postman collection JSON manually is often tedious and prone to formatting errors; however, AI was able to transform endpoint descriptions into a valid schema effortlessly. It also excelled at identifying edge cases—such as pagination needs and data validation—that are often overlooked during the high-speed prototyping phase.

## Where Manual Adjustments Were Needed
Despite the efficiency of AI, manual intervention was crucial in two specific areas: environment-specific configuration and logical consistency. 
1. **Directory and Path Management**: AI often struggled with the specific folder structures required by the project's checker (e.g., whether a README should be in /src or the root). Manual pathing in PowerShell was necessary to ensure the repository met the exact submission standards.
2. **Business Context**: While AI could write a generic PUT request, it did not automatically understand the specific business rules of the Azerbaijan market (e.g., local currency formatting or specific ID structures used in local rental businesses). These nuances required human oversight to ensure the prototype remained practical for its intended market.

## Lessons for Future Workflows
Future API prototyping workflows should leverage AI for "rapid-fail" iterations—quickly building a prototype to test an idea's feasibility before investing in manual code. A key lesson learned is the importance of **Structured Prompting**; using a prompt patterns library significantly improves the quality of the generated code compared to vague requests. 

In conclusion, AI is not a replacement for a developer but a force multiplier. It handles the repetitive "how-to-code" aspects, allowing the developer to focus on the "what-to-build" and "why-it-matters" from a business perspective.
