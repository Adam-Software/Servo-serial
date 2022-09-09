import unittest
from servo_serial.connection import Connection


class ConnectTestCase(unittest.TestCase):

    def test_similarity_class_instances(self):
        connect1 = Connection()
        connect2 = Connection()
        self.assertEqual(connect1, connect2)

    def test_not_init_close_port(self):
        connect = Connection()
        self.assertEqual(connect.closePort(), None)

    def test_init_close_port(self):
        connect = Connection()
        connect.getPacketHandler()
        self.assertEqual(connect.closePort(), None)


if __name__ == '__main__':
    unittest.main()