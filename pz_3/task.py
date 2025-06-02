import datetime as dt
import sqlite3
from typing import Any

DB_NAME = "security_events.db"


def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def register_event_source(name: str, location: str, source_type: str) -> None:
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO EventSources (name, location, type)
            VALUES (?, ?, ?);
        """,
            (name, location, source_type),
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print("Error adding source:", e)
    finally:
        conn.close()


def register_event_type(type_name: str, severity: str) -> None:
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO EventTypes (type_name, severity)
            VALUES (?, ?);
        """,
            (type_name, severity),
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print("Error adding event type:", e)
    finally:
        conn.close()


def log_security_event(
    source_id: int,
    event_type_id: int,
    message: str,
    ip_address: str | None = None,
    username: str | None = None,
) -> None:
    conn = connect_db()
    cursor = conn.cursor()
    timestamp = dt.datetime.now(tz=dt.UTC)
    cursor.execute(
        """
        INSERT INTO SecurityEvents (timestamp, source_id, event_type_id, message, ip_address, username)
        VALUES (?, ?, ?, ?, ?, ?);
    """,
        (timestamp, source_id, event_type_id, message, ip_address, username),
    )
    conn.commit()
    conn.close()


def get_login_failed_last_24h() -> list[Any]:
    conn = connect_db()
    cursor = conn.cursor()
    since = dt.datetime.now(tz=dt.UTC) - dt.timedelta(days=1)
    cursor.execute(
        """
        SELECT SecurityEvents.*, EventSources.name AS source_name
        FROM SecurityEvents
        JOIN EventTypes ON SecurityEvents.event_type_id = EventTypes.id
        JOIN EventSources ON SecurityEvents.source_id = EventSources.id
        WHERE EventTypes.type_name = 'Login Failed' AND timestamp >= ?
        ORDER BY timestamp DESC;
    """,
        (since,),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def detect_brute_force() -> list[Any]:
    conn = connect_db()
    cursor = conn.cursor()
    since = dt.datetime.now(tz=dt.UTC) - dt.timedelta(hours=1)
    cursor.execute(
        """
        SELECT ip_address, COUNT(*) as fail_count
        FROM SecurityEvents
        JOIN EventTypes ON SecurityEvents.event_type_id = EventTypes.id
        WHERE EventTypes.type_name = 'Login Failed' AND timestamp >= ?
        GROUP BY ip_address
        HAVING fail_count > 5;
    """,
        (since,),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def get_critical_events_last_week() -> list[Any]:
    conn = connect_db()
    cursor = conn.cursor()
    since = dt.datetime.now(tz=dt.UTC) - dt.timedelta(weeks=1)
    cursor.execute(
        """
        SELECT EventSources.name AS source_name, COUNT(*) AS event_count
        FROM SecurityEvents
        JOIN EventTypes ON SecurityEvents.event_type_id = EventTypes.id
        JOIN EventSources ON SecurityEvents.source_id = EventSources.id
        WHERE EventTypes.severity = 'Critical' AND timestamp >= ?
        GROUP BY EventSources.name
        ORDER BY event_count DESC;
    """,
        (since,),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def search_events_by_keyword(keyword: str) -> list[Any]:
    conn = connect_db()
    cursor = conn.cursor()
    pattern = f"%{keyword}%"
    cursor.execute(
        """
        SELECT SecurityEvents.*, EventSources.name AS source_name, EventTypes.type_name
        FROM SecurityEvents
        LEFT JOIN EventSources ON SecurityEvents.source_id = EventSources.id
        LEFT JOIN EventTypes ON SecurityEvents.event_type_id = EventTypes.id
        WHERE message LIKE ?
        ORDER BY timestamp DESC;
    """,
        (pattern,),
    )
    results = cursor.fetchall()
    conn.close()
    return results


def main() -> None:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM EventSources WHERE name = ?", ("Test_Firewall",))
    row = cursor.fetchone()
    if row:
        source_id = row[0]
        print("Test event source already exists.")
    else:
        register_event_source("Test_Firewall", "10.10.10.10", "Firewall")
        cursor.execute("SELECT id FROM EventSources WHERE name = ?", ("Test_Firewall",))
        source_id = cursor.fetchone()[0]
        print("Test event source added.")

    cursor.execute("SELECT id FROM EventTypes WHERE type_name = ?", ("Test Event",))
    row = cursor.fetchone()
    if row:
        event_type_id = row[0]
        print("Test event type already exists.")
    else:
        register_event_type("Test Event", "Informational")
        cursor.execute("SELECT id FROM EventTypes WHERE type_name = ?", ("Test Event",))
        event_type_id = cursor.fetchone()[0]
        print("Test event type added.")

    conn.close()

    log_security_event(source_id, event_type_id, "This is a test security event", "10.10.10.10", "tester")
    print("Test security event logged.")

    print("\nLogin Failed last 24h:")
    failed = get_login_failed_last_24h()
    if failed:
        for event in failed:
            ts = event[1]
            msg = event[5]
            print(f"{ts}: {msg}")
    else:
        print("No 'Login Failed' events found.")

    print("\nIPs with >5 failed logins in last hour:")
    brute = detect_brute_force()
    if brute:
        for ip, count in brute:
            print(f"{ip} - {count} attempts")
    else:
        print("No suspicious IPs found.")

    print("\nCritical events last week by source:")
    critical = get_critical_events_last_week()
    if critical:
        for source, count in critical:
            print(f"{source}: {count} events")
    else:
        print("No critical events found.")

    print("\nEvents containing keyword 'malware':")
    malware = search_events_by_keyword("malware")
    if malware:
        for event in malware:
            ts = event[1]
            msg = event[5]
            print(f"{ts}: {msg}")
    else:
        print("No events found containing 'malware'.")


if __name__ == "__main__":
    main()
