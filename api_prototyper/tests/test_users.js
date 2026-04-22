const request = require('supertest');
const express = require('express');

const app = express();
app.use(express.json());

// Mock Data & Routes
let users = [{ id: "1", username: "eco_user" }];

app.get('/users', (req, res) => res.status(200).json(users));
app.post('/users', (req, res) => res.status(201).json(req.body));
app.get('/users/:id', (req, res) => res.status(200).json(users[0]));
app.put('/users/:id', (req, res) => res.status(200).json({ updated: true }));
app.delete('/users/:id', (req, res) => res.status(204).send());

describe('EcoRide User API - Complete Suite', () => {
  // Test 1: List Users
  it('GET /users should return list of users', async () => {
    const res = await request(app).get('/users');
    expect(res.statusCode).toEqual(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  // Test 2: Create User
  it('POST /users should create a new user', async () => {
    const res = await request(app).post('/users').send({ username: "new_green_user" });
    expect(res.statusCode).toEqual(201);
  });

  // Test 3: Get Single User
  it('GET /users/:id should return user details', async () => {
    const res = await request(app).get('/users/1');
    expect(res.statusCode).toEqual(200);
    expect(res.body.username).toBe("eco_user");
  });

  // Test 4: Update User
  it('PUT /users/:id should update user info', async () => {
    const res = await request(app).put('/users/1').send({ username: "updated_user" });
    expect(res.statusCode).toEqual(200);
  });

  // Test 5: Delete User
  it('DELETE /users/:id should remove user', async () => {
    const res = await request(app).delete('/users/1');
    expect(res.statusCode).toEqual(204);
  });
});
