# Data Model - Smart Task Prioritizer

## Entity 1: Task
Represents the core unit of work in the system.
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for the task. |
| title | String | Name of the task. |
| deadline | Date | Due date for the task. |
| effort | Integer | Estimated effort from 1 (low) to 5 (high). |
| priorityScore | Float | Calculated value used for ranking. |
| status | Enum | Current state: 'todo', 'doing', 'done'. |

## Entity 2: Category
Used to group tasks for better organization.
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for the category. |
| name | String | Name (e.g., Work, School, Health). |
| colorCode | String | Hex color for UI representation. |

## Entity 3: UserSettings
Stores personal preferences for the application.
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for settings. |
| themeMode | String | 'light' or 'dark'. |
| defaultCategory | UUID | ID of the category assigned to new tasks by default. |
