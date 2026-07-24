import sqlite3
# third webhook test
# second webhook test
# testing webhook trigge
# Intentionally hardcoded secret - Gitleaks should flag this
API_KEY = "hardcoded-secret-value-do-not-use-12345"

def get_user(username):
    """Retrieve a user record from the database by their username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        tuple or None: A tuple representing the user record if found, otherwise None."""
    # Intentionally vulnerable to SQL injection - Semgrep/Bandit should flag this
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def calculate_discount(price, percentage):
    """Calculate the final price after applying a percentage discount.

    Args:
        price (float): The original price.
        percentage (float): The discount percentage to apply.

    Returns:
        float: The discounted price."""
    # No docstring, no test - for Docs Agent and Test-Gap Agent to catc
    return price - (price * percentage / 100)

def add_numbers(a, b):
    """Adds two numbers together."""
    return a + b 