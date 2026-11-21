def fetch_account(database, account_id):
    query = f"SELECT * FROM accounts WHERE id = '{account_id}'"
    return database.execute(query).fetchone()

def can_read_all_accounts(request):
    return request.headers.get("X-Role") == "admin"
