# Data Model - Smart Task Prioritizer

## Entity 1: Task
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for the task. |
| title | String | Name of the task. |
| deadline | Date | Due date for the task. |
| effort | Integer | Difficulty rating (1 to 5). |
| priorityScore | Float | Value calculated by the prioritization engine. |
| status | Enum | Current state: 'todo', 'doing', 'done'. |

## Entity 2: Category
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for the category. |
| name | String | Display name (e.g., Work, Life, Urgent). |
| colorCode | String | Hex code for UI representation. |

## Entity 3: UserSettings
| Attribute | Type | Description |
| :--- | :--- | :--- |
| id | UUID | Unique identifier for user preferences. |
| themeMode | String | 'light' or 'dark' UI theme selection. |
| taskLimit | Integer | User-defined maximum of active tasks allowed. |
