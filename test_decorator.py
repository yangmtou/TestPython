def link(a):
    def linked():
        print('begin')
        a()
        print('end')
    return linked


@link
def personOneSay():
    print('my name is yct')

#personTwoSay = link(personTwoSay())
@link
def personTwoSay():
    print('my name is ymt')

personOneSay()

personTwoSay()
