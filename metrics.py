# This file is part of the inventory management project and captures metrics during execution.
# It records the time taken for execution and allows for dumping metrics to a JSON file.

import time, json
from logging import getLogger

logger = getLogger(__name__)


class Metrics:
    def __init__(self):
        self.start = time.time()
        self.data = {}

    def record(self, key, value):
        self.data[key] = value

    def dump(self, path="metrics.json"):
        self.data["runtime_sec"] = time.time() - self.start
        with open(path, "w") as f:
            json.dump(self.data, f, indent=2)
        logger.info(f"Metrics dumped to {path}")
