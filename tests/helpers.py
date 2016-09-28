import subprocess
import sys


def run_and_capture(cmd, path):
    result = subprocess.run([cmd, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # handle failures
    print(result.stderr, file=sys.stderr)
    result.check_returncode()

    return result.stdout
