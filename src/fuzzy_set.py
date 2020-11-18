class FuzzySet:

    def __init__(self, d_min, d_max):

        self._domain_min = d_min
        self._domain_max = d_max

        self._step = (d_max - d_min)/100
        self._domain = FuzzySet.set_domain(d_min, d_max)
        self._degree = [0.00]*101

        self.last_degree_value = 0

    @staticmethod
    def set_domain(d_min, d_max):
        step = (d_max - d_min)/100
        domain = [d_min]
        for _ in range(99):
            domain.append(round(domain[-1] + step, 2))

        domain.append(d_max)

        return domain

    def __getitem__(self, x_val):
        return self._adjust_to_set(x_val, 1)

    def __setitem__(self, x_val, degree):
        val = self._adjust_to_set(x_val)
        i = self._domain.index(val)
        self._degree[i] = round(degree, 2)

    @staticmethod
    def create_trapezoidal(domain_min, domain_max, low, mid1, mid2, high):
        t1fs = FuzzySet(domain_min, domain_max)

        low = t1fs._adjust_to_set(low)
        mid1 = t1fs._adjust_to_set(mid1)
        mid2 = t1fs._adjust_to_set(mid2)
        high = t1fs._adjust_to_set(high)

        t1fs._degree = [round(min(max(min(
            (dom-low)/(mid1-low), (high-dom)/(high-mid2)), 0), 1), 2) for dom in t1fs._domain]
        return t1fs

    @staticmethod
    def create_triangular(domain_min, domain_max, low, mid, high):
        t1fs = FuzzySet(domain_min, domain_max)

        low = t1fs._adjust_to_set(low)
        mid = t1fs._adjust_to_set(mid)
        high = t1fs._adjust_to_set(high)

        if mid == low:
            t1fs._degree = [round(max((high - dom)/(high - mid), 0), 2)
                            for dom in t1fs._domain]
        elif mid == high:
            t1fs._degree = [round(max((dom - low)/(mid - low), 0), 2)
                            for dom in t1fs._domain]
        else:
            t1fs._degree = [round(max(min((dom - low)/(mid - low),
                                          (high - dom)/(high - mid)), 0), 2) for dom in t1fs._domain]

        return t1fs

    def _adjust_to_set(self, x_val, dom_type=0):
        search = 0
        for i in range(101):
            search = self._domain[i]
            if search >= x_val:
                break

        return self._degree[i] if dom_type else search

    def min_operator(self, val):

        result = FuzzySet(self._domain_min, self._domain_max)
        result._degree = [min(deg, val) for deg in self._degree]

        return result

    def union(self, f_set):

        result = FuzzySet(self._domain_min, self._domain_max)
        result._degree = [max(deg1, deg2) for deg1, deg2 in zip(self._degree, f_set._degree)]

        return result

    def defuzzify(self, method="COA"):  # Añadir BOA y MOM
        if method == "COA":  # Centoride of Area
            num = sum([deg*dom for deg, dom in zip(self._degree, self._domain)])
            den = sum(self._degree)

            return num/den