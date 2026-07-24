# API Documentation

## Authentication
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@institution.edu",
  "password": "securepassword"
}
```

## Core Endpoints
### Prediction Endpoint
```http
POST /predict
Authorization: Bearer <token>
Content-Type: application/json

{
  "citation_count": 45,
  "h_index": 8,
  "collab_network_score": 0.72
}
```

### Researcher Search
```http
GET /researchers?min_score=0.8&specialization=NL
```

## WebSocket Updates
```javascript
const ws = new WebSocket('wss://api/predictions/stream');
ws.onmessage = (event) => {
  console.log('Real-time update:', JSON.parse(event.data));
};
```