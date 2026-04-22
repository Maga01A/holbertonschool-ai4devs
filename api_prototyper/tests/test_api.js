const request = require('supertest');
const express = require('express');
const app = express();
app.use(express.json());

// Mock Data
let users = [{ id: "1", username: "eco_rider" }];
let items = [{ id: "1", name: "Electric Drill", price: 20 }];

// Routes for Users
app.get('/users', (req, res) => res.status(200).json(users));
app.post('/users', (req, res) => res.status(201).json(req.body));
app.get('/users/:id', (req, res) => res.status(200).json(users[0]));
app.put('/users/:id', (req, res) => res.status(200).json({ updated: true }));
app.delete('/users/:id', (req, res) => res.status(204).send());

// Routes for Items
app.get('/items', (req, res) => res.status(200).json(items));
app.post('/items', (req, res) => res.status(201).json(req.body));
app.get('/items/:id', (req, res) => res.status(200).json(items[0]));
app.put('/items/:id', (req, res) => res.status(200).json({ updated: true }));
app.delete('/items/:id', (req, res) => res.status(204).send());

describe('Unified API Integration Suite', () => {
  // User Tests (1-5)
  it('GET /users works', async () => { const res = await request(app).get('/users'); expect(res.statusCode).toBe(200); });
  it('POST /users works', async () => { const res = await request(app).post('/users').send({u: "test"}); expect(res.statusCode).toBe(201); });
  it('GET /users/:id works', async () => { const res = await request(app).get('/users/1'); expect(res.statusCode).toBe(200); });
  it('PUT /users/:id works', async () => { const res = await request(app).put('/users/1'); expect(res.statusCode).toBe(200); });
  it('DELETE /users/:id works', async () => { const res = await request(app).delete('/users/1'); expect(res.statusCode).toBe(204); });

  // Item Tests (6-10)
  it('GET /items works', async () => { const res = await request(app).get('/items'); expect(res.statusCode).toBe(200); });
  it('POST /items works', async () => { const res = await request(app).post('/items').send({n: "drill"}); expect(res.statusCode).toBe(201); });
  it('GET /items/:id works', async () => { const res = await request(app).get('/items/1'); expect(res.statusCode).toBe(200); });
  it('PUT /items/:id works', async () => { const res = await request(app).put('/items/1'); expect(res.statusCode).toBe(200); });
  it('DELETE /items/:id works', async () => { const res = await request(app).delete('/items/1'); expect(res.statusCode).toBe(204); });
});
