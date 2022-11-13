from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()


class RiskPreferenceMeasureForm01(forms.Form):
    question01_01 = forms.CharField()
    question01_02 = forms.CharField()
    question01_03 = forms.ChoiceField()


class RiskPreferenceMeasureForm02(forms.Form):
    question02_01 = forms.CharField()
    question02_02 = forms.CharField()


class PictureForm(forms.Form):
    label01 = '1. When faced with a major financial decision, are you more concerned about the possible losses or the possible gains?'
    label02 = '2. Investments can go up and down in value, and experts often say you should be prepared to weather a downturn. By how much could the total value of all your investments go down before you would begin to feel uncomfortable?'
    label03 = '3. In addition to whatever you own, you have been given $1,000. You are now asked to choose between:'
    label04 = '4. In addition to whatever you own, you have been given $2,000. You are now asked to choose between:'
    label05 = '5. After the stock market declines significantly, what do you typically do?'
    label06 = '6. Suppose you have saved $500,000 for retirement in a diversified stock portfolio. By what percentage could the total value of your retirement assets drop before you would begin to think about selling your investments and going to cash?'
    label07 = '7. What degree of risk have you taken with your financial decisions in the past?'
    label08 = '8. What degree of risk are you currently prepared to take with your financial decisions?'
    label09 = '9. What degree of risk are you currently prepared to take with your financial decisions?'
    label10 = '10. How do you usually feel about your major financial decisions after you make them?'
    label11 = '11. If you had to invest $500,000 for retirement, which of the following'
    label12 = '12. Compared to others, how would you rate your willingness to take financial risks?'

    CHOICES01 = [(1, "Always the possible losses"),
                 (2, "Usually the possible losses"),
                 (3, "Usually the possible gains"),
                 (4, "Always the possible gains"), ]

    CHOICES02 = [(1, "Any fall in value would make me feel uncomfortable"),
                 (2, "10%"),
                 (3, "20%"),
                 (4, "33%"),
                 (5, "50%"),
                 (6, "More than 50%"), ]

    CHOICES03 = [(1, "A sure gain of $500"),
                 (2, "A 50% chance to gain $1,000 and a 50% chance to gain nothing"), ]

    CHOICES04 = [(1, "A sure gain of $500"),
                 (2, "A 50% chance to gain $1,000 and a 50% chance to gain nothing"), ]

    CHOICES05 = [(1, "Always buy lower-risk assets"),
                 (2, "Mostly buy lower-risk assets"),
                 (3, "Mostly buy higher - risk assets"),
                 (4, "Always buy higher-risk assets"), ]

    CHOICES06 = [(1, "A 10% drop (retirement assets drop $50,000 to a value of $450,000)"),
                 (2, "A 20% drop (retirement assets drop $100,000 to a value of $400,000)"),
                 (3, "A 30% drop (retirement assets drop $150,000 to a value of $350,000)"),
                 (4, "A 40% drop (retirement assets drop $200,000 to a value of $300,000)"),
                 (5, "A 50% drop (retirement assets drop $250,000 to a value of $250,000)"), ]

    CHOICES07 = [(1, "Very small"),
                 (2, "Small"),
                 (3, "Medium"),
                 (4, "Large"),
                 (5, "Very large"), ]

    CHOICES08 = [(1, "Very small"),
                 (2, "Small"),
                 (3, "Medium"),
                 (4, "Large"),
                 (5, "Very large"), ]

    CHOICES09 = [(1, "Very small"),
                 (2, "Small"),
                 (3, "Medium"),
                 (4, "Large"),
                 (5, "Very large"), ]

    CHOICES10 = [(1, "Very pessimistic"),
                 (2, "Somewhat pessimistic"),
                 (3, "Somewhat optimistic"),
                 (4, "Very optimistic"), ]

    CHOICES11 = [(1, "70% in low-risk investments, 30% in medium-risk investments,0% in high-risk investments"),
                 (2, "50% in low-risk investments, 20% in medium-risk investments,30% in high-risk investments"),
                 (3, "30% in low-risk investments, 20% in medium-risk investments,50% in high-risk investments"),
                 (4, "0% in low-risk investments, 30% in medium-risk investments,70% in high-risk investments"), ]

    CHOICES12 = [(1, "Extremely low risk taker"),
                 (2, "Very low risk taker"),
                 (3, "Low risk taker"),
                 (4, "Average risk taker"),
                 (5, "High risk taker"),
                 (6, "Very high risk taker"),
                 (7, "Extremely high risk taker"), ]

    question01 = forms.ChoiceField(choices=CHOICES01, widget=forms.RadioSelect, label=label01)
    question02 = forms.ChoiceField(choices=CHOICES02, widget=forms.RadioSelect, label=label02)
    question03 = forms.ChoiceField(choices=CHOICES03, widget=forms.RadioSelect, label=label03)
    question04 = forms.ChoiceField(choices=CHOICES04, widget=forms.RadioSelect, label=label04)
    question05 = forms.ChoiceField(choices=CHOICES05, widget=forms.RadioSelect, label=label05)
    question06 = forms.ChoiceField(choices=CHOICES06, widget=forms.RadioSelect, label=label06)
    question07 = forms.ChoiceField(choices=CHOICES07, widget=forms.RadioSelect, label=label07)
    question08 = forms.ChoiceField(choices=CHOICES08, widget=forms.RadioSelect, label=label08)
    question09 = forms.ChoiceField(choices=CHOICES09, widget=forms.RadioSelect, label=label09)
    question10 = forms.ChoiceField(choices=CHOICES10, widget=forms.RadioSelect, label=label10)
    question11 = forms.ChoiceField(choices=CHOICES11, widget=forms.RadioSelect, label=label11)
    question12 = forms.ChoiceField(choices=CHOICES12, widget=forms.RadioSelect, label=label12)



