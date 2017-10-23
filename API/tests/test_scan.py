import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scanner import *

assert db is not None

git_results = git_scan("SynergySINE")

assert isinstance(git_results, set)
assert len(git_results) != 0

print("Finished scanning")

reading_list = create_reading_list(git_results)

assert isinstance(reading_list, list)
assert len(reading_list) != 0

print("Finished creating new reading list")

result = store_reading_list(reading_list, "SynergySINE")

assert result == True

print("All tests finished!")
