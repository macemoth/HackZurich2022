import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

class Summarizer():

    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model_name = 'google/pegasus-xsum'
        self.tokenizer = PegasusTokenizer.from_pretrained(model_name)
        self.summarizer_model = PegasusForConditionalGeneration.from_pretrained(model_name).to(self.device)

    def summarize(self, text):
        batch = self.tokenizer([text], truncation=True, padding='longest', return_tensors="pt").to(self.device)
        translated = self.summarizer_model.generate(**batch)
        return self.tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

if __name__ == "__main__":
    text = "This study aims to assess coronavirus disease 2019 (COVID-19) surveillance methods, health resources, vaccination coverage and income stratification and quantify burdens of disease and death in children and adolescents in the Caribbean. The investigation was a descriptive, cross-sectional study that included 15 Caribbean countries/territories and utilized surveys and secondary data sources. Quarantine and isolation measures were robust and surveillance strategies were similar. Pediatric specialists were available across the region, but few had designated pediatric hospitals or high-dependency units. There were more cases in children on islands with larger populations. Compared to high-income countries/territories, upper and lower middle-income countries/territories had higher disease burdens, fewer doctors and nurses per 1 000 population, lower bed capacities, and lower vaccination coverage. Child and adolescent cases ranged from 0.60% to 16.9%, compared with a global case rate of 20.2% in 2021. By August 2021 there were 33 deaths among children from Haiti, Jamaica, Trinidad and Tobago, and Barbados. The respective case fatality rates for 0–9-year-olds and 10–19-year-olds were 2.80 and 0.70 in Haiti, 0.10 and 0.20 in Jamaica, and 0.00 and 0.14 in Trinidad, compared with 0.17 and 0.1 globally. Overall COVID-19 incidence and mortality in children were consistent with global estimates. Limited resources have been offset by availability of pediatricians across the region, and minimally direct effects on children. Prioritization of admission of specific at-risk groups, training of first responders and vaccination campaigns targeting pregnant women and vulnerable children and adolescents could benefit countries with low vaccine coverage rates and limited resources."
    summariser = Summarizer()
    print(summariser.summarize(text))