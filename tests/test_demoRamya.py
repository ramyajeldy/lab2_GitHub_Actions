import sys
from pathlib import Path

# Add parent directory to path so we can import demoRamya
sys.path.insert(0, str(Path(__file__).parent.parent))

from demoRamya import get_github_status

def test_github_api():
    status = get_github_status()
    assert status[0] == 200
    assert status[1] == 404
    print("GitHub API status code is {} and invalid endpoint status code is {} as expected.".format(status[0], status[1]))
