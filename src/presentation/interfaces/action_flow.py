from src.presentation.interfaces.action import Action
from dataclasses import dataclass
from abc import ABC


@dataclass
class ActionFlow(Action, ABC):
    title: str
        
