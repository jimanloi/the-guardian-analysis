class GuardianArticle:
    def __init__(self, article_data_from_json):
        self.type = article_data_from_json["type"]
        self.sectionName = article_data_from_json["sectionName"]
        self.webTitle = article_data_from_json["webTitle"]
        self.bodyText = article_data_from_json["fields"]["bodyText"]
        self.date = article_data_from_json.get("webPublicationDate")
        self.pillarName = article_data_from_json.get("pillarName")
        self.webUrl = article_data_from_json.get("webUrl")

    def __repr__(self):
        return f"{self.type} in {self.sectionName} section : {self.webTitle} published at {self.date}"