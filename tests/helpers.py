import subprocess


def run_and_capture(cmd, path):
    result = subprocess.run([cmd, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    # TODO print stderr on failure
    return result.stdout
