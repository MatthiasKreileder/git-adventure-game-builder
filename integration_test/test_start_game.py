import os
import pygit2
import shutil
import startgame
import subprocess
import tempfile
import unittest
import util

class StartGameTest(unittest.TestCase):

    def setUp(self):
        self.tmpfolder = tempfile.TemporaryDirectory()
        util.copytree("/tmp/GIT_GAME_clone", self.tmpfolder.name)
        os.chdir(self.tmpfolder.name)

    def tearDown(self):
        self.tmpfolder.cleanup()

    def test_start_game_default_data_dir(self):
        """
        Test that we can start the game.
        Accepting the default location for the data directory.
        """
        sg = startgame.StartGame()
        sg.enter()

        self.assertTrue(sg.check_data_dir_created())

        repository_path = pygit2.discover_repository(os.getcwd())
        repo = pygit2.Repository(repository_path)
        local_branches = list(repo.branches.local)

        expectBranches = ['00_enter_the_forest', 'master']
        self.assertEqual(expectBranches, local_branches)


if __name__ == "__main__":
    unittest.main()