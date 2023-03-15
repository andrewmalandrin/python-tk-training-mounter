from enum import Enum

class TrainingColumnsEnum(str, Enum):
    training = 'Treino'
    muscle = 'Músculo'
    exercise = 'Exercício'
    sets = 'Séries'
    reps = 'Repetições'
