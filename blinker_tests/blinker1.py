from blinker import signal


def subscriber(sender):
    print("Got a signal sent by %r" % sender)


ready = signal('ready')
ready.connect(subscriber)
ready.send('fake sender')
