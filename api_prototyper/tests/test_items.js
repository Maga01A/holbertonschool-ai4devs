const request = require('supertest');
const express = require('express');
// API logic (mocked for testing)
const app = express();
app.use(express.json());
let items = [{ id: 1, name: "Drill", price: 15 }];
app.get('/items', (req, res) => res.json(items));
app.post('/items', (req, res) => res.status(201).json(req.body));

describe('RentFlow API Integration Tests', () => {
  it('should return all items', async () => {
    const res = await request(app).get('/items');
    expect(res.statusCode).toEqual(200);
    expect(res.body.length).toBeGreaterThan(0);
  });

  it('should add a new item', async () => {
    const res = await request(app).post('/items').send({ name: "Saw", price: 10 });
    expect(res.statusCode).toEqual(201);
  });
});
