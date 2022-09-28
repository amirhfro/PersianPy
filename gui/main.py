import eel

eel.init('interface')


def execution(n):
    exec(n)


eel.get_code()(execution)

eel.start('index.html')
