import json
from cloud_client import get_usage, apply_optimization

def optimize(usage):
    # Minimal genetic algorithm placeholder logic
    # Replace/expand for custom strategies
    out = []
    for item in usage:
        if item['cost'] > 20:
            out.append({"resource":item['service'],"action":"reduce","suggest":"downscale or shutdown"})
    return out

if __name__=="__main__":
    usage = get_usage(api_key="changeme",region="us-east-1") # swap in from os.environ in practice
    suggestions = optimize(usage)
    apply_optimization(suggestions)
    print("Optimization complete. Suggestions:",json.dumps(suggestions,indent=2))
