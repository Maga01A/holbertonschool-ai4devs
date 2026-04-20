function camelToSnake(obj) {
    const newObj = {};
    for (let key in obj) {
        const snakeKey = key.replace(/[A-Z]/g, letter => _);
        newObj[snakeKey] = obj[key];
    }
    return newObj;
}
