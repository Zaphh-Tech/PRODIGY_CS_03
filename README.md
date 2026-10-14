# PRODIGY_CS_03

A password strength checker written in Python, built for Task 3 of the Prodigy InfoTech
Cyber Security internship.

It looks at a password and rates it out of 5, then tells you what it's missing.

## What it does

- Scores a password on five checks: length (8+), uppercase, lowercase, number, special char
- Gives a rating: Weak / Moderate / Strong / Very Strong
- Prints feedback on what to add to make it stronger
- Reads the password hidden (getpass) by default, so it isn't shown on screen

## Setup

No install needed, just Python 3. Everything runs locally — nothing is sent anywhere.

## How to run

```bash
# hidden prompt (recommended)
python3 password_checker.py

# quick test with an inline password
python3 password_checker.py --password "P@ssw0rd123!"
```

## Example output

```
$ python3 password_checker.py --password "P@ssw0rd123!"
Score : 5/5
Rating: Very Strong
length=12
Feedback:
  - good length (12+)
  - nice, meets all checks
```

## Files

- `password_checker.py` — `check_password()` runs the checks and returns the score, rating and feedback.
