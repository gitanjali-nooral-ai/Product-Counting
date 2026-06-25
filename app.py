import subprocess
import sys



def start_dashboard():


    subprocess.run(

        [

            sys.executable,

            "-m",

            "streamlit",

            "run",

            "dashboard/streamlit_app.py"

        ]

    )



if __name__=="__main__":


    start_dashboard()