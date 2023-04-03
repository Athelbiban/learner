with open('../../stepik_pba/2/dataset_24465_4.txt', encoding='utf-8') as inf,\
        open('new_file.txt', 'w', encoding='utf-8') as ouf:
    ouf.write('\n'.join(inf.read().split()[::-1]))
