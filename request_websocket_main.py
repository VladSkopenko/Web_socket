from schemas.request_schemas.request_schema import RequestSchema

q3 = {
    "command": "authenticate_controls",
    "payload": {
        "action": "change_password", #or "login",
        "content": {
            "username": "admin",
            "organization": "Acme Inc.",
            "user_id": 789,
            "password": "secret",
        },
    },
}


class RequestWebSocket:

    @staticmethod
    def generate_request_data(data: dict):
        requests_body = {
            "command": data.get("command"),
            "payload": data.get("payload"),
        }
        RequestSchema.model_validate(requests_body)
        return requests_body


if __name__ == "__main__":
    a = RequestWebSocket.generate_request_data(q3)
    print(type(a))
