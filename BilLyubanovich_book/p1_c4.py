letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in our {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

print(letter.format(salutation='Sa', name='N', product='Pr',
                    verbed='V', room='R', animals='A', percent='Pe',
                    spokesman='Sp', job_title='J_T', amount='Am'))

# l = 'The {0[thing]} is in the {0[place]}'
# c = {'thing': 'duck', 'place': 'bathtub'}
# print(l.format(c))
