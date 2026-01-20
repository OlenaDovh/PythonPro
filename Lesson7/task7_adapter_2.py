class MessageSender:
    """Interface for sending messages via various channel"""

    def send_message(self, message: str) -> None:
        """Sends message"""
        pass


class SMSService:
    """Sends sms"""

    def send_sms(self, phone_number: str, message: str) -> None:
        """Sends sms message to a phone number"""
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    """Sends email"""

    def send_email(self, email_address: str, message: str) -> None:
        """Sends email to the specified email address"""
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    """Sends push"""

    def send_push(self, device_id: str, message: str) -> None:
        """Send a push notification to a device"""
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Adapter for SMSService to send messages via sms"""

    def __init__(self, sms_service: SMSService, phone_number: str) -> None:
        """Initializes the sms adapter"""
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """Sends message via sms"""
        self.sms_service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    """Adapter for EmailService to send messages via email"""

    def __init__(self, email_service: EmailService, email_address: str) -> None:
        """Initializes the email adapter"""
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """Sends message via email"""
        self.email_service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    """Adapter for PushService to send messages via push"""

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """Initializes the push adapter"""
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """Sends message via push"""
        self.push_service.send_push(self.device_id, message)


sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+380123456789")
email_adapter = EmailAdapter(email_service, "user@example.com")
push_adapter = PushAdapter(push_service, "device123")

message = "Привіт! Це тестове повідомлення."

sms_adapter.send_message(message)
email_adapter.send_message(message)
push_adapter.send_message(message)
