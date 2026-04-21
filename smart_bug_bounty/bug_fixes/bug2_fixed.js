// Fixed version using parameterized queries and authorization
function getUserData(userId, currentSessionUser) {
    if (userId !== currentSessionUser.id) {
        throw new Error("Unauthorized access attempt.");
    }
    
    // Using placeholder for parameterized query
    const query = "SELECT * FROM users WHERE id = ?";
    return db.execute(query, [userId]);
}
