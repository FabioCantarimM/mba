capitais_brasil = {
    'AC': {'state': 'Acre', 'capital': 'Rio Branco', 'lat': -9.9712, 'lon': -67.8249, 'pop': 364_756, 'area': 8_834.942},
    'AL': {'state': 'Alagoas', 'capital': 'Maceió', 'lat': -9.6658, 'lon': -35.7350, 'pop': 957_916, 'area': 509.320},
    'AP': {'state': 'Amapá', 'capital': 'Macapá', 'lat': 0.0349, 'lon': -51.0665, 'pop': 442_993, 'area':  6_563.849},
    'AM': {'state': 'Amazonas', 'capital': 'Manaus', 'lat': -3.4653, 'lon': -62.2159, 'pop': 2_063_547, 'area': 11_401.092},
    'BA': {'state': 'Bahia', 'capital': 'Salvador', 'lat': -12.9714, 'lon': -38.5014, 'pop': 2_417_678, 'area':  693.453},
    'CE': {'state': 'Ceará', 'capital': 'Fortaleza', 'lat': -3.7172, 'lon': -38.5433, 'pop': 2_428_708, 'area':  312.353},
    'DF': {'state': 'Distrito Federal', 'capital': 'Brasília', 'lat': -15.7801, 'lon': -47.9292, 'pop': 2_817_068, 'area':  5_760.783},
    'ES': {'state': 'Espírito Santo', 'capital': 'Vitória', 'lat': -20.3155, 'lon': -40.3128, 'pop': 322_869, 'area':  97.123},
    'GO': {'state': 'Goiás', 'capital': 'Goiânia', 'lat': -16.6864, 'lon': -49.2643, 'pop': 1_437_237, 'area':  728.841},
    'MA': {'state': 'Maranhão', 'capital': 'São Luís', 'lat': -2.5387, 'lon': -44.2820, 'pop': 1_037_775, 'area':  582.974},
    'MT': {'state': 'Mato Grosso', 'capital': 'Cuiabá', 'lat': -15.6010, 'lon': -56.0979, 'pop': 650_912, 'area':  4_327.45},
    'MS': {'state': 'Mato Grosso do Sul', 'capital': 'Campo Grande', 'lat': -20.4428, 'lon': -54.6464, 'pop': 897_938, 'area':  8_082.978},
    'MG': {'state': 'Minas Gerais', 'capital': 'Belo Horizonte', 'lat': -19.9167, 'lon': -43.9345, 'pop': 2_315_560, 'area':  331.354},
    'PA': {'state': 'Pará', 'capital': 'Belém', 'lat': -1.4550, 'lon': -48.5024, 'pop': 1_303_375, 'area':  1_059.466},
    'PB': {'state': 'Paraíba', 'capital': 'João Pessoa', 'lat': -7.1151, 'lon': -34.8641, 'pop': 833_932, 'area':  210.044},
    'PR': {'state': 'Paraná', 'capital': 'Curitiba', 'lat': -25.4284, 'lon': -49.2733, 'pop': 1_773_733, 'area':  434.892},
    'PE': {'state': 'Pernambuco', 'capital': 'Recife', 'lat': -8.0476, 'lon': -34.8770, 'pop': 1_488_920, 'area':  218.843},
    'PI': {'state': 'Piauí', 'capital': 'Teresina', 'lat': -5.0936, 'lon': -42.8034, 'pop': 866_300, 'area': 1_391.046},
    'RJ': {'state': 'Rio de Janeiro', 'capital': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729, 'pop': 6_211_423, 'area':  1_200.329},
    'RN': {'state': 'Rio Grande do Norte', 'capital': 'Natal', 'lat': -5.7945, 'lon': -35.2120, 'pop': 751_300, 'area':  167.401},
    'RS': {'state': 'Rio Grande do Sul', 'capital': 'Porto Alegre', 'lat': -30.0346, 'lon': -51.2177, 'pop': 1_332_833, 'area':  495.390},
    'RO': {'state': 'Rondônia', 'capital': 'Porto Velho', 'lat': -8.7600, 'lon': -63.9000, 'pop': 460_413, 'area': 34_090.952},
    'RR': {'state': 'Roraima', 'capital': 'Boa Vista', 'lat': 2.8215, 'lon': -60.6731, 'pop': 413_486, 'area':  5_687.037},
    'SC': {'state': 'Santa Catarina', 'capital': 'Florianópolis', 'lat': -27.5954, 'lon': -48.5480, 'pop': 537.213, 'area':  674.844},
    'SP': {'state': 'São Paulo', 'capital': 'São Paulo', 'lat': -23.5505, 'lon': -46.6333, 'pop': 11_451_245, 'area':  1_521.110},
    'SE': {'state': 'Sergipe', 'capital': 'Aracaju', 'lat': -10.9472, 'lon': -37.0731, 'pop': 602_757, 'area':  182.163},
    'TO': {'state': 'Tocantins', 'capital': 'Palmas', 'lat': -10.2496, 'lon': -48.3242, 'pop': 302_692, 'area':  2_227.444}
}

geo_rules = {
    "35" : (0,999_999),
    "50" : (1_000_000,1_999_999),
    "100" : (2_000_000, float('inf'))
}