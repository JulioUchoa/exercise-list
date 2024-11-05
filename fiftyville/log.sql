-- Keep a log of any SQL queries you execute as you solve the mystery.

==> crime_scene_reports
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28;
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 27;
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 26;
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 25;
-- CONCLUSÃO > The robbery occuried at 10:15am. three withness mentioned the bakery

==> interviews
SELECT * FROM interviews WHERE month = 7 AND day = 28;
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND id > 160 AND id < 164;
-- CONCLUSÃO > Ruth reported that she saw the thief getting into a car in bakery parking between 10:14 and 10:35.
--           > Eugene saw the thief at the ATM withdrawing money earlier in 07/28.
--           > Raymond reported that he heard the thief saying that they're planning to leave the town on the first flight next morning(29).
--           > Raymond said that the thief phoned someone for less than a minute. and ask the person to buy the flight ticket.
--           > the first flight on 29th heads LaGuardia Airpot - New York City

==> bakery_security_logs
SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28;
SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 35;
SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 35;
-- CONCLUSÃO > the following licence_plates left the bakery park within 10:16 and 10:35 ::
-- 5P2BI95 - 94KL13X - 6P58WS2 - 4328GD8 - G412CB7 - L93JTIZ - 322W7JE - ONTHK55 - 1106N58

==> atm_transaction
SELECT * FROM atm_transactions WHERE day = 28 AND atm_location = "Humphrey Lane";
SELECT * FROM atm_transactions WHERE day = 28 AND atm_location = "Humphrey Lane" AND transaction_type = "withdraw";
SELECT account_number FROM atm_transactions WHERE day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";
-- CONCLUSÃO > the following account_numbers withdraw money at ATM in Humphrey Lane street on july 28th :
-- 28500762 - 28296815 - 76054385 - 49610011 - 16153065 - 25506511 - 81061156 - 26013199

==> Exploring
SELECT * FROM people;
SELECT * FROM passengers;
SELECT * FROM bank_accounts;
SELECT * FROM phone_calls;
SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;
SELECT * FROM flights WHERE day = 29;

==> people + bank_accounts
SELECT people.name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE account_number IN
(SELECT account_number FROM atm_transactions WHERE day = 28 AND atm_location = "Leggett Street" and transaction_type = "withdraw");
-- CONCLUSÃO > The following people withdraw money from ATM at Humphrey Lane on 28th morning:
-- Bruce - Diana - Brooke - Kenny - Iman - Luca - Taylor - Benista

==> bakery_security_logs + people
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 35);
SELECT name, passport_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 14 AND minute < 35);
-- CONCLUSÃO > the following people exited the bakery park between 10:14 and 10:35 on july 28th:
-- Vanessa - Barry - Iman - Sofia - Luca - Diana - Kelsey - Bruce

==> flights + people
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- CONCLUSÃO > the following people where at the first flight at july 29th: The destination was New York City
-- Kenny - Sofia - Taylor - Luca - Kelsey - Edward - Bruce - Doris

==> phone_calls + people
SELECT * FROM phone_calls WHERE duration < 60 AND day = 28;
SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28;
SELECT DISTINCT (people.name) FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE phone_number IN (SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28);
SELECT DISTINCT (people.name) FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE duration < 60 AND day = 28);
-- CONCLUSÃO > callers names on july 28th: Kenny, Sofia, Benista, Diana, Kelsey, Bruce, Carina.
--           > receiver names on july 28th: James, Larry, Anna, Jack, Melissa, Jacqueline, Philip, Robin, Doris




==> people + atm_transactions + bank_accounts + passengers
SELECT people.name FROM people JOIN bank_accounts ON
people.id = bank_accounts.person_id WHERE account_number IN
(SELECT account_number FROM atm_transactions WHERE day = 28 AND
atm_location = "Leggett Street" and transaction_type = "withdraw") AND
passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- CONCLUSÃO > the following people withdraw money from ATM and were at the first flight of july 29th:
--          <> Bruce . Kenny . Luca . Taylor

==> people + phone_calls + passengers
SELECT DISTINCT (people.name) FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28)
AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-- CONCLUSÃO > the following people were at the first flight on july 29 and called someone
-- for less than a minute on july 28:
--           > Kenny, Sofia, Taylor, Kelsey, Bruce


==> people + phone_calls + passengers + license_plate
SELECT DISTINCT (people.name) FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28)
AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE month = 7
AND day = 28 AND hour = 10 AND minute > 14 AND minute < 35);
-- CONCLUSÃO > Sofia, Kelsey, Bruce


==> people + atm_transactions + bank_accounts + passengers + phone_calls
SELECT people.name
FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id
WHERE account_number IN
(SELECT account_number FROM atm_transactions WHERE day = 28
AND atm_location = "Leggett Street" and transaction_type = "withdraw")
AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
AND phone_number IN (SELECT caller FROM phone_calls WHERE duration < 60 AND day = 28);
-- CONCLUSÃO > Bruce, Kenny, Taylor


==> airport > destination city
SELECT city FROM airports WHERE id IN
(SELECT destination_airport_id FROM flights WHERE year = 2021 AND month = 7 AND day = 29
    ORDER BY hour, minute ASC LIMIT 1);
-- CONCLUSÃO > Destination : New York City

==> license_plate + atm_transaction + phone_calls + passengers
SELECT name FROM people
WHERE people.license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25)
AND people.id IN (
    SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28
    AND transaction_type = "withdraw"
    AND atm_transactions.atm_location = "Leggett Street")
AND people.phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28
    AND duration < 60)
AND people.passport_number IN (
    SELECT passport_number FROM passengers
    WHERE flight_id IN (
        SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29
        ORDER BY hour, minute ASC LIMIT 1));
-- CONCLUSÃO > Bruce



SELECT name FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28
    AND caller = (SELECT phone_number FROM people WHERE name = "Bruce"
    )
    AND duration < 60
);
-- CONCLUSÃO > Robin