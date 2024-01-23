from finite_state_machine import *

class Dot_2_Fsm:
    def __init__(self, dot_file, fsm):
        self.file = open(dot_file, "r")
        self.fsm = fsm
    
    def __del__(self):
        self.file.close()

    def find_header(self):
        self.file.seek(0)
        line, found = self.file.readline(), False
        while line:
            line = line.split(" ")
            if line[0] == "digraph":
                name=line[1].replace("{","")
                self.fsm.set_name(name=name)
                found = True
                break
            line = self.file.readline()
        return found
    
    def filter_blank_spaces(self, line):
        line = line.split(" ")
        while '' in line:
            line.remove('')
        return line
    
    def find_states(self):
        self.file.seek(0)
        is_state = True
        has_label = False
        line = self.file.readline()
        while line:
            line = self.filter_blank_spaces(line=line)
            for word in line:
                if "->" in word: 
                    is_state = False
                    break    
                elif "label" in word:
                    has_label = True
                
                if is_state == True and has_label == True:
                    if "[" in line[0]:
                        line[0] = line[0][:line[0].find('[')]
                    self.fsm.create_state(name=line[0])
            is_state = True
            has_label = False  
            line = self.file.readline()
    
    def get_next_state_name(self, words, index_arrow):
        if words[index_arrow].find('>') + 1 < len(words[index_arrow]):
            end_next_state = words[index_arrow].find('[')
            if end_next_state == -1:
                return words[index_arrow][words[index_arrow].find('->')+2:]
            else:
                return words[index_arrow][words[index_arrow].find('->')+2:end_next_state]
        else:
            end_next_state = words[index_arrow + 1].find('[')
            if end_next_state != -1: 
                return words[index_arrow + 1][:words[index_arrow + 1].find('[')]
            else:
                return words[index_arrow + 1]
    
    def find_transitions(self):
        self.file.seek(0)
        labelled = True
        index_arrow, index_label = -1, -1
        line = self.file.readline()
        while line:
            words = line
            words = self.filter_blank_spaces(line=words)
            for index_word, word in enumerate(words):
                if "->" in word: 
                    index_arrow = index_word 
                if "label" in word:
                    index_label = index_word

            if index_arrow != -1:
                match index_arrow:
                    case 0:
                        state_name = words[index_arrow][:words[index_arrow].find('->')]
                    case 1:
                        state_name = words[0]

                next_state_name = self.get_next_state_name(words=words, index_arrow=index_arrow) 

                if index_label == -1:
                    next_state_name = next_state_name[:len(next_state_name)-2]
                    labelled = False
                    condition = ''
                else:
                    i = line.find('\"') + 1
                    labelled = True
                    condition = line[i:line[i:].find('\"') + i]
        

                state_created = False
                next_state_created = False
                states = self.fsm.get_states()
                for index_state, aux_state in enumerate(states):
                    if aux_state.get_name() == state_name:
                        state_created = True
                        state_found_in = index_state
                    if aux_state.get_name() == next_state_name:
                        next_state_created = True
                
                if state_created == False:
                    self.fsm.create_state(name=state_name)
                if next_state_created == False:
                    self.fsm.create_state(name=next_state_name)
                    
                states[state_found_in].create_transition(labelled = labelled, next_state_name = next_state_name, condition = condition)

            index_arrow, index_label = -1, -1
            line = self.file.readline()

    def run(self):
        if self.find_header() == True:
            self.find_states()
            self.find_transitions()
        else:
            print("Cannot find a header")