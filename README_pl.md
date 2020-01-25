<html>
<body>
<h1 class="title">Computationally Hard Problems</h1>
<h3 class="why">Powód</h3>
<p class="why">Niniejszy projekt powstał w ramach przedmiotu Computationally Hard Problems podczas moich studiów magisterskich na Duńskim Uniwersytecie Technicznym (DTU).</p>
<h3 class="what">Cel</h3>
<p class="what">Postawiony został nam problem "rozwiązania krzyżówki" - składa się on z krzyżówki oraz listy dostępnych słów o różnej długości. Krzyżówka jest prostokątna i w zasadzie wygląda jak typowa krzyżówka, zawierająca "elementy blokujące" - miejsca w których niedozwolone jest postawienie znaku (dzięki temu możliwe jest wstawianie słów o długości krótszej niż długość któregoś z boków krzyżówki). Celem projektu było udowodnienie NP-zupełności problemu krzyżówki oraz stworzenie algorytmu sprawdzającego poprawnosć zaproponowanej krzyżówki jak i znalezienie jej rozwiązania, lub zwrócenie "NO" w przypadku gdy krzyzówka nie może zostać rozwiązana przy użyciu listy zaproponowanych słów. Projekt powstał w kooperacji, jednak algorytm rozwiązujący krzyżówkę został w całości stworzony przeze mnie.</p>
<h3 class="how">Wykonanie</h3>
<p class="how">Algorytm rozwiązujący to rekursywny algorytm brute-force. Podczas każdej iteracji, pierwszy odnaleziony pusty wiersz (bądź słowo w wierszu) jest odnajdowane. Następnie obliczana jest długość słowa i losowo wybierane jest słowo z listy dostępnych słów o odpowiedniej długości, i umieszczane w krzyżówce. Po umieszczeniu słowa w wierszu, każda kolumna, do której ten wiersz przynależy, jest sprawdzana przyrostowo - biorąc pod uwagę znaki już umieszczone w kolumnie, sprawdzane jest czy istnieje przynajmniej jedno słowo (o wymaganej przez kolumnę długości), które może byc wstawione w tym miejscu. Jeśli takie słowo jest dostępne dla każdej z kolumn, algorytm wstawia kolejne słowo w wierszu. Jeśli przynajmniej dla jednej z kolumn takie słowo nie istnieje, algorytm cofa się i wybiera kolejne słowo do wstawienia w tym wierszu. W związku z tym, maksymalna głębokość rekurencji jest równa ilości wszystkich słów poziomo w krzyżówce.</p>
<h3 class="technologies">Zastosowane technologie</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
</ul>
<hr>
<small class="created">Data powstania: Listopad 2018</small>
</body>
</html>
