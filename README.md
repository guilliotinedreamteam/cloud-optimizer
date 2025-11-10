# Cloud Optimizer

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Smart cloud resource allocator using genetic algorithms. Universal, easily swappable credentials—swap all platform/cloud/parms instantly via `.env` variables and abstracted calls.

## Features
- Multi-cloud cost optimization (AWS, Azure, GCP, others via pluggable config)
- Genetic-algorithm core for efficient searching
- All credentials, targets, strategies defined in `.env` or passed as args
- No hardcoded vendor or resource IDs—pure abstraction layer
- Python CLI: cloud-agnostic and easy to script

## .env.example
```
CLOUD_PROVIDER=aws
API_KEY=changeme
REGION=us-east-1
OPTIMIZATION_TARGET=cost
```

## Usage
```bash
git clone https://github.com/guilliotinedreamteam/cloud-optimizer.git
cd cloud-optimizer
cp .env.example .env
# Edit your provider/keys
python optimize.py --analysis "7d_usage.json"
```

## How to Swap Clouds/Platforms
- Credentials + provider via `.env`
- To change from AWS to Azure to GCP to any other: just edit `.env` and, if needed, swap out a single client/
import in `cloud_client.py`
- Add new cloud provider by extending `cloud_client.py`, no main code rewrite

## Main Entrypoint Example
```python
import os
PROVIDER = os.getenv('CLOUD_PROVIDER','aws')
API_KEY = os.getenv('API_KEY','changeme')
REGION = os.getenv('REGION','us-east-1')

from cloud_client import get_usage, apply_optimization
usage = get_usage(api_key=API_KEY, region=REGION)
suggestions = optimize(usage)
apply_optimization(suggestions)
```

## Tech Stack
- Python 3.9+
- Modular plugin dispatch for multi-cloud
- Optimizer core in plain Python/genetic algorithm

## Contributing
Open for all cloud PRs/integrations.

## License
MIT
