select a.born, a.description, a.author_name, q.text, qt.tag
from Author a, Quotes q, Quote_tags qt
Where
q.author_name = 'Albert Einstein' and
q.author_name = a.author_name and
qt.quote_id = q.quote_id
--Needs Summary Piece?