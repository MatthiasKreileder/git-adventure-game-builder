import os
import unittest
import subprocess

def init_git():
    """Initialize git by setting user mail and name"""

    subprocess.run(["git", "config", "--global", "user.email", "bbg-test-bot@bloomberg.com"])
    subprocess.run(["git", "config", "--global", "user.name", "The bot!"])

def create_the_game():
    """Create the game in a temporary location"""

    game_name = "/tmp/GIT_GAME"
    p = subprocess.run(["bash", "../setup_clean_repo", "-o", game_name])
    assert (0 == p.returncode), "Un-able to create game:  'setup_clean_repo' failed."
    subprocess.run(["git", "clone", game_name, game_name + '_clone'])

def run_all_test():
    loader = unittest.TestLoader()
    testSuite = loader.discover(os.getcwd())
    testRunner = unittest.TextTestRunner(verbosity=2)
    testRunner.run(testSuite)

if __name__ == "__main__":
    init_git()
    create_the_game()
    run_all_test()
