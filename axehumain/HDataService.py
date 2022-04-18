class HDataService:

    NS_INF=0
    NS_SUP=4

    PS_INF=5
    PS_SUP=6

    AS_INF=7
    AS_SUP=8

    TS_INF=9
    TS_SUP=10


    def __init__(self, data_list) -> None:
        self.data_list = data_list


    def __calulate_param(self, inf, sup):
        return len([data for data in self.data_list if inf <= float(data) <= sup])


    def calulate_Tr(self):
        return len(self.data_list)


    def calulate_Ns(self):
        return self.__calulate_param(self.NS_INF, self.NS_SUP)


    def calulate_Ps(self):
        return self.__calulate_param(self.PS_INF, self.PS_SUP)


    def calulate_As(self):
        return self.__calulate_param(self.AS_INF, self.AS_SUP)


    def calulate_Ts(self):
        return self.__calulate_param(self.TS_INF, self.TS_SUP)



    def fornat_stats(self, Tr, Ns, Ps, As, Ts):
        return [
            {
                'title': "Nombre total de réponses",
                'notation': 'Tr',
                "value": Tr,
            },
            {
                'title': "Nombre de non satisfaits de la PPD",
                'notation': 'Ns',
                "value": Ns,
            },
            {
                'title': "Nombre de peu satisfaits de la PPD",
                'notation': 'Ps',
                "value": Ps,
            },
            {
                'title': "Nombre d’assez satisfaits de la PPD",
                'notation': 'As',
                "value": As,
            },
            {
                'title': "Nombre de très satisfaits de la PPD",
                'notation': 'Ts',
                "value": Ts,
            }
        ]

