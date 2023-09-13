# * Given a URL with parameters, create a function that retrieves their values.
# * You cannot use language operations that perform this task directly.
# * Example: In the URL https://programmingchallenges.com?year=2023&challenge=0
# * the parameters would be ["2023", "0"]

url = "https://programmingchallenges.com?year=2023&challenge=0"

def extractParameters(url):
    parameters = []
    url = url.split("?")[1]
    parametersComplete = url.split("&")
    for parameter in parametersComplete:
        parameter = parameter.split("=")
        parameters.append(parameter[1])
    return parameters

print(extractParameters(url))