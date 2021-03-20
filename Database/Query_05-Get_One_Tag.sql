select qt1.tag, q.text, qt2.tag 
from Quotes q, Quote_tags qt2, Quote_tags qt1
Where
qt2.quote_id = q.quote_id and 
q.quote_id = qt1.quote_id and 
qt1.tag in ('love')

Order by qt1.tag, q.text, qt2.tag

