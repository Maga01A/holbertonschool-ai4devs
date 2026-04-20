# Prompt Testing Examples

## Example 1 – Color Palette Generation
**Prompt**: Create a comprehensive color palette for a sustainable ride-sharing application named 'EcoRide'. Focus on eco-friendly and high-tech vibes.  
**Input**: Brand values: Sustainability, Innovation, Trust, Urban Mobility.  
**AI Output**: 
- Primary: #10b981 (Emerald Green)
- Secondary: #3b82f6 (Electric Blue)
- Neutral: #f9fafb (Off-white), #1f2937 (Dark Slate)
- Semantic Success: #059669
- Semantic Error: #dc2626
**Feedback**: The color choices perfectly balance the 'green' aspect with a modern tech feel. Accessibility contrast for #10b981 on white needs to be verified.

## Example 2 – Typography Scale
**Prompt**: Generate a responsive typography system for a mobile-first project management dashboard.  
**Input**: Base font size: 16px, Scale: 1.25 (Major Third).  
**AI Output**:
- H1: 3.052rem (48.83px)
- H2: 2.441rem (39.06px)
- H3: 1.953rem (31.25px)
- Body: 1rem (16px)
- Small: 0.8rem (12.8px)
**Feedback**: Scaling is consistent. The H1 might be too large for small mobile screens (320px), suggesting a 1.2 scale for mobile.

## Example 3 – User Journey Mapping
**Prompt**: Design the complete user journey for 'Booking an Electric Vehicle ride' in EcoRide.  
**Input**: Goal: User needs to find and book an EV in under 4 taps.  
**AI Output**:
1. Discovery: App opens to map showing nearby EVs.
2. Selection: User taps destination bar and selects a saved 'Work' address.
3. Decision: AI suggests 'Greenest Route' with CO2 savings. User taps 'Book'.
4. Confirmation: Driver assigned, ETA displayed.
**Feedback**: The journey is efficient. Adding a 'One-tap Rebook' feature for routine trips could further optimize the UX.

## Example 4 – Accessibility Audit Prompt
**Prompt**: Conduct an accessibility audit for a 'Payment Success' screen with green text on a light gray background.  
**Input**: Text color: #059669, Background: #f3f4f6.  
**AI Output**:
- Contrast Ratio: 4.58:1.
- WCAG 2.1 Level AA: Pass.
- WCAG 2.1 Level AAA: Fail (Requires 7:1).
- Recommendation: Darken the green to #047857 for better readability.
**Feedback**: Very precise analysis. The recommendation provides a specific hex code which is helpful for designers.

## Example 5 – Component State Definition
**Prompt**: Define interactive states for a primary action button in a dark-themed UI.  
**Input**: Component: 'Confirm Booking' Button, Base Color: #2563eb.  
**AI Output**:
- Default: #2563eb (Blue)
- Hover: #3b82f6 (Lighten 10%)
- Active/Pressed: #1d4ed8 (Darken 10%)
- Disabled: #9ca3af (Gray)
- Focus: Outline 2px #60a5fa offset 2px.
**Feedback**: Excellent coverage of states. Focus state definition is crucial for keyboard navigation and meets accessibility standards.
