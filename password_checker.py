#!/usr/bin/env python3
# password checker - prodigy task 3
# checks length, upper, lower, digit, special char and gives a score

import argparse
import getpass
import string
import sys


def check_password(pw):
    if pw is None:
        pw = ""
    pw = str(pw)

    n = len(pw)
    long8 = n >= 8
    long12 = n >= 12
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for c in pw:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        if c in string.punctuation:
            has_special = True

    score = 0
    if long8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 1:
        rating = "Weak"
    elif score <= 3:
        rating = "Moderate"
    elif score == 4:
        rating = "Strong"
    else:
        rating = "Very Strong"

    tips = []
    if not long8:
        tips.append("use at least 8 characters (12+ is better)")
    elif not long12:
        tips.append("good length, 12+ is even better")
    else:
        tips.append("good length (12+)")
    if not has_upper:
        tips.append("add an uppercase letter (A-Z)")
    if not has_lower:
        tips.append("add a lowercase letter (a-z)")
    if not has_digit:
        tips.append("add a number (0-9)")
    if not has_special:
        tips.append("add a special character like !@#$")
    if score == 5:
        tips.append("nice, meets all checks")

    return {
        "password_length": n,
        "has_min_length_8": long8,
        "has_length_bonus_12": long12,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special,
        "score": score,
        "max_score": 5,
        "rating": rating,
        "feedback": tips,
    }


def show(result):
    print("Score : " + str(result["score"]) + "/" + str(result["max_score"]))
    print("Rating: " + result["rating"])
    print("length=" + str(result["password_length"]))
    print("Feedback:")
    for t in result["feedback"]:
        print("  - " + t)


def main(argv=None):
    p = argparse.ArgumentParser(description="password strength checker")
    p.add_argument("--password", default=None)
    a = p.parse_args(argv)

    if a.password is not None:
        print("note: --password shows up in shell history, use interactive mode for real passwords", file=sys.stderr)
        pw = a.password
    else:
        try:
            pw = getpass.getpass("enter password: ")
        except (EOFError, KeyboardInterrupt):
            print("\ncancelled")
            return 1

    show(check_password(pw))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
