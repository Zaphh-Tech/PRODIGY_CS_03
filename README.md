# My Prodigy Task 3 - Password Checker

Checks how strong a password is. Gives score out of 5 + tips on what to add.

Points for: 8+ chars, uppercase, lowercase, number, special char.

## how to run

```
python3 password_checker.py
```
It hides what you type. Or for quick testing:
```
python3 password_checker.py --password "Password1"
```

Example:
```
Score : 4/5
Rating: Strong
```

## files

- `password_checker.py` - `check_password()` does the checking, returns score/rating/feedback

Only uses python builtins, no pip install needed. Everything stays local, nothing sent anywhere.
