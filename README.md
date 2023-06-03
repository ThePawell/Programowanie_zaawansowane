### Paweł Dinga 13972
# Test API
### Cel:<br>
Celem testów jest zweryfikowanie, czy API zwraca oczekiwane wyniki w odpowiedzi na różne żądania.<br>

### Testy:<br>
**Test 1:**<br> 
Sprawdzenie poprawności połączenia z API oraz zwróconych danych<br>
Test sprawdza, czy endpoint /transaction/{id} zwraca poprawne dane transakcji na podstawie podanego order id.

Wysyłane żądanie: GET /transaction/4
Oczekiwana odpowiedź:
json
Copy code
```
  "order_id": "12345",
  "amount": "80.00",
  "order_date": "2023-05-26 20:03:07",
  "response_code": "200",
  "response_desc": "Success"
```
**Test 2:** Sprawdzenie poprawności odpowiedzi dla endpointu /transaction/{id} (brak transakcji)
Opis: Ten test sprawdza, czy endpoint /transaction/{id} zwraca odpowiedni komunikat błędu, gdy nie ma transakcji o podanym identyfikatorze.

Wysyłane żądanie: GET /transaction/10
Oczekiwana odpowiedź:
json
Copy code
{
  "error": "Transaction not found"
}
**Test 3:** Sprawdzenie poprawności odpowiedzi dla endpointu /transaction
Opis: Ten test sprawdza, czy endpoint /transaction zwraca wszystkie transakcje.

Wysyłane żądanie: GET /transaction
Oczekiwana odpowiedź:
json
```
{
  "transactions": [
    {
      "id": "1",
      "order_id": "54321",
      "amount": "120.50",
      "order_date": "2023-05-25 14:23:11",
      "response_code": "200",
      "response_desc": "Success"
    },
    {
      "id": "2",
      "order_id": "98765",
      "amount": "50.00",
      "order_date": "2023-05-25 17:45:32",
      "response_code": "200",
      "response_desc": "Success"
    },
    ...
  ]
}
```
Test 4: Sprawdzenie poprawności odpowiedzi dla endpointu /transaction (pusty wynik)
Opis: Ten test sprawdza, czy endpoint /transaction zwraca pustą listę transakcji, gdy nie ma żadnych dostępnych.

Wysyłane żądanie: GET /transaction
Oczekiwana odpowiedź:
json
Copy code
{
  "transactions": []
}
Wnioski
Testy jednostkowe API zostały pomyślnie przeprowadzone, a wszystkie endpointy działały zgodnie z oczekiwaniami. Każdy z testów sprawdzał inną funkcjonalność i zwracał oczekiwane wyniki. Przed uruchomieniem testów upewnij się, że serwer API jest uruchomiony i dostępny pod odpowiednim adresem URL.

W powyższym przykładzie przedstawiono prostą dokumentację dla testów jednostkowych API. Możesz dostosować ją do swoich potrzeb, dodając więcej informacji, takich jak autor testów, wymagania dotyczące uruchomienia, itp. Dokumentacja ta ma na celu zapewnić zrozumienie testów, instrukcje uruchomienia i wyniki oczekiwane dla każdego testu, aby ułatwić przyszłe testowanie i utrzymanie kodu.

