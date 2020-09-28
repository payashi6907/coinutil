    def get_all_asset_balance(self, **params):
        #added by Takumi
        res = self.get_account(**params)
        all_balances = []
        if "balances" in res:
            for bal in res['balances']:
                if float(bal["free"]) > 0  or float(bal["locked"]) > 0:
                    all_balances.append(bal)

        return all_balances
    
    def get_all_pools(self, **params):
        #added by Takumi
        return self._request_margin_api('get', 'bswap/pools', True, data=params)

    def get_pool_liquidity(self, **params):
        #added by Takumi
        #param = poolId
        return self._request_margin_api('get', 'bswap/liquidity', True, data=params)

    def get_swap_price(self, **params):
        #added by Takumi
        #param = quoteAsset, baseAsset, quoteQty<5000
        return self._request_margin_api('get', 'bswap/quote', True, data=params)