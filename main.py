from hashlib import md5, sha1, sha224, sha256, sha384, sha512


def main():
    pw = b"Password"
    print(f"md5: {md5(pw).hexdigest()}")
    print(f"sha1; {sha1(pw).hexdigest()}")
    print(f"sha224; {sha224(pw).hexdigest()}")
    print(f"sha256; {sha256(pw).hexdigest()}")
    print(f"sha384: {sha384(pw).hexdigest()}")
    print(f"sha512: {sha512(pw).hexdigest()}")


if __name__ == "__main__":
    main()
