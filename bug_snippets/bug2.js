function getUserData(userId) {
    // SECURITY BUG: Direct string concatenation leads to SQL Injection.
    // Also lacks authorization checks for the requesting user.
    const query = "SELECT * FROM users WHERE id = " + userId;
    console.log("Executing query for user...");
    
    // Simulating database call
    let result = db.execute(query);
    return result;
}

// Example of malicious input
getUserData("1; DROP TABLE users;");
