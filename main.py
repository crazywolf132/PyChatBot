import Tkinter as tk
import ttk as ttk
import ScrolledText
import time
import urllib2

from chatterbot import ChatBot

class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        '''
        Create & set window variables.
        '''
        tk.Tk.__init__(self, *args, **kwargs)

	# Get the datebase file
	#downloadReq = urllib2.urlopen('SET_ME_TO_A_URL')
	#databaseContent = downloadReq.read()

	# Write the file
	#databaseFile = open('../database.db', 'w')
	#databaseFile.write(databaseContent)
	#databaseFile.close()

        self.chatbot = ChatBot("No Output",
            storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
            logic_adapters=[
                "chatterbot.adapters.logic.ClosestMatchAdapter"
            ],
            input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
            database="../database.db"
        )

        self.title("Samantha")

        self.initialize()

    def initialize(self):
        '''
        Set window layout.
        '''
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    def get_response(self):
        '''
        Get a response from the chatbot &
        display it.
        '''
        user_input = self.usr_input.get()
	if user_input == "":
		exit()

        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)
	responseTxt = str(response.text)

	if len(responseTxt) > 0 and (responseTxt[len(responseTxt) - 1] != "!" or responseTxt[len(responseTxt) - 1] != "?"):
		responseTxt = responseTxt + "."

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)

gui_example = TkinterGUIExample()
gui_example.mainloop()
