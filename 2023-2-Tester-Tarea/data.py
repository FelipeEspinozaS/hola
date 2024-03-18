from src.models import Director, Movie, Ranking


DIRECTORS_A = [
    Director('Quentin Tarantino', 57, 'United States', True),
    Director('Christopher Nolan', 50, 'United Kingdom', False),
    Director('Greta Gerwig', 38, 'United States', False),
]

DIRECTORS_B = [
    Director('Sofia Coppola', 51, 'United States', True),
    Director('Kathryn Bigelow', 70, 'United States', True),
    Director('Pedro Almodóvar', 72, 'Spain', True),
]

WRONG_DIRECTORS = [
    Director('Alfred Hitchcock', 90, '', False),
    Director('', 52, 'United Kingdom', True),
]

MOVIES_A = [
    Movie(
        'Pulp Fiction',
        'Un enigmático gánster, su mujer, un boxeador y un par de ladrones de poca monta se entrecruzan en una historia llena de violencia y diálogos afilados en Los Ángeles.',
        154,
        '1994-10-10'
    ),
    Movie(
        'Kill Bill: Vol. 1',
        'La Novia, una asesina a sueldo, despierta de un coma y busca venganza contra su antiguo jefe y su equipo de asesinos que la traicionaron.',
        111,
        '2003-10-10'
    ),
    Movie(
        'Inception',
        'Dom Cobb, un ladrón de sueños, es contratado para implantar una idea en la mente de alguien. Sin embargo, se enfrenta a desafíos inimaginables en un mundo de sueños dentro de sueños.',
        148,
        '2010-07-16'
    ),
    Movie(
        'Interstellar',
        'En un futuro distópico, un grupo de astronautas emprende un viaje interestelar en busca de un nuevo hogar para la humanidad, enfrentando agujeros de gusano y el tiempo relativo.',
        169,
        '2014-11-07'
    ),
    Movie(
        'Lady Bird',
        'Christine "Lady Bird" McPherson, una adolescente en Sacramento, California, lucha por definir su identidad mientras se enfrenta a las tensiones familiares y las presiones del último año de preparatoria.',
        94,
        '2017-11-03'
    ),
    Movie(
        'Little Women',
        'La historia sigue a cuatro hermanas mientras crecen y buscan independencia en la sociedad de la posguerra en Nueva Inglaterra. Basada en la novela clásica de Louisa May Alcott.',
        135,
        '2019-12-25'
    ),
]

MOVIES_B = [
    Movie(
        'Lost in Translation',
        'Two strangers, feeling disconnected from their surroundings in Tokyo, form an unlikely bond as they explore the city together.',
        102,
        '2003-08-29'
    ),
    Movie(
        'The Virgin Suicides',
        'A group of teenage sisters captivate a group of neighborhood boys, leading to a tragic series of events in their conservative suburban community.',
        97,
        '1999-05-19'
    ),
    Movie(
        'The Hurt Locker',
        'An intense portrayal of an elite US. Army bomb disposal unit during the Iraq War, focusing on their high-stakes and dangerous missions.',
        131,
        '2008-09-04'
    ),
    Movie(
        'Zero Dark Thirty',
        'Follows the decade-long hunt for Osama bin Laden after the September 11 attacks in US, culminating in the successful raid by US. Navy SEALs.',
        157,
        '2012-12-19'
    ),
    Movie(
        'Hable con Ella',
        'Two men develop a unique friendship as they care for two women in comas, exploring themes of love, connection, and emotional depth.',
        112,
        '2002-03-15'
    ),
    Movie(
        'All About My Mother (Todo sobre mi madre)',
        'After her sons tragic death, a nurse embarks on a journey to find her sons transgender father, encountering a cast of colorful characters along the way.',
        101,
        '1999-04-08'
    ),
]

WRONG_MOVIES = [
    Movie(
        '',
        'An FBI agent goes undercover to infiltrate a group of surfers who are suspected of robbing banks and participating in extreme sports.',
        122,
        '1991-07-12'
    )
]

RANKINGS_A = [
    Ranking('imdb', 0, 8.7, 10),
    Ranking('rotten_tomatoes', 0, 85, 100),
    Ranking('metacritic', 0, 76, 95),
    Ranking('imdb', 0, 6.5, 10),
    Ranking('rotten_tomatoes', 0, 64, 100),
    Ranking('metacritic', 0, 50, 95),
    Ranking('imdb', 0, 5.3, 10),
    Ranking('rotten_tomatoes', 0, 42, 100),
    Ranking('metacritic', 0, 39, 95),
]

RANKINGS_B = [
    Ranking('imdb', 0, 5.6, 10),
    Ranking('rotten_tomatoes', 0, 48, 100),
    Ranking('metacritic', 0, 20, 95),
    Ranking('imdb', 0, 9.1, 10),
    Ranking('rotten_tomatoes', 0, 80, 100),
    Ranking('metacritic', 0, 30, 95),
    Ranking('imdb', 0, 7.9, 10),
    Ranking('rotten_tomatoes', 0, 47, 100),
    Ranking('metacritic', 0, 10, 95),
]
