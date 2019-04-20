from Scripts import utils
from Scripts import plist

class tool:
    def __init__(self):
        self.plist = None
        self.dir = None
        self.destination = None
        self.destination_data = None
        self.u = utils.Utils("PatchPorter")

    def menu(self):
        self.u.head()
        print("")
        print("1. Select patches.plist")
        print("2. Port patches")
        print("")
        print("Q. Quit")
        print("")
        menu = self.u.grab("Please select an option:  ").lower()
        if not len(menu):
            return
        if menu == "q":
            self.u.custom_quit()
        elif menu == "1":
            self._get_plist()
        elif menu == "2":
            self._patch()
        elif menu == "3":
            self._debug()
        elif menu == "4":
            self._write_test()

    def _patch(self):
        self.u.head("Porting Patches!")
        print("")
        print("This may take a while.")
        print("")

    def _write_test(self):
        


    def _get_plist(self):
        self.u.head("Select Plist")
        print("")
        print("Current: {}".format(self.plist))
        print("")
        print("C. Clear Selection")
        print("M. Main Menu")
        print("Q. Quit")
        print("")
        p = self.u.grab("Please drag and drop the target plist:  ")
        if p.lower() == "q":
            self.u.custom_quit()
        elif p.lower() == "m":
            return
        elif p.lower() == "c":
            self.plist = None
            self.plist_data = None
            return
        
        pc = self.u.check_path(p)
        if not pc:
            self.u.head("File Missing")
            print("")
            print("Plist file not found:\n\n{}".format(p))
            print("")
            self.u.grab("Press [enter] to return...")
            self._get_plist()
        try:
            with open(pc, "rb") as f:
                self.plist = p
                self.plist_data = plist.load(f)
        except Exception as e:
            self.u.head("Plist Malformed")
            print("")
            print("Plist file malformed:\n\n{}".format(e))
            print("")
            self.u.grab("Press [enter] to return...")
            self._get_plist()
    
    def _debug(self): #Hidden debug functionality
        try:
            self.u.head("Debug data!")
            print("")
            #print(self.plist_data)
            #print("")
            print("self.plist_data\n")

            for Comment in self.plist_data["KernelAndKextPatches"]["KernelToPatch"]:
                #print([Comment])        
                #print("")
                #print([Comment][0])
                print("")
                print("Comment:")
                print([Comment][0]["Comment"])
                print("")
                print("Disabled:")
                print([Comment][0]["Disabled"])
                print("")
                print("Find:")
                print([Comment][0]["Find"])
                print("")
                print("MatchOS:")
                print([Comment][0]["MatchOS"])
                print("")
                print("Replace:")
                print([Comment][0]["Replace"])
                print("")
            print("")
            self.u.grab("Press [enter] to return...")
        except Exception as e:
            print(e)
            self.u.grab("Press [enter] to return...")


t = tool()

while True:
    try:
        t.menu()
    except Exception as e:
        print(e)