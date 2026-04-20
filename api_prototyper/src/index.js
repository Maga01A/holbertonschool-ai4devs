const express = require('express');
const app = express();
app.use(express.json());

let items = [
    { id: 1, name: "Drill", category: "Tools", pricePerDay: 15 },
    { id: 2, name: "Projector", category: "Electronics", pricePerDay: 25 }
];

// 1. READ ALL
app.get('/items', (req, res) => res.json(items));

// 2. READ ONE
app.get('/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    item ? res.json(item) : res.status(404).send('Item not found');
});

// 3. CREATE
app.post('/items', (req, res) => {
    const newItem = { id: items.length + 1, ...req.body };
    items.push(newItem);
    res.status(201).json(newItem);
});

// 4. UPDATE
app.put('/items/:id', (req, res) => {
    const index = items.findIndex(i => i.id === parseInt(req.params.id));
    if (index === -1) return res.status(404).send('Item not found');
    items[index] = { ...items[index], ...req.body };
    res.json(items[index]);
});

// 5. DELETE
app.delete('/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => console.log('RentFlow API running on http://localhost:' + PORT));
