def average(array):
    rm_dupes = set(array)
    ave = sum(rm_dupes)/len(rm_dupes)
    return f'{ave: .3f}'

if __name__ == '__main__':
