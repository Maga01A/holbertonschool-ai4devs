# System Architecture - Smart Task Prioritizer

## High-Level System Diagram
The application follows a client-side architecture optimized for speed and privacy.



### Components:
1. **Frontend Layer (UI)**: Built with HTML5, CSS3, and JavaScript. Handles user input and visualizes the Kanban board.
2. **Priority Engine**: A core JavaScript module that takes 'Deadline' and 'Effort' as inputs and applies a weighted algorithm to calculate a Priority Score.
3. **Data Storage (LocalStorage)**: Browser-based persistent storage to keep user data secure and available offline.
4. **Export Module**: Converts JSON task data into a downloadable CSV format.
