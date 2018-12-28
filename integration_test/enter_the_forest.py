
import pygit2
import os
import code
class EnterTheForest:
    """
    Provide a class that plays the 'enter_the_forest' level.
    """
    def place_solution_string_into_talisman(self):
        
        with open('talisman', 'w') as f:
            f.write('grace')

    def make_commit(self):

        # Get a handle to the repo
        repository_path = pygit2.discover_repository(os.getcwd())
        repo = pygit2.Repository(repository_path)

        # Add the talisman file to the index
        repo.index.add('talisman')
        repo.index.write()
        tree = repo.index.write_tree()

        # actually make the commit
        author = pygit2.Signature('Alice Author', 'alice@authors.tld')
        commiter = pygit2.Signature('Cecil Committer', 'cecil@committers.tld')
        repo.create_commit('refs/heads/00_enter_the_forest', author, commiter, 'blubb commit msg', tree, [repo.lookup_reference("refs/heads/00_enter_the_forest").get_object().hex])
    