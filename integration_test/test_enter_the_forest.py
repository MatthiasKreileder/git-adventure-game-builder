import enter_the_forest
import os
import startgame
import tempfile
import unittest
import util
import pygit2
import subprocess

class EnterTheForestTest(unittest.TestCase):

    def setUp(self):
        self.tmpfolder = tempfile.TemporaryDirectory()
        util.copytree("/tmp/GIT_GAME_clone", self.tmpfolder.name)
        os.chdir(self.tmpfolder.name)
        sg = startgame.StartGame()
        sg.enter()

    def tearDown(self):
        self.tmpfolder.cleanup()

    def test_enter_the_forest(self):
        
        ef = enter_the_forest.EnterTheForest()
        ef.place_solution_string_into_talisman()
        ef.make_commit()

        # TODO Run hook manually.  libgit2 doesn't run hooks for us
        # Then check if a new level branch has been unlocked.


if __name__ == "__main__":
    unittest.main()