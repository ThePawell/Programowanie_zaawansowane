### Paweł Dinga 13972
# Test API
Testy są stworzone dla prostego API stworzonogego na potrzeby przedmiotu _Programowanie Aplikacji Internetowych_
### Cel:<br>
Celem testów jest zweryfikowanie, czy API zwraca oczekiwane wyniki w odpowiedzi na różne żądania.<br>

### Testy:<br>
**Test 1: Sprawdzenie poprawności połączenia z API oraz zwróconych danych**<br>
Test sprawdza, czy czy możliwe jest połączenie z API oraz czy zwraca ono poprawne dane na podstawie podanego order id.

Oczekiwana odpowiedź:
```
status_code: 200
```
```
  "order_id": "12345",
  "amount": "80.00",
  "order_date": "2023-05-26 20:03:07",
  "response_code": "200",
  "response_desc": "Success"
```
<br><br>
**Test 2: Sprawdzenie poprawności odpowiedzi dla odred id podanego jako string**<br>
Opis: Ten test sprawdza, czy API zwraca odpowiedni kod odpowiedzi, gdy jako id zostanie wprowadzony string.


Oczekiwana odpowiedź:

```
status_code: 500
```
<br><br>
**Test 3: Sprawdzenie poprawności odpowiedzi dla nieistniejącego order id** <br>
Opis: Ten test sprawdza, czy API zwraca odpowiedne dane, gdy wprowadzone zostanie nieistniejące order id.


Oczekiwana odpowiedź:
```
  null
```
<br><br>
**Test 4: Sprawdzenie odpowiedzi dla niepełnej ściezki**<br>
Opis: Ten test sprawdza, czy API zwraca odpowiedni kod odpowiedzi, gdy podana jest niepełna ścieżka.

Oczekiwana odpowiedź:

{
  "transactions": []
}
Wnioski
Testy jednostkowe API zostały pomyślnie przeprowadzone, a wszystkie endpointy działały zgodnie z oczekiwaniami. Każdy z testów sprawdzał inną funkcjonalność i zwracał oczekiwane wyniki. Przed uruchomieniem testów upewnij się, że serwer API jest uruchomiony i dostępny pod odpowiednim adresem URL.

W powyższym przykładzie przedstawiono prostą dokumentację dla testów jednostkowych API. Możesz dostosować ją do swoich potrzeb, dodając więcej informacji, takich jak autor testów, wymagania dotyczące uruchomienia, itp. Dokumentacja ta ma na celu zapewnić zrozumienie testów, instrukcje uruchomienia i wyniki oczekiwane dla każdego testu, aby ułatwić przyszłe testowanie i utrzymanie kodu.

