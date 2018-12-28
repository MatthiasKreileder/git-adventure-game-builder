import subprocess
import os
import shutil

class StartGame:
    """
    Provide a way to start the game.
    """

    def enter(self):

        process = subprocess.Popen(['./start_game'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                
        (out,err) = process.communicate('/tmp/game-data\n'.encode('utf-8'))
        self.stdout = out.decode()
        self.stderr = err.decode()

    def show_output(self):
        print(self.stdout)
        print(self.stderr)

    def check_data_dir_created(self):
        return os.path.isdir("/tmp/game-data")