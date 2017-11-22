from blinker import Signal


class Processor:
    on_a = Signal()
    on_b = Signal()

    def a(self):
        self.on_a.send(self)

    def b(self):
        self.on_b.send(self, first_kw='some data', second_kw=123456)


processor = Processor()


@processor.on_a.connect
def a_notified(sender):
    print('Processor %s a!' % sender)


@processor.on_b.connect
def b_notified(sender, **kwargs):
    print('Processor %s b! %r' % (sender, kwargs))


processor.a()
processor.b()
