import unittest
from hydraulics.hsystem import HSystem
from hydraulics.elements import Source, Tap, Split, Sink


class TestR1(unittest.TestCase):

    def setUp(self):
        self._tap = Tap("tap")
        self._source = Source("src")
        self._sink = Sink("sink")
        self._split = Split("split")

    def test_get_name(self):
        self.assertEqual(self._tap.get_name(), "tap")
        self.assertEqual(self._source.get_name(), "src")
        self.assertEqual(self._sink.get_name(), "sink")
        self.assertEqual(self._split.get_name(), "split")

    def test_add_get(self):
        h = HSystem()
        h.add_element(self._tap)
        h.add_element(self._source)
        h.add_element(self._sink)
        h.add_element(self._split)
        self.assertTrue(self._tap in h.get_elements())
        self.assertTrue(self._source in h.get_elements())
        self.assertTrue(self._sink in h.get_elements())
        self.assertTrue(self._split in h.get_elements())


class TestR2(unittest.TestCase):

    def setUp(self):
        self._tap = Tap("tap")
        self._source = Source("src")
        self._sink = Sink("sink")

    def test_connect(self):
        self._source.connect(self._tap)
        self._tap.connect(self._sink)
        self.assertIs(self._source.get_output(), self._tap)
        self.assertIs(self._tap.get_output(), self._sink)

    def test_connect_sink(self):
        self._sink.connect(self._tap)
        self.assertIs(self._sink.get_output(), None)

    def test_get_outputs_none(self):
        self.assertIs(self._source.get_output(), None)
        self.assertIs(self._tap.get_output(), None)


class TestR3(unittest.TestCase):

    def setUp(self):
        self._tap = Tap("tap")
        self._sink = Sink("sink")
        self._split = Split("split")

    def test_connect_at(self):
        self._split.connect_at(self._tap, 0)
        self._split.connect_at(self._sink, 1)
        outputs = self._split.get_outputs()
        self.assertIs(outputs[0], self._tap)
        self.assertIs(outputs[1], self._sink)

    def test_connect_at_none(self):
        self._split.connect_at(self._tap, 0)
        outputs = self._split.get_outputs()
        self.assertIs(outputs[0], self._tap)
        self.assertIs(outputs[1], None)


class TestR5(unittest.TestCase):

    def setUp(self):
        self._source = Source("src")
        self._tap = Tap("tap")
        self._split = Split("split")
        self._sink1 = Sink("sink1")
        self._sink2 = Sink("sink2")

        self._hsys = HSystem()
        self._hsys.add_element(self._source)
        self._hsys.add_element(self._tap)
        self._hsys.add_element(self._split)
        self._hsys.add_element(self._sink1)
        self._hsys.add_element(self._sink2)

    def test_simple_test_open(self):
        self._source.connect(self._tap)
        self._tap.connect(self._sink1)
        self._source.set_flow(4.789)
        self._tap.set_status(to_open=True)
        info = self._hsys.simulate()
        self.assertEqual(len(info), 3)
        self.assertTrue('Source src 0.000 4.789' in info)
        self.assertTrue('Tap tap 4.789 4.789' in info)
        self.assertTrue('Sink sink1 4.789 0.000' in info)

    def test_simple_test_close(self):
        self._source.connect(self._tap)
        self._tap.connect(self._sink1)
        self._source.set_flow(4.789)
        self._tap.set_status(to_open=False)
        info = self._hsys.simulate()
        self.assertEqual(len(info), 3)
        self.assertTrue('Source src 0.000 4.789' in info)
        self.assertTrue('Tap tap 4.789 0.000' in info)
        self.assertTrue('Sink sink1 0.000 0.000' in info)

    def test_simple_test_split(self):
        self._source.connect(self._split)
        self._split.connect_at(self._sink1, 0)
        self._split.connect_at(self._sink2, 1)
        self._source.set_flow(6.789)
        info = self._hsys.simulate()
        self.assertEqual(len(info), 4)
        self.assertTrue('Source src 0.000 6.789' in info)
        self.assertTrue('Split split 6.789 3.394 3.394' in info)
        self.assertTrue('Sink sink1 3.394 0.000' in info)
        self.assertTrue('Sink sink2 3.394 0.000' in info)

    def test_all_elements(self):
        self._source.connect(self._tap)
        self._tap.connect(self._split)
        self._split.connect_at(self._sink1, 0)
        self._split.connect_at(self._sink2, 1)
        self._source.set_flow(7)
        self._tap.set_status(to_open=True)
        info = self._hsys.simulate()
        self.assertEqual(len(info), 5)
        self.assertTrue('Source src 0.000 7.00 in info')
        self.assertTrue('Tap tap 7.000 7.000' in info)
        self.assertTrue('Split split 7.000 3.500 3.500' in info)
        self.assertTrue('Sink sink1 3.500 0.000' in info)
        self.assertTrue('Sink sink2 3.500 0.000' in info)
