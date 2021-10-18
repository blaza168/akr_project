class EndSequenceCollisionException(Exception):
    
    def __init__(self, bytes):
        self.bytes = bytes
