class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.expiry = OrderedDict()
        self.life = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        self.expiry[tokenId] = self.life + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        if tokenId in self.expiry:
            self.expiry.move_to_end(tokenId) # necessary to move to the end to keep expiry time in ascending order.
            self.expiry[tokenId] = self.life + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evict_expired(currentTime)
        return len(self.expiry)    
    
    def evict_expired(self, currentTime: int) -> None:
        while self.expiry and next(iter(self.expiry.values())) <= currentTime:
            self.expiry.popitem(last=False)
