import os


# Create a list of all of the fixtures used for testing
pytest_plugins = [
    # Add the fixtures directory on and remove the .py
    os.path.splitext('fixtures/{fixture}'.format(fixture=f))[0] for f in
    # For each file that begins with fixtures_ the fixtures folder
    list(filter(lambda x: x.startswith('fixture_'),
                os.listdir("tests/fixtures")))]
