
import bag


class TestBag:

    def test_bag(self):
        keg = bag.Bag()
        assert type(keg.keg_list) == list()