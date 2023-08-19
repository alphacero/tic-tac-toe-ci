from typing import Optional
from beanie import Document

from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List


class GameMovements(BaseModel):
    board_position: int
    player: str


class Game(Document):
    id: UUID = Field(default_factory=uuid4)
    player1_id: UUID = Field(...)
    player2_id: UUID = Field(...)
    board_size: int = Field(...)
    movements: Optional[List[GameMovements]]

    class Settings:
        name = "games"
