import subprocess
import sys
import unicodedata


def normalize(unicode_str):
    """Returns a copy of the string with any funky unicode characters converted to their more standardized equivalents."""
    # http://stackoverflow.com/a/1207479/358804
    # http://unicode.org/faq/normalization.html#2
    return unicodedata.normalize('NFKD', unicode_str)


def run_and_capture(args):
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # handle failures
    print(result.stderr, file=sys.stderr)
    result.check_returncode()

    return normalize(result.stdout)
