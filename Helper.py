class DataHelper:
    requiredParameterKeys = ["dl", "dt", "dh", "dp"]

    def getRequiredParameters(self, params):
        requiredParameters = {}
        for key in self.requiredParameterKeys :
            if key in params:
                requiredParameters[key] = params[key]
            else:
                requiredParameters[key] = ""
        return requiredParameters

    def getParameters(self, pathParameters):
        params = {}
        parameters = pathParameters.split("&")
        for pathParameter in parameters:
            keyValues = pathParameter.split("=")
            params[keyValues[0]] = keyValues[1]
        return params

    def getRequiredDataFrom(self, answer):
        urlAndParam = {}
        for entry in answer["log"]["entries"]:
            url = str(entry["request"]["url"])
            if (url.__contains__("google-analytics.com/r/collect")) or (url.__contains__("dc.optimahub.com")):
                print("Task 2 Completed")
                if (url.__contains__("google-analytics.com/r/collect")):
                    onlyUrl = url[0:url.index("?")]
                    urlAndParam = self.getRequiredParameters(self.getParameters(url[url.index("?")+1:]))
                    urlAndParam["url"] = onlyUrl
                    break
        return urlAndParam