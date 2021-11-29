
import cx_Freeze

executables = [cx_Freeze.Executable(
    script="snake.py", icon="assets/snek.ico")]

cx_Freeze.setup(
    name="Snake Game",
    options = {"build_exe": { "packages": ["pygame"],
                            "include_files": ["assets"]
    }},
    executables=executables
)