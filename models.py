from dataclasses import dataclass


@dataclass
class UserData:
    id_: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @staticmethod
    def from_json(json) -> "UserData":
        return UserData(
            id_=json["id"],
            email=json["email"],
            first_name=json["first_name"],
            last_name=json["last_name"],
            avatar=json["avatar"],
        )
