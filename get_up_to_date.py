from git import Repo
repo = Repo('/mnt/sn1/H6C_Notebooks/')
log = repo.heads.main.log()
hashes = []
for l in log[::-1]:
    h = str(l).split(' ')[1]
    hashes.append(h[0:7])
    if h == str(repo.rev_parse('origin/main')):
        break

print(f'for gh in {" ".join(hashes[::-1])}' + ' main; do git checkout ${gh}; git pull; git push -f origin HEAD:main; done')

