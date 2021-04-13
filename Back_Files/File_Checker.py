from pathlib import Path
import os
def check_common_files_existence():
    if not(Path('chatbot_model.h5').is_file()) or not(Path('words.pkl').is_file()) or not(Path('classes.pkl').is_file()):
        print("missing some Model files")
        print("retraining the model")
        os.chdir(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "Back_Files"))
        os.system('python train_chatbot.py')
    os.chdir(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "Model"))    
    if not(Path('intents.json').is_file()):
        print ("missing intents.json")
        