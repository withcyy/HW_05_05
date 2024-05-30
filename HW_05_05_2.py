import json

class Survey:
    def __init__(self):
        self.data = {}

    def create_survey(self, survey_name, questions):
        self.data[survey_name] = questions

    def save_responses(self, survey_name, responses):
        if survey_name in self.data:
            if survey_name not in self.data:
                self.data[survey_name] = []
            self.data[survey_name].append(responses)
        else:
            print(f"{survey_name} not found")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)
survey = Survey()

survey.create_survey("Customer Satisfaction Survey", ["Q1. How satisfied are you with our service?", "Q2. Would you recommend our product to others?", "Q3. Any suggestions for improvement?"])
survey.save_responses("Customer Satisfaction Survey", ["Very satisfied", "Yes", "Faster shipping"])

survey.save_to_file("survey_responses.json")
survey.load_from_file("survey_responses.json")

print(survey.data)