from desafio_ibm.users.models import State


def run():
    states = open("data/states.csv")

    for state in states:
        State(name=state.strip()).save()
