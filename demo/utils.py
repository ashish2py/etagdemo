class ETagConstructor(object):
    def __init__(self):
        bits = self.get_bits()
        return None

    def get_bits(self):
        return 124

default_etag_constructor = ETagConstructor()

default_list_etag_calculator = default_etag_constructor
