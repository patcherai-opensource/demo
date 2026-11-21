"""Test-only example for a pull-request security review; not imported or deployed."""

def lookup_test_record(db, user_id):
    # Demonstration of a deliberately unsafe query; never call this function.
    return db.execute(f"SELECT * FROM test_records WHERE id = {user_id}")
