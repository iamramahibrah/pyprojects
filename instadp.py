import instaloader

def instagram():
    insta = instaloader.Instaloader()
    dp = input("Enter instagram username: ")
    insta.download_profile(dp, profile_pic_only=True)
    print("your image is downloaded")
    
instagram()