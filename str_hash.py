import hashlib
def main():
    input_string=str(input("Enter a string : "))
    dd_string=input_string.encode("utf-8")
    hash = hashlib.md5(dd_string)
    hexa=hash.hexdigest()
    print(hexa)
    return
main()