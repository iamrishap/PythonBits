import glob

folders = ['arrays', 'backtracking', 'binary-search', 'bit-manipulation', 'dp', 'graphs', 'greedy', 'hashing',
           'heaps-and-maps', 'linked-lists', 'math', 'stacks-and-queues', 'strings', 'tree', 'two-pointers'
           ]

# for folder in folders:
#     read_files = glob.glob(folder + "/*.py")
#     with open(folder + ".py", "wb") as outfile:
#         for f in read_files:
#             with open(f, "rb") as infile:
#                 name = f.split('/')[1].split('.')[0].split('-')
#                 cap_name = ' '.join([word.capitalize() for word in name])
#                 s = "\n\n#####\t\t" + cap_name + "\t\t#####\n\n"
#                 outfile.write(s.encode())
#                 outfile.write(infile.read())

# for folder in folders:
#     read_files = glob.glob(folder + "/*.py")
#     with open("result" + ".py", "ab") as outfile:
#         folder_name = "\n\n#########################\t" + folder + "\t#########################\n\n"
#         outfile.write(folder_name.encode())
#         for f in read_files:
#             with open(f, "rb") as infile:
#                 name = f.split('/')[1].split('.')[0].split('-')
#                 cap_name = ' '.join([word.capitalize() for word in name])
#                 s = "\n\n#####\t\t" + cap_name + "\t\t#####\n\n"
#                 outfile.write(s.encode())
#                 outfile.write(infile.read())


for folder in folders:
    read_files = glob.glob(folder + "/*.py")
    with open("index" + ".txt", "ab") as outfile:
        folder_name = "\n\n#########################\t" + folder + "\t#########################\n\n"
        outfile.write(folder_name.encode())
        for idx, f in enumerate(read_files):
            with open(f, "rb") as infile:
                name = f.split('/')[1].split('.')[0].split('-')
                cap_name = ' '.join([word.capitalize() for word in name])
                s = str(idx + 1) + ". " + cap_name + "\n"
                outfile.write(s.encode())
                # outfile.write(infile.read())