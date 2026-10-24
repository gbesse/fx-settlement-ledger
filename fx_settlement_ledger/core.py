from decimal import Decimal,localcontext,ROUND_HALF_EVEN
import re
from .common import integer

def D(x):
 if isinstance(x,bool)or not isinstance(x,(str,int,float))or len(str(x))>50:raise ValueError('decimal')
 value=Decimal(str(x))
 if not value.is_finite()or abs(value)>Decimal('1e12')or value.as_tuple().exponent< -20:raise ValueError('decimal')
 return value
def run(data):
 for k in ('foreign_currency','base_currency'):
  if not isinstance(data[k],str)or not re.fullmatch('[A-Z]{3}',data[k]):raise ValueError('currency')
 if data['foreign_currency']==data['base_currency']:raise ValueError('distinct_currency')
 digits=integer(data.get('base_minor_digits',2),0,4);unit=Decimal(1).scaleb(-digits)
 with localcontext()as context:
  context.prec=60
  invoice=D(data['invoice_foreign']);paid=D(data['settled_foreign']);fee=D(data.get('fee_base','0'));r0=D(data['invoice_rate']);r1=D(data['settlement_rate'])
  if invoice<=0 or not 0<=paid<=invoice or fee<0 or min(r0,r1)<=0:raise ValueError('bounds')
  quote=data['quote_direction']
  if quote=='foreign_per_base':r0=1/r0;r1=1/r1
  elif quote!='base_per_foreign':raise ValueError('quote_direction')
  def q(v):return v.quantize(unit,rounding=ROUND_HALF_EVEN)
  book=q(paid*r0);gross=q(paid*r1);cash=q(paid*r1-fee);fees=q(fee);gain=q(paid*(r1-r0));postings=[{'account':'cash','debit_minus_credit':str(cash)},{'account':'fee','debit_minus_credit':str(fees)},{'account':'receivable','debit_minus_credit':str(-book)},{'account':'fx_gain','debit_minus_credit':str(-gain)}];rounding=-sum(Decimal(x['debit_minus_credit'])for x in postings);postings.append({'account':'rounding','debit_minus_credit':str(rounding)})
  return {'base_currency':data['base_currency'],'foreign_currency':data['foreign_currency'],'book_value_settled':str(book),'gross_settlement':str(gross),'fx_gain':str(gain),'rounding_balance':str(rounding),'remaining_foreign':str(invoice-paid),'postings':postings,'debit_minus_credit_total':str(sum(Decimal(x['debit_minus_credit'])for x in postings)),'model':'caller_supplied_rates_partial_settlement_half_even_declared_minor_units_not_accounting_advice'}
