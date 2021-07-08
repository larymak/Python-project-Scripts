# Usage of the wikipedia


 >>>import wikipedia<br/>
 >>>print wikipedia.summary("Wikipedia")<br/>
output : Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited,<br/> 
multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...<br/>

>>>>wikipedia.search("Barack")<br/>
output : [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama',<br/> 
u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, <br/>
2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']<br/>

>>> ny = wikipedia.page("New York")<br/>
>>> ny.title<br/>
output : u'New York'
>>> ny.url<br/>
output : *[Click URL :](u'http://en.wikipedia.org/wiki/New_York')<br/>
>>> ny.content<br/>
output : u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...<br/>
>>> ny.links[0]<br/>
output : u'1790 United States Census'<br/>

>>> wikipedia.set_lang("fr")<br/>
>>> wikipedia.summary("Facebook", sentences=1)<br/>
output : Facebook est un service de réseautage social en ligne sur Internet permettant d'y publier des,<br/>
 informations (photographies, liens, textes, etc.) en contrôlant leur visibilité par différentes catégories de personnes.<br/>
