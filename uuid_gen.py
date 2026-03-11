#!/usr/bin/env python3
"""uuid_gen - Generate UUIDs (v1, v4, v5). Zero deps."""
import sys, uuid

def main():
    version = "4"
    count = 1
    if "-v" in sys.argv:
        idx = sys.argv.index("-v")
        version = sys.argv[idx+1]
    if "-n" in sys.argv:
        idx = sys.argv.index("-n")
        count = int(sys.argv[idx+1])
    if "--upper" in sys.argv:
        fmt = str.upper
    else:
        fmt = str
    for _ in range(count):
        if version == "1": u = uuid.uuid1()
        elif version == "4": u = uuid.uuid4()
        elif version == "5":
            ns = sys.argv[-1] if len(sys.argv) > 1 else "test"
            u = uuid.uuid5(uuid.NAMESPACE_DNS, ns)
        else: u = uuid.uuid4()
        print(fmt(str(u)))

if __name__ == "__main__":
    main()
