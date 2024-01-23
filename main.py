import argparse
import subprocess
import os
import sys
sys.path.append("src")
from finite_state_machine import *
from dot_2_fsm import *
from fsm_2_vhd import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser("\n--dot, -d".ljust(15) + "Directory containing .dot files\n\n--compile, -c".ljust(16) + " Directory containing .compile files\n\n")
    parser.add_argument("--dot", "-d")
    parser.add_argument("--compile", "-c")

    args = parser.parse_args()
    
    if args.compile:
        compile_result = subprocess.run(args.compile, shell=True, capture_output=True, text=True)
        if compile_result.returncode != 0:
            print("Erro ao executar: ", args.compile)
    
    if args.dot:
        dot_files_dir = args.dot
    else:
        dot_files_dir = "dot/"
    try:
        for dot_file_name in os.listdir(dot_files_dir):
            try:
                os.mkdir("vhd")
            except:
                pass
            vhd_file_name = "vhd/" + dot_file_name[:dot_file_name.find(".")] + ".vhd"

            fsm = Finite_State_Machine(name="")
            parser = Dot_2_Fsm(dot_file=dot_files_dir + dot_file_name,  fsm=fsm)
            parser.run()

            writer = Fsm_2_Vhd(vhd_file=vhd_file_name, fsm=fsm)
            writer.run()
    except FileNotFoundError:
        print("Directory not found: ", dot_files_dir)
