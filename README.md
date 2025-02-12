curl -X POST "http://localhost:8000/users/" -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "secret"}'
curl -X GET "http://localhost:8000/users/"