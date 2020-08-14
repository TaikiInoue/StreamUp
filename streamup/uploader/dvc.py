import os


class UploaderDVC:
    def data_versioning(self):

        # TODO: Inoue: I should be able to write better code
        os.chdir("/dgx/github/DVC")
        os.system("cp /dgx/github/StreamUp/data/dataset.zip /dgx/github/DVC/data/dataset5.zip")
        os.system("dvc add data/dataset5.zip")
        os.system("git checkout master")
        os.system("git add data/dataset5.zip.dvc data/.gitignore")
        os.system("git commit -m 'Add data/dataset5.zip.dvc'")
        os.system("git push origin master")
        os.system("dvc push")
        os.chdir("/dgx/github/StreamUp/streamup")
