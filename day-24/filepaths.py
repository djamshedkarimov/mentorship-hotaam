# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("my_file.txt", mode="w") as file:
    file.write("New text.")

'''modes:
        w = write
        r = read
        a = append'''

'''file path
    \ root
        Work
            report.doc
            Project
                talk.ppt
                
    how to get to talk.ppt:
        /Work/Project/talk.ppt'''