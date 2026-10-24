import unittest,json,subprocess,sys,tempfile
from pathlib import Path
class DecimalInputContract(unittest.TestCase):
 def test_bad_or_extreme_decimal_is_localized_in_all_languages(self):
  base=json.loads(Path('examples/demo.json').read_text())
  for value in ('invalid','1e1000000','1e-1000000'):
   data=dict(base)
   data['invoice_rate']=value
   with tempfile.TemporaryDirectory()as tmp:
    p=Path(tmp)/'input.json';p.write_text(json.dumps(data))
    for lang in ('fr','en','es'):
     result=subprocess.run([sys.executable,'-m','fx_settlement_ledger',str(p),'--lang',lang],capture_output=True,text=True)
     self.assertEqual(result.returncode,2,result.stderr);self.assertEqual(json.loads(result.stderr)['code'],'invalid_input');self.assertNotIn('Traceback',result.stderr)
