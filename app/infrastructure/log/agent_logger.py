import json
import requests


class AgentLogger:

    def __init__(self):
        self.log_api_url = "https://vibeappop.saa.ai/EnterpriseLogging/api/Logs/TenderAgentLog"

    def log_event(
        self,
        agent_name,
        message,
        event_type,
        source_module,
        is_success,
        payload=None,
        correlation_id=""
    ):

        log_payload = {
            "agentName": agent_name,
            "message": message,
            "eventType": event_type,
            "sourceModule": source_module,
            "isSuccess": is_success,
            "durationMs": 0,
            "payloadJson": json.dumps(payload or {}),
            "correlationId": correlation_id
        }

        try:
            response = requests.post(
                url=self.log_api_url,
                json=log_payload,
                timeout=10
            )

            print(f"Log Sent | Status={response.status_code}")

            print(f"Response={response.text}")

        except requests.exceptions.RequestException as e:

            print(f"Logging Error: {str(e)}")