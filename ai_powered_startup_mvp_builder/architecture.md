# System Architecture - Smart Task Prioritizer

## High-Level System Diagram
The application is designed as a standalone Client-Side Web Application to ensure privacy and low latency.

### Core Components:
1. **Frontend View**: Built with modern JavaScript/HTML/CSS. It handles the rendering of the Kanban board and user interaction events.
2. **Priority Calculation Engine**: A logic module that processes the 'Deadline' (Urgency) and 'Effort' (Complexity) data points to determine a priority score.
3. **Storage Layer (LocalStorage)**: A persistent browser-based database used to store tasks and user settings across sessions.
4. **Export Service**: A utility that parses the internal JSON state into a structured CSV format for data portability.
