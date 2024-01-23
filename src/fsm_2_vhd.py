from finite_state_machine import *

class Fsm_2_Vhd:
    TAB = " "*3
    def __init__(self, vhd_file, fsm):
        self.fsm = fsm
        self.file = open(vhd_file, "w")
        self.main_name = self.fsm.get_name().upper().replace("\n","")
        self.state_name = self.main_name + "_STATE_s"
        self.next_state_name = self.main_name + "_NEXT_STATE_s"
    
    def __del__(self):
        self.file.close()

    def create_signal(self):
        self.file.write("type " + self.main_name + "_t is (")
        states = self.fsm.get_states()
        for i, state in enumerate(states):
            self.file.write(state.get_name())
            if i < len(states) -1:
                self.file.write(", ")
            else: 
                self.file.write(");\n")
        self.file.write("signal " + self.state_name + " : " + self.main_name + "_t;\n")
        self.file.write("signal " + self.next_state_name + " : " + self.main_name + "_t;\n")
        self.file.write("\n")

    def create_synchronous_proc(self):
        self.file.write("p_" + self.main_name + "_SYNCHRONOUS: process()\n")
        self.file.write("begin\n")
        self.file.write(self.TAB + "if () then\n")
        self.file.write(self.TAB*2 + self.state_name + " <= ;\n")
        self.file.write(self.TAB + "elsif () then\n") 
        self.file.write(self.TAB*2 + self.next_state_name + " <= ;\n")
        self.file.write(self.TAB + "end if;\n")
        self.file.write("end process;\n")
        self.file.write("\n")
    
    def create_transitions(self, state):
        transitions = state.get_transitions()
        for index_transition, transition in enumerate(transitions):
            if transition.is_labelled() == False:
                self.file.write(self.TAB*3 + self.next_state_name + " <= " + transition.get_next_state_name() + ";\n")
                continue
            else:
                num_transition = state.get_num_transitions()
                if index_transition == 0:
                    self.file.write(self.TAB*3 + "if (" + transition.get_condition() + ") then\n")
                else:
                    self.file.write(self.TAB*3 + "elsif (" + transition.get_condition() + ") then\n") 
                self.file.write(self.TAB*4 + self.next_state_name + " <= " + transition.get_next_state_name() + ";\n")
                if index_transition != num_transition - 1:
                    continue

            self.file.write(self.TAB*3 + "else\n") 
            self.file.write(self.TAB*4 + self.next_state_name + " <= " + state.get_name() + ";\n")
            self.file.write(self.TAB*3 + "end if;\n")

    def create_combinational_proc(self):
        self.file.write("p_" + self.main_name + "_COMBINATIONAL: process()\n")
        self.file.write("begin\n")
        self.file.write(self.TAB + "case(" + self.state_name + ") is\n")
        states = self.fsm.get_states()
        for state in states:
            self.file.write(self.TAB*2 + "when " + state.get_name() + " =>\n")    
            self.create_transitions(state=state)
            self.file.write("\n")
        self.file.write(self.TAB*2 + "when others =>\n\n")
        self.file.write(self.TAB + "end case;\n")
        self.file.write("end process;\n")
        self.file.write("\n")

    def run(self):
        self.create_signal()
        self.create_synchronous_proc()
        self.create_combinational_proc()