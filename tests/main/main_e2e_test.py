from tests.commons_test import client, async_get_call
import pytest

expected_result = {"application": "FASTAPI POC"}
"""Not async call"""
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected_result

"""async call"""
@pytest.mark.anyio
async def test_root():
    response = await async_get_call('/')
    assert response.status_code == 200
    assert response.json() == expected_result

