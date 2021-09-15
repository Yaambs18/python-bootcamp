import unittest
import bank_class

class Test_withdr(unittest.TestCase):
    def test_balance(self):
        acct1 = bank_class.Account('Jose',100)
        acct1.deposit(50)
        bal = acct1.balance
        self.assertEqual(bal, 150)

if __name__ == '__main__':
    unittest.main()

