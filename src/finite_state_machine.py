class Finite_State_Machine:
    def __init__(self, name = "") -> None:
        self.name = name
        self.states = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_states(self):
        return self.states

    def create_state(self, name):
        self.states.append(State(name=name))
    
    def add_state(self, state):
        self.states.append(state)

class State:
    def __init__(self, name = "", num_transitions = 0):
        self.name = name
        self.num_transitions = num_transitions
        self.transitions = []
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_transitions(self):
        return self.transitions
    
    def get_num_transitions(self):
        return self.num_transitions
    
    def create_transition(self, labelled = False, next_state_name = None, condition = ""):
        self.transitions.append(Transition(labelled=labelled, condition=condition, next_state_name=next_state_name))
        if labelled == True:
            self.num_transitions += 1

class Transition:
    def __init__(self, labelled = False, next_state_name = None, condition = ""):
        self.labelled = labelled
        self.condition = condition
        self.next_state_name = next_state_name

    def is_labelled(self):
        return self.labelled

    def get_condition(self):
        return self.condition

    def set_condition(self, condition):
        self.condition = condition
    
    def get_next_state_name(self):
        return self.next_state_name

    def set_next_state_name(self, next_state_name):
        self.next_state_name = next_state_name