from app import get_github_status

def test_github_api():
    status = get_github_status()
    assert status == 200
