<html>
<body>
<h1 class="title">Computationally hard problems</h1>
<h3 class="why">Why</h3>
<p class="why">This project was created for Computationally Hard Problems subject during MSc of Computer Science studies at Technical University of Denmark (DTU).</p>
<h3 class="what">What</h3>
<p class="what">We were presented with a crossword problem - a crossword layout and a set of available words of various lenght is presented. The crossword layout is a rectangle and works pretty much like a typical crossword. It can contain 'blocking' character which indicates, that in the given place a character cannot be inserted. The goal of the project was to prove the NP-Completness of the crossword problem and create a crossword validator as well as an algorithm that can solve it as efficiently as possible, or return a 'NO' if the crossword is unsolvable with the available set of words. The whole project was created in collaboration, but the problem solver was created entirely by me.</p>
<h3 class="how">How</h3>
<p class="how">The solving algorithm is a recursive brute-force algorithm. On every iteration a first available empty row (or word in a row) is selected. The length of the word that needs to fit is then calculated, and a random word of this length is inserted. After a word is inserted, every column that this row belongs to is incrementally checked - given the already filled-out characters in the column, we check if there is at least one available word that could be inserted into this column. If there is, the algorithm proceeds to insert a word into the next available row. If there isn't, the algorithm takes a step back and tries to insert another word into that row. All in all, the maximum recursion depth is equal to the number of available horizontal word slots in the crossword.</p>
<h3 class="technologies">Technologies used</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
</ul>
<hr>
<small class="created">Created: November 2018</small>
</body>
</html>
