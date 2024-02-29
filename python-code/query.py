import parse
from urllib import parse as parse_package

# EXAMPLE QUERIES
    # https://twitter.com/search?q=(%22iron%20man%22%20OR%20%22Iron%20Man%22)
    # https://twitter.com/search?q=(from%3Anba)&src=typed_query
    # https://twitter.com/search?f=top&q=mlk%20(from%3Anfl%20OR%20from%3Anba)&src=typed_query
    # https://twitter.com/search?f=top&q=(%23gsw)%20lang%3Aen&src=typed_query
    # https://twitter.com/search?f=top&q=(%40nba)&src=typed_query

    # https://twitter.com/search?f=top&q=until:2023-09-01%20since:2023-07-04&src=typed_query
    # until:2023-09-01 since:2023-07-04

def query_builder(**kwargs) -> str:
    # print(kwargs)

    # Initializing Query Parameters
    keyword         = "";       hash_tags       = "";
    from_account    = "";       language        = "";
    to_account      = "";       start_date      = "";
    exact_phrase    = "";       end_date        = "";
    any_phrase      = "";


    if (kwargs.get('keyword') != None): 
        keyword = parse.combine_words(kwargs.get('keyword'))
    if (kwargs.get('from_account') != None): 
        # https://twitter.com/search?q=iron%20man%20(from%3A%22iron_man%22%2C%20OR%20from%3A%22RobertDowneyJr%22%2C%20OR%20from%3A%22terrencehoward%22%2C%22%20OR%20from%3Athejeffbridges%22%2C%20OR%20from%3A%22Jon_Favreau%22)&src=typed_query
        accounts = parse.combine_words(kwargs.get('from_account'))
        from_account += "("
        for account in accounts:
            from_account += parse_package.quote(f'from:{account}')
            if account != accounts[-1]:
                from_account += parse_package.quote(", OR ")
            else:
                from_account += ")"

    if (kwargs.get('to_account') != None): 
        accounts = parse.combine_words(kwargs.get('to_account'))
        to_account += "("
        for account in accounts:
            to_account += parse_package.quote(f'to:{account}')
            if account != accounts[-1]:
                from_account += parse_package.quote(", OR ")
            else:
                from_account += ")"

    ########### TODO: FIX THE PARSING ON THIS BLOCK TO PROPERLY MATCH URLS
    if (kwargs.get('exact_phrase') != None):
        exact_phrase = parse.combine_words(kwargs.get('exact_phrase'), method="AND")
    if (kwargs.get('any_phrase') != None): 
        any_phrase = parse.combine_words(kwargs.get('any_phrase'), method="OR")
    if (kwargs.get('hash_tags') != None): 
        hash_tags = parse.hash_tags(kwargs.get('any_phrase'))
    if (kwargs.get('language') != None): 
        language = parse.combine_words('language')
    #############
    
    if (kwargs.get('start_date') != None): 
        start_date = parse_package.quote(f"since:{kwargs['start_date']}")
    if (kwargs.get('end_date') != None): 
        end_date = parse_package.quote(f"until:{kwargs['end_date']}")


    query = f"https://twitter.com/search?q={keyword}{from_account}{to_account}\
        {exact_phrase}{any_phrase}{hash_tags}{language}{end_date}{start_date}&src=typed_query"

    return query.replace(" ", "")