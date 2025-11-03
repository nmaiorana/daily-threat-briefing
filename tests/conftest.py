import pytest
from datetime import datetime

@pytest.fixture
def sample_nvd_item():
    # Simulates the normalized record mapping from NVD
    return {
        "id": "CVE-2025-0001",
        "source": "NVD",
        "published": datetime.utcnow().isoformat() + "Z",
        "headline": "Example RCE vulnerability in foobar",
        "body": "A remote code execution vulnerability was discovered. PoC posted."
    }

@pytest.fixture
def sample_bc_item():
    return {
        "id": "bc-1234",
        "source": "BC",
        "published": datetime.utcnow().isoformat() + "Z",
        "headline": "Ransomware campaign hits ACME corp",
        "body": "Ransomware campaign observed in the wild targeting ACME. Supply chain implications."
    }

@pytest.fixture
def many_items(sample_nvd_item, sample_bc_item):
    return [sample_nvd_item, sample_bc_item]
