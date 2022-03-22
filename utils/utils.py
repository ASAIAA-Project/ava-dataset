import os

def moveimgs():
    """Move images out of extracted dir."""
    oldp = os.path.join(os.path.dirname(__file__), 'AVA/images/images')
    newp = os.path.join(os.path.dirname(__file__), 'AVA/images/')
    print(oldp)
    # print(os.listdir(oldp))
    for fname in os.listdir(oldp):
        if fname.endswith('jpg'):
            os.system(f'mv {os.path.join(oldp, fname)} {newp}')

def avatxt():
    """Check AVA.txt."""
    avapath = os.path.join(os.path.dirname(__file__), 'AVA/AVA.txt')
    with open(avapath, 'r') as lines:
        for line in lines:
            imgid = line.split()[1]
            imgpath = os.path.join(os.path.dirname(__file__), f'AVA/images/{imgid}.jpg')
            if not os.path.exists(imgpath):
                print(imgid) 

def get_score():
    avapath = os.path.join(os.path.dirname(__file__), 'AVA/AVA.txt')
    with open(avapath, 'r') as lines:
        for line in lines:
            votes, sc = 0, 0
            for w, s in enumerate(line.split()[2:12]):
                votes += int(s)
                sc += (w+1) * int(s)
            print(votes, sc, sc/votes)
            break

if __name__ == "__main__":
    # moveimgs()
    # avatxt()
    get_score()