class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        parsed = []

        for i, tx in enumerate(transactions):
            name, time, amt, city = tx.split(",")
            parsed.append((name, int(time), int(amt), city, i))

        
        bad = [False] * len(transactions)

        hm = defaultdict(list)


        for name, time, amt, city, idx in parsed:
            if amt >1000:
                bad[idx] = True
            

            for t in range(max(0,time-60), min(1000, time+60)+1):
                for prev_name, prev_city, prev_idx in hm[t]:
                    if prev_city != city and prev_name == name:
                        bad[idx] = True
                        bad[prev_idx] = True


            hm[time].append((name, city, idx))


        return [transactions[i] for i in range(len(transactions)) if bad[i] ]
        