from git import Repo


def commit_count():
    """
    统计某个分支commit总数

    :return:
    """
    repo = Repo('/Users/sakura/Data/temp/GitOpeationsTest')
    count = len(list(repo.iter_commits(rev='main')))
    print(count)


if __name__ == '__main__':
    commit_count()
