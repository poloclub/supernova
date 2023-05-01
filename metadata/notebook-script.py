import os
import shutil
import json
import ast
import _thread

### IDENTIFYING ALL INTERACTIVE NOTEBOOKS
def getInteractiveNotebooks(directory):
    for filename in os.listdir(f"notebooks/{directory}"):
        try:
            if filename.endswith('.json'):
                with open(f"notebooks/{directory}/{filename}", 'r') as f:
                    data = json.load(f)
                    cells = data['cells']
                    for cell in cells:
                        if 'outputs' not in cell:
                            break
                        outputs = cell['outputs']
                        for output in outputs:
                            if output['output_type'] == 'display_data' or output['output_type'] == 'execute_result':
                                data = output['data']
                                for key in data:
                                    if key == 'text/html':
                                        html = data[key]
                                        if '</script>' in html:
                                            shutil.copy(f"notebooks/{directory}/{filename}", f"{directory}/script/{filename}")
        except Exception as e:
            print(f"Error {str(filename)}: {str(e)}")

### CONVERTING ALL INTERACTIVE NOTEBOOKS FROM JSON TO IPYNB
def jsonToNotebook(directory):
    for filename in os.listdir(directory + '/script'):
        os.system(f"jupyter nbconvert --to notebook --inplace --ExecutePreprocessor.timeout=600 --output-dir={directory}/script-nb {directory}/script/{filename}")

### COUNTING THE NUMBER OF INTERACTIVE NOTEBOOKS
def countInteractive(directory):
    countInteractive = len(os.listdir(directory + '/script')) // 2
    countTotal = len(os.listdir('notebooks/' + directory))
    print("Number of interactive notebooks: " + str(countInteractive))
    print("Total number of notebooks: " + str(countTotal))
    print("Percentage of interactive notebooks: " + str((1.0 * countInteractive / countTotal) * 100) + "%")
    with open(f"{directory}/statistics.txt", 'w') as w:
        w.write("Number of interactive notebooks: " + str(countInteractive) + "\n")
        w.write("Total number of notebooks: " + str(countTotal) + "\n")
        w.write("Percentage of interactive notebooks: " + str((1.0 * countInteractive / countTotal) * 100) + "%")

### CONVERTING THE IPYNB FILES TO PYTHON FILES
def notebookToPython(directory):
    if not os.path.exists(f"{directory}/script-py"):
        os.makedirs(f"{directory}/script-py")
    for filename in os.listdir(directory + '/script'):
        if filename.endswith('.ipynb'):
            os.system(f"jupyter nbconvert --to python --output-dir={directory}/script-py {directory}/script/{filename}")

### IDENTIFYING THE SOURCE CODE FOR INTERACTIVE CELLS
def extractSourceCode(directory):
    if not os.path.exists(f"{directory}/script"):
                os.makedirs(f"{directory}/script")
    if not os.path.exists(f"{directory}/source"):
            os.makedirs(f"{directory}/source")
    for filename in os.listdir(f"notebooks/{directory}"):
        try:
            if filename.endswith('.json'):
                with open(f"notebooks/{directory}/{filename}", 'r') as f:
                    data = json.load(f)
                    cells = data['cells']
                    for cell in cells:
                        found = False
                        if 'outputs' not in cell:
                            continue
                        outputs = cell['outputs']
                        for output in outputs:
                            if output['output_type'] == 'display_data' or output['output_type'] == 'execute_result':
                                data = output['data']
                                for key in data:
                                    print(key)
                                    if key == 'text/html':
                                        html = ''.join(data[key])
                                        if '/script' in html:
                                            found = True
                                            print("Found interactive: ", filename)
                                            shutil.copy(f"notebooks/{directory}/{filename}", f"{directory}/script/{filename}")
                        if found:
                            if 'source' in cell:
                                source = ''.join(cell['source'])
                                if len(source) > 0:
                                    with open(f"{directory}/source/{filename[:-5]}.py", 'w') as w:
                                        w.write(source)
        except Exception as e:
            print("Error " + str(filename) + ": " + str(e))

### FOR ALL PYTHON FILES, WRITE A .TXT FILE OF THE IMPORTS
def identifyImports(directory):
    if not os.path.exists(f"{directory}/imports"):
        os.makedirs(f"{directory}/imports")
    for filename in os.listdir(f"{directory}/script-py"):
        try:
            with open(f"{directory}/script-py/{filename}", 'r') as f:
                tree = ast.parse(f.read())
                imports = []
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imports.append(alias.name)
                            if alias.asname is not None:
                                imports.append(alias.asname)
                                imports.append("ALIAS")
                    if isinstance(node, ast.ImportFrom):
                        for alias in node.names:
                            if node.module is not None:
                                imports.append(node.module)
                            imports.append(alias.name)
                            if node.module is not None:
                                imports.append("ALIAS")
                imports.append("END")
                with open(f"{directory}/imports/{filename[:-3]}.txt", 'w') as w:
                    for imp in imports:
                        w.write(imp + '\n')
        except Exception as e:
            print(f"Error{str(filename)}: {str(e)} ")

### CHECK IF THE VARIABLE IN THE LAST LINE OF THE SOURCE CODE IS ONE OF THE IMPORTS
def findModule(directory):
    if not os.path.exists(f"{directory}/source-imports"):
            os.makedirs(f"{directory}/source-imports")
    for filename in os.listdir(f"{directory}/source"):
        try:
            with open(f"{directory}/source/{filename}", 'r') as f:
                lines = [line.strip() for line in f.readlines()]
                lastLine = lines[-1]

                lastLine = lastLine.replace(')', '')
                lastLine = lastLine.replace(']', '')

                lastLine = lastLine.replace('.', ' ')
                lastLine = lastLine.replace(',', ' ')
                lastLine = lastLine.replace('(', ' ')
                lastLine = lastLine.replace('[', ' ')
                lastLine = lastLine.replace('=', ' ')

                lastLine = lastLine.split()
                print('LAST LINE: ', lastLine)

                filePrefix = filename[:-3]

                with open(f"{directory}/imports/{filePrefix}.txt", 'r') as r:
                    imports = r.readlines()
                    imports = [imp.strip() for imp in imports]
                    print("IMPORTS: ", imports)
                    for var in lastLine:
                        var = var.strip()
                        if var in imports:
                            index = imports.index(var)
                            if imports[index+1] == "ALIAS":
                                module = imports[index-1]
                            else:
                                module = var
                            with open(f"{directory}/source-imports/{filePrefix}.txt", 'w') as w:
                                w.write(module)
                            with open("all-modules.txt", 'a') as w:
                                w.write(module + '\n')
        except Exception as e:
            print(f"Error{str(filename)}: {str(e)} ")

## GENERATE A SET OF ALL MODULES
def generateModuleSet():
    lines_seen = set()
    outfile = open("modules-set.txt", "w")
    for line in open("all-modules.txt", "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

## COUNT THE TOTAL NUMBER OF NOTEBOOKS
def countTotalNotebooks(directories):
    total = 0
    for directory in directories:
        files = os.listdir(f"{directory}/source-imports")
        total += len(files)
    return total

## COUNT THE FREQUENCIES OF MODULES
def countFrequencies(directories):
    modules = {}
    for directory in directories:
        for filename in os.listdir(f"{directory}/source-imports"):
            with open(f"{directory}/source-imports/{filename}", 'r') as f:
                module = f.readline().strip()
                if module in modules:
                    modules[module] += 1
                else:
                    modules[module] = 1
    modules = {k: v for k, v in sorted(modules.items(), key=lambda item: item[1], reverse=True)}
    with open("modules-frequencies.txt", 'w') as w:
        for module in modules:
            w.write(module + ": " + str(modules[module]) + '\n')
    
directories = ["gh-1000000-1100000", "gh-1100000-1200000", "gh-1600000-1800000", "gh-24145-40000", "gh-40000000-500000000", "gh-5000000-8000000", "gh-8000000-11000000", "gh-100000-255623", "gh-1300000-1600000", "gh-1800000-2000000", "gh-255623-300000", "gh-400000-500000", "gh-500000-600000", "gh-9058-12000", "gh-1000-1475", "gh-14195-20000", "gh-20000000-30000000", "gh-3000-3187", "gh-40000-45539", "gh-6749-9000", "gh-11000000-15000000", "gh-1475-3000", "gh-2000000-5000000", "gh-3655-6000", "gh-45539-60000", "gh-79521-80000"]

for directory in directories:
    try:
        print("Starting with directory: " + directory)
        shutil.copytree(f"/project/zwang3049/notebooks/{directory}", f"/nvmescratch/david/notebooks/{directory}")
        extractSourceCode(directory)
        jsonToNotebook(directory)
        countInteractive(directory)
        shutil.rmtree(f"notebooks/{directory}")
        notebookToPython(directory)
        identifyImports(directory)
        findModule(directory)
    except:
        pass

generateModuleSet()

countFrequencies(directories)
