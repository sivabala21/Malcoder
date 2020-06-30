def convert(name, code):
    try:
        import os
        vir = open(name, 'w')
        vir.write(code)
        vir.close()
        my_file = name
        base = os.path.splitext(my_file)[0]
        os.rename(my_file, base + '.bat')
        return
    except FileExistsError:
        os.remove(name)
        from time import sleep
        sleep(2)
        print("File Already exists")
        return