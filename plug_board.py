from plug_lead import PlugLead

class Plugboard:
    def __init__(self):
        """initiate a version of the Plug Board
        """
        self.__plugleads = []

    def __find_pluglead(self, mappings):
        """returns first pluglead from plugboard with at least one matching mapped value
            params:
                mappings: list
        """
        if len(self.__plugleads) == 0:
            return None

        return next((pl for pl in self.__plugleads for m in pl.mapping if m in mappings), None)

    def add(self, plug_lead):
        """add a plug lead mapping
            params:
                plug_lead: PlugLead
        """
        if type(plug_lead) != PlugLead:
            raise ValueError("Plug Lead should be of type PlugLead")
        if self.__find_pluglead(plug_lead.mapping) != None:
            raise ValueError("Mapping already exists for this letter")

        self.__plugleads.append(plug_lead)

    def encode(self, char):
        """find and encode (swap) mapping value if present, else return itseld
            params:
                char: string
        """
        if type(char) != str or len(char) != 1:
            raise ValueError("Character to encode should be single character of type string")

        matched = self.__find_pluglead(char)
        if matched != None:
            return matched.encode(char)
        else:
            return char

    def status(self):
        """print status of plug board
        """
        for pl in self.__plugleads:
            print(f"pluglead: {pl.mapping}")
        print("-----------------------")
        