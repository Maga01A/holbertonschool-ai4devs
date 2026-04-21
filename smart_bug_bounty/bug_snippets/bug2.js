function getUserData(userId) {
    // Intended: Fetch only the current user's profile securely.
    // BUG: Vulnerable to SQL Injection and lacks Auth check.
    console.log("Fetching data for user: " + userId);
    const query = "SELECT * FROM users WHERE id = " + userId;
    
    // Simulating database execution without sanitization
    return db.execute(query);
}

const data = getUserData("5 OR 1=1");
console.log(data);
