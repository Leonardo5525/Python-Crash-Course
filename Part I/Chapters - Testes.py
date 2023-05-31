def build_car(many, model, **info):
    profile = {}
    profile['Manifacture'] = many
    profile['Model'] = model
    for key, value in info.items():
        profile[key] = value
    return profile

print(build_car('fiat', 'GM', location='Marília',color='blue'))