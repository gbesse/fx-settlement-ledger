import unittest
from decimal import Decimal as D
from fx_settlement_ledger import run
class Tests(unittest.TestCase):
 def data(self):return {'foreign_currency':'USD','base_currency':'EUR','invoice_foreign':'100','settled_foreign':'100','invoice_rate':'1.1','settlement_rate':'1.2','quote_direction':'base_per_foreign','fee_base':'2'}
 def test_known_gain_fee_and_balanced_receipt(self):
  r=run(self.data());self.assertEqual(r['fx_gain'],'10.00');self.assertEqual(r['postings'][0]['debit_minus_credit'],'118.00');self.assertEqual(D(r['debit_minus_credit_total']),0)
 def test_partial_settlement(self):
  d=self.data();d['settled_foreign']='50';r=run(d);self.assertEqual(r['remaining_foreign'],'50');self.assertEqual(r['book_value_settled'],'55.00')
 def test_inverse_quote_uses_inverse_not_multiply(self):
  d=self.data();d.update(invoice_rate='2',settlement_rate='4',quote_direction='foreign_per_base');r=run(d);self.assertEqual(r['fx_gain'],'-25.00');self.assertEqual(r['gross_settlement'],'25.00')
 def test_rounding_is_separate_and_exactly_balances(self):
  d=self.data();d.update(invoice_rate='1.001',settlement_rate='1.007',settled_foreign='1',fee_base='.005');r=run(d);self.assertEqual(sum(D(x['debit_minus_credit'])for x in r['postings']),0);self.assertEqual(r['rounding_balance'],'0.01')
 def test_overpayment_and_zero_rate_rejected(self):
  for k,v in [('settled_foreign','101'),('invoice_rate','0')]:
   d=self.data();d[k]=v
   with self.assertRaises(ValueError):run(d)
