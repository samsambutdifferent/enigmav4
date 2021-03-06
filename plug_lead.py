

class PlugLead:
    def __init__(self, mapping):
        if type(mapping) != str:
            raise ValueError('Mapping value should be a string')
        if len(mapping) != 2:
            raise ValueError('Two mapping values should be passed in')
        if mapping[0] == mapping[1]:
            raise ValueError('Mapping values should be unique')

        self.mapping = mapping
        
    def encode(self, character):
        if character in self.mapping:
            return ''.join([c for c in self.mapping if c != character])
        else:
            return character
        