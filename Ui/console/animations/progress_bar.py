from time import sleep

def launch(sentence):
    width=30
    percent=0,
    # The number of hashes to show is based on the percent passed in. The
    # number of blanks is whatever space is left after.
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',end='', flush=True)

    print(sentence)
    for i in range(101):
        launch(i)
        sleep(0.1)

