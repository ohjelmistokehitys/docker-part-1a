import sys

result = sys.stdin.read()

print(result)
print("\n" + "=" * 80 + "\n")

assert result.count("Up") >= 2, "There should be two running containers (STATUS Up)"
assert (
    result.count("Exited") >= 1
), "There should be an exited container (STATUS Exited)"

print("Success!")
