import os
import glob
import inspect
import gdrive


class Helpers:

    @staticmethod
    def help(args: str):
        print("HELP DOC - Command list of the tool")
        print()
        Helpers.commands()

    @staticmethod
    def commands():
        class_excluded = ["helpers", "login"]
        cmd_labels = []
        path = os.path.dirname(os.path.abspath(__file__))
        for file in glob.glob(os.path.join(path, "*.py")):
            file_name = os.path.splitext(os.path.basename(file))[0]
            if class_excluded.__contains__(file_name):
                continue
            module = getattr(gdrive, file_name)
            class_attr = getattr(module, dir(module)[0])
            class_func = inspect.getmembers(class_attr, inspect.isfunction)
            for func in class_func:
                if func[0] == "__init__" or func[1].__doc__ is None:
                    continue

                cmd_labels.append(func[1].__doc__)

        cmd_labels.sort()
        for cmd in cmd_labels:
            print(cmd)
