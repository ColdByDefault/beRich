from flask import flash

# validation functions
def username_valid(username):
    
    if len(username) < 4:
        flash("Der Benutzername muss mindestens 5 Zeichen lang sein!", "info")
        return False
    elif len(username) > 13:
        flash("Der Benutzername darf nicht länger als 12 Zeichen sein!", "info")
        return False
    return True

def password_valid(password, confirm_password):
    is_valid = True  # return only one Boolean in order to show multi-error msgs
    if password != confirm_password:
        flash("Die Passwörter stimmen nicht überein. Bitte versuchen Sie es erneut.", "error")
        is_valid = False

    if len(password) < 7:
        flash("Das Passwort muss mindestens 8 Zeichen lang sein!", "info")
        is_valid = False
    elif len(password) > 16:
        flash("Das Passwort darf höchstens 16 Zeichen lang sein!", "info")
        is_valid = False

    symbols_list = "!§$%&/()*@€#'_-.;,?"
    is_lower = any(character.islower() for character in password)
    is_upper = any(character.isupper() for character in password)
    has_symbol = any(character in symbols_list for character in password)
    is_digit = any(character.isdigit() for character in password)

    if not (is_lower and is_upper and has_symbol and is_digit):
        flash("Das Passwort muss Zahlen, mindestens einen Großbuchstaben und ein Sonderzeichen enthalten!", "info")
        is_valid = False

    return is_valid
