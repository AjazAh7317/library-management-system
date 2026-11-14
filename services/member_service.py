
from models.member import Member


class MemberService:

    def __init__(self, member_repository):
        # Repository is used to store and manage members
        self.member_repository = member_repository

    # Register a new library member
    def register_member(self, member_id: str, name: str, email: str) -> Member:

        # Check that no field is empty
        if not member_id or not member_id.strip():
            raise ValueError("Member ID cannot be empty.")

        if not name or not name.strip():
            raise ValueError("Name cannot be empty.")

        if not email or not email.strip():
            raise ValueError("Email cannot be empty.")

        # Basic email validation
        if "@" not in email:
            raise ValueError("Please provide a valid email address.")

        # Create a new member
        member = Member(member_id, name, email)

        # Save the member in the repository
        self.member_repository.add(member)

        return member

    # Find a member using their ID
    def get_member(self, member_id: str) -> Member:

        member = self.member_repository.get(member_id)

        if member is None:
            raise ValueError(f"Member '{member_id}' was not found.")

        return member

    # Get the list of all registered members
    def list_members(self):
        return self.member_repository.list_all()
