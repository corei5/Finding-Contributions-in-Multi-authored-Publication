# Finding-Contributions-in-Multi-authored-Publication

BOP:

Here, impact of the author is calcualted based on number of papers he/she published in Scopus in that particular year.

Impact = b / tp

where b->number of papers published by that author in that particular year
tp-> total number of papers published by UMP in that particular year.

CBPOS:

Here, impact of the author is calcualted based on atuhors' position in all of his/her published papers in Scopus in that particular year.

i = author_pos
a_i = 1 / i

b_i = a_i / SUM(a_0, ..., a_n)
where n -> number of authors in that paper

Impact = SUM(b_0, ..., b_m) / tp
where m ->number of papers published by that author in that particular year
tp-> total number of papers publihsed by UMP in that particular year

EC:

Here, impact of the author is calcualted based on the consideration that all the authors have equal contributions in a papaer.

b_i = 1 / number_of_authors
Impact = SUM(b_0, ..., b_m) / tp

where m -> number of papers published in that year
tp-> total number of papers published by UMP in that year
