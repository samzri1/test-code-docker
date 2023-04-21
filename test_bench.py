import pytest
import requests

@pytest.mark.benchmark(group='simple', warmup=True, warmup_iterations=2, disable_gc=True)
def test_benchmark(benchmark):
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
    benchmark(response.elapsed.total_seconds)



#pip install pytest-benchmark