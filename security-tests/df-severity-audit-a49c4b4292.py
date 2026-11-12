# Test-only, non-deployed Security Reviewer fixture: df-severity-audit-a49c4b4292
        # This example intentionally models a dangerous SQL injection, and must never be run.

        def find_user_by_untrusted_id(connection, request):
            user_id = request.args["user_id"]  # attacker-controlled input
            sql = "SELECT * FROM users WHERE id = '" + user_id + "'"
            return connection.execute(sql).fetchall()  # SQL injection: use parameter binding instead
        
