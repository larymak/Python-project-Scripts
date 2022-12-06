import wikipedia
wikipedia.set_lang("fr")
print(wikipedia.summary("Facebook", sentences=1))

# output : 
# Facebook est un service de réseautage social en ligne sur Internet permettant d'y publier des informations (photographies, liens, textes, etc.) en contrôlant leur visibilité par différentes catégories de personnes.
