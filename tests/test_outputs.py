import json
import re
from collections import Counter


def expected_report():
    paths = Counter()
    ips = set()
    total = 0

    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += 1
            ips.add(line.split()[0])

            match = re.search(
                r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ',
                line,
            )

            if match:
                paths[match.group(1)] += 1

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def test_report_contents():
    with open("/app/report.json") as f:
        actual = json.load(f)

    assert actual == expected_report()