function fetchUserData(userId) {
    // This function fetches user info from DB.
    // WARNING: This is a legacy implementation.
    // ------------------------------------------
    console.log("Preparing to fetch data...");
    
    // SECURITY BUG: Direct string concatenation.
    // This allows SQL Injection attacks.
    let sqlQuery = "SELECT * FROM users WHERE id = " + userId;
    
    console.log("Executing: " + sqlQuery);
    
    // Simulating database execution
    let response = db.execute(sqlQuery);
    
    // Return result to the caller
    return response;
}

// Triggering the function
fetchUserData("101; DROP TABLE users;");
