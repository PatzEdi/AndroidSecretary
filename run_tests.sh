# Simple script used to run all tests at once via the command line.

# Run the tests using unittest:
python3 -m unittest discover -s tests -p "*test*.py"

# Capture the exit code
EXIT_CODE=$?

# Exit with the same code as the test command
exit $EXIT_CODE