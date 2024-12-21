q4 = {
    "command": "profile_controls",
    "payload": {"action": "change_language", "content": {"language": "en"}},
}
q2 = {
    "command": "robot_controls",
    "payload": {
        "action": "start/stop/pause/settings/schedule",
        "content": {
            "robot_id": 456,
            "user_id": 789,
            "settings": {"speed": 100, "file": "path/to/file"},
            "schedule": {
                "start_time": "2023-01-01 00:00:00",
                "end_time": "2023-01-01 00:00:00",
            },
        },
    },
}

q3 = {
    "command": "authenticate_controls",
    "payload": {
        "action": "login|change_password",
        "content": {
            "username": "admin",
            "organization": "Acme Inc.",
            "password": "secret",
        },
    },
}

q5 = {
    "command": "message_controls",
    "payload": {"action": "send_message", "content": {"message": "Some message"}},
}
