import sys

result = sys.stdin.read()

print(result)
print("\n" + "=" * 80 + "\n")

assert result.count("Up") == 0, "There should not be any running containers (STATUS Up)"
assert (
    result.count("Exited") == 0
), "There should not be any exited containers (STATUS Exited)"

print("Success!")
