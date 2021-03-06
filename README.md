# CognitiveMonitorApp

Login: Grażyna,
Hasło: password

create_database.py - skrypt resetujący bazę danych SQLite i wypełniający ją testowymi danymi użytkownika

Folder screenshots zawiera zrzuty ekranu z poszczególnych elementów aplikacji

# Technologie

- Python
- Framework Kivy do tworzenia GUI
- Baza danych SQLite

# Możliwe ulepszenia

Ponieważ jest to tylko wersja demo, nie zawiera ona wszystkich funkcjonalności. Przede wszystkim brakuje kluczowej funkcji, jaką jest możliwość uruchamiania gier sprawdzających zdolności poznawcze użytkownika wraz z zapisywaniem w bazie danych wyników uzyskanych w każdym podejściu do gry. Nie udało się zaimplementować tych funkcji ze względu na niedostateczną ilość czasu. 

Pozostałe funkcje, które powinny znaleźć się w aplikacji to, między innymi:

- rejestracja nowych użytkowników (na razie można logować się tylko jako użytkownik testowy)
- możliwość zmiany emaila/numeru telefonu oraz hasła użytkownika
- możliwość tworzenia bardziej szczegółowych podsumowań i raportów z wyników uzyskanych w grach (na razie wyświetlane są tylko w formie wykresu zmian uzyskanej punktacji w czasie)
- możliwość wysyłania podsumowań wyników gier na adres email lekarza i bliskiej osoby
- dostosowywanie wyglądu interfejsu użytkownika w zależności od wieku osoby (duże litery i większy kontrast kolorystyczny dla osób starszych, standardowy interfejs dla osób młodszych)
- dodanie tutorialu pokazującego sposób korzystania z aplikacji
- dodanie obsługi błędów w kodzie wywołanych błędnymi danymi wprowadzonymi przez użytkownika oraz poprawa bezpieczeństwa aplikacji (na przykład mechanizmu logowania i przechowywania haseł)

