# EcoRide Microservices Architecture Description

In this architecture, the monolithic application is decomposed into independent, decoupled services that communicate via an API Gateway and asynchronous events.

### Service Descriptions:

* **API Gateway**: The single entry point for all clients. It handles request routing, load balancing, and rate limiting.
* **Auth & User Service**: Manages user profiles, authentication, and authorization. It has its own dedicated database for security.
* **Ride Matching Service**: Contains the core logic to pair riders with drivers based on eco-preferences and location.
* **Live Tracking Service**: Optimized for high-frequency GPS updates. Uses a geo-spatial database to handle real-time location data.
* **Sustainability Analytics Service**: Asynchronously processes trip data to calculate carbon savings and update environmental impact metrics.
* **Payment & Rewards Service**: Manages financial transactions and the eco-points loyalty system, ensuring data consistency for payments.
* **Notification Service**: A shared service that sends push notifications, emails, and SMS based on events triggered by other services.
* **Database per Service**: Each microservice manages its own data store to ensure loose coupling and independent scalability.
