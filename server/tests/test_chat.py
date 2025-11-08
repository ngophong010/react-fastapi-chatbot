import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from main import api

client = TestClient(api)

class TestChatAPI:
    def test_health_check(self):
        response = client.get("/test")
        assert response.status_code == 200
        assert response.json() == {"msg": "API is Online"}
    
    @patch('src.redis.config.Redis')
    def test_token_generation(self, mock_redis):
        # Mock Redis connection
        mock_redis_instance = AsyncMock()
        mock_redis.return_value = mock_redis_instance
        
        response = client.post("/token?name=TestUser")
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert data["name"] == "TestUser"
    
    def test_token_generation_empty_name(self):
        response = client.post("/token?name=")
        assert response.status_code == 400