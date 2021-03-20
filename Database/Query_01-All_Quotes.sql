select a.author_name, q.text, qt.tag
from Author a, Quotes q, Quote_tags qt
Where
q.author_name = a.author_name and
qt.quote_id = q.quote_id
Order by a.author_name, q.text, qt.tag