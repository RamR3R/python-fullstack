def slug_generator(ppp : str):
    # Hello World! Welcome to Django.
    ppp = ppp.lower()
    # hello world! welcome to django.
    ppp = list(ppp)
    result = "" #hello
    #[h , e , l , l ,o , , w, o ,r , l , d, ! , , w]
    for i in range(0, len(ppp)):
        if ppp[i].isalnum():
            result += ppp[i]
        elif ppp[i] == " ":
            result += "-"
        else:
            continue

    # ppp.replace(" " , "-")


    return result







title = input()
# "Hello World! Welcome to Django."
#hello-world-welcome-to-django
#lowercase , no spl char , space => -
result = slug_generator(title)

print(result)