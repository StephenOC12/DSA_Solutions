# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.ind = int(query[1]) if self.type == 'check' else None
        self.s = query[1] if self.type != 'check' else None

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for x in range(bucket_count)]

    def _hash_func(self, s):
        ans = sum((ord(c) * self._multiplier ** i) for i, c in enumerate(s))
        return ((ans % self._prime) + self._prime) % self._prime % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(reversed(self.buckets[query.ind]))
        else:
            hashed_value = self._hash_func(query.s)
            bucket = self.buckets[hashed_value]
            query_in_bucket = query.s in bucket
            if query.type == 'find':
                self.write_search_result(query_in_bucket)
            elif query.type == 'add':
                if not query_in_bucket:
                    bucket.append(query.s)
            else:
                if query_in_bucket:
                    bucket.remove(query.s)

    def process_queries(self):
        n = int(input())
        for x in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()