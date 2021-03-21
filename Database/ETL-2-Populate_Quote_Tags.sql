insert into quote_tags
(select q.quote_id, qti.tag  
from quote_tags_initialize as qti,
	 quotes as q 
where qti.text = q.text) 