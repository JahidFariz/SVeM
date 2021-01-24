def tts(text):
    engine.say(text)
    engine.runAndWait()


def stt():
    try:
        with speech_recognition.Microphone() as source:
            print("Listening...")
            s = listener.listen(source)
            t = listener.recognize_google(s).lower()
            print(t)
            return t

    except AttributeError as err:
        print(colorama.Fore.RED + "[FAILED] Unable to Listen...")
        print(colorama.Fore.RED + f"[FAILED] {format(err)}")

        print(colorama.Fore.YELLOW + "Type Manually.")
        return input(colorama.Fore.RED + ">> " + colorama.Style.RESET_ALL).strip()


try:
    name = ""
    email = ""
    passwd = ""
    to_addr = ""
    subj = ""
    msg = ""
    pub_ip = ""

    print("[ INFO ] Importing platform...")
    import platform
    print("[  OK  ] platform imported successfully...")

    operating_system = platform.system()
    print("[ INFO ] Operating System: " + operating_system)

    print("[ INFO ] Importing os...")
    import os
    print("[  OK  ] os imported successfully...")

    main_loop = True
    while main_loop:
        try:
            print("[ INFO ] Importing pip v21.0...")
            print("The PyPA recommended tool for installing Python packages.")
            import pip
            print("[  OK  ] pip v21.0 imported successfully...")

            main_loop = False

        except ModuleNotFoundError as e:
            print(f"[FAILED] {format(e)}")

            if operating_system == "Linux":
                print("SECURITY REMINDER! PYTHON3-PIP REQUIRED...")
                print("For more information: https://pypi.org/project/pip/")

                sub_loop = True
                while sub_loop:
                    choice = input("Would you like to install python3-pip? [y|n] : ").lower()

                    if choice.strip() == "y" or choice.strip() == "yes":
                        print("[ INFO ]Updating repositories...")
                        print("$ sudo apt update")
                        os.system("sudo apt update")

                        print("[ INFO ] Installing Python3-Pip...")
                        print("$ sudo apt install -y python3-pip")
                        os.system("sudo apt install -y python3-pip")

                        sub_loop = False

                    elif choice.strip() == "n" or choice.strip() == "no":
                        print("Exiting...")
                        sub_loop = False
                        exit()

                    else:
                        print("[ INFO ] Invalid choice, Please try again...")

    try:
        print("[ INFO ] Importing colorama v0.4.4...")
        print("Cross-platform colored terminal text.")
        import colorama

        print(colorama.Fore.GREEN + "[  OK  ] colorama v0.4.4 imported successfully..." + colorama.Style.RESET_ALL)

        print(colorama.Fore.YELLOW + "[ INFO ] Initializing colorama..." + colorama.Style.RESET_ALL)
        colorama.init(autoreset=True)
        print(colorama.Fore.GREEN + "[  OK  ] colorama initialized successfully...")

    except ModuleNotFoundError as e:
        print(f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install colorama: \'pip install colorama\'")
        print("For more information: https://pypi.org/project/colorama/")
        print("Exiting...")
        exit()

    print(colorama.Fore.YELLOW + "[ INFO ] Operating System : " + colorama.Style.RESET_ALL + operating_system)

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing pyttsx3 v2.90...")
        print(colorama.Fore.BLUE + "Text to Speech (TTS) library for Python 2 and 3.")
        print(colorama.Fore.BLUE + "Works without internet connection or delay.")
        print(colorama.Fore.BLUE + "Supports multiple TTS engines, including Sapi5, nsss, and espeak.")
        import pyttsx3

        print(colorama.Fore.GREEN + "[  OK  ] pyttsx3 v2.90 imported successfully...")

        main_loop = True
        while main_loop:
            try:
                print(colorama.Fore.YELLOW + "[ INFO ] Initializing pyttsx3...")
                engine = pyttsx3.init()
                print(colorama.Fore.GREEN + "[  OK  ] pyttsx3 initialized successfully...")
                main_loop = False

            except OSError as e:
                print(colorama.Fore.RED + f"[FAILED] {format(e)}")

                if operating_system == "Linux":
                    print(colorama.Fore.RED + "SECURITY REMINDER! ESPEAK AND ALSA-UTILS REQUIRED...")

                    sub_loop0 = True
                    while sub_loop0:
                        choice = input(colorama.Fore.RED + "Would you like to install espeak and alsa-utils? [y|n] : "
                                       + colorama.Style.RESET_ALL).lower()

                        if choice.strip() == "y" or choice.strip() == "yes":
                            print(colorama.Fore.YELLOW + "[ INFO ] Updating repositories...")
                            print("$ " + colorama.Fore.RED + "sudo apt update")
                            os.system("sudo apt update")

                            print(colorama.Fore.YELLOW + "[ INFO ] Installing Espeak...")
                            print("$ " + colorama.Fore.RED + "sudo apt install -y espeak")
                            os.system("sudo apt install -y espeak")

                            print(colorama.Fore.YELLOW + "[ INFO ] Installing Alsa-utils...")
                            print("$ " + colorama.Fore.RED + "sudo apt install -y alsa-utils")
                            os.system("sudo apt install -y alsa-utils")

                            print(colorama.Fore.GREEN + "Done...")
                            sub_loop0 = False

                        elif choice.strip() == "n" or choice.strip() == "no":
                            print("Exiting...")
                            sub_loop0 = False
                            exit()

                        else:
                            print(colorama.Fore.RED + "[FAILED] Invalid choice, Please try again...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install pyttsx3: \'pip install pyttsx3\'")
        print("For more information: https://pypi.org/project/pyttsx3/")
        print("Exiting...")
        exit()

    print(colorama.Fore.YELLOW + "[ INFO ] Importing smtplib...")
    import smtplib

    print(colorama.Fore.GREEN + "[  OK  ] smtplib imported successfully...")

    print(colorama.Fore.YELLOW + "[ INFO ] Importing socket")
    import socket

    print(colorama.Fore.GREEN + "[  OK  ] socket imported successfully...")

    print(colorama.Fore.YELLOW + "[ INFO ] Importing pickle...")
    import pickle

    print(colorama.Fore.GREEN + "[  OK  ] pickle imported successfully...")

    print(colorama.Fore.YELLOW + "[ INFO ] Importing getpass...")
    import getpass

    print(colorama.Fore.GREEN + "[  OK  ] getpass imported successfully...")

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing speech_recognition v3.8.1...")
        print(colorama.Fore.BLUE + "Library for performing speech recognition, "
                                   "with support for several engines and APIs, "
                                   "online and offline.")
        import speech_recognition

        print(colorama.Fore.GREEN + "[  OK  ] speech_recognition v3.8.1 imported successfully...")

        print(colorama.Fore.YELLOW + "[ INFO ] Creating a listener...")
        listener = speech_recognition.Recognizer()
        print(colorama.Fore.GREEN + "[  OK  ] Listener created successfully...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install speech_recognition: "
                                     "\'pip install SpeechRecognition\'")
        print("For more information: https://pypi.org/project/SpeechRecognition/")
        print("Exiting...")
        exit()

    print(colorama.Fore.YELLOW + "[ INFO ] Importing re")
    import re
    print(colorama.Fore.GREEN + "[  OK  ] re imported successfully...")

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing urllib3 v1.26.2...")
        print(colorama.Fore.BLUE + "HTTP library with thread-safe connection pooling, file post, and more.")
        import urllib3
        print(colorama.Fore.GREEN + "[  OK  ] urllib3 v1.26.2 imported successfully...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install urllib3: \'pip install urllib3\'")
        print("For more information: https://pypi.org/project/urllib3/")
        print("Exiting...")
        exit()

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing chardet v4.0.0...")
        print(colorama.Fore.BLUE + "Universal encoding detector for Python 2 and 3")
        import chardet
        print(colorama.Fore.GREEN + "[  OK  ] chardet v4.0.0 imported successfully...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following to install chardet: \'pip install chardet\'")
        print("For more information: https://pypi.org/project/chardet/")
        print("Exiting...")
        exit()

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing certifi v2020.12.5...")
        print(colorama.Fore.BLUE + "Python package for providing Mozilla's CA Bundle.")
        import certifi
        print(colorama.Fore.GREEN + "[  OK  ] certifi v2020.12.5 imported successfully...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install certifi: \'pip install certifi\'")
        print("For more information: https://pypi.org/project/certifi/")
        print("Exiting...")
        exit()

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing idna v3.1...")
        print(colorama.Fore.BLUE + "Internationalized Domain Names in Applications (IDNA)")
        import idna
        print(colorama.Fore.GREEN + "[  OK  ] idna v3.1 imported successfully...")

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install idna: \'pip install idna\'")
        print("For more information: https://pypi.org/project/idna/")
        print("Exiting...")
        exit()

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Importing requests v2.25.1...")
        print(colorama.Fore.BLUE + "Python HTTP for Humans.")
        import requests
        print(colorama.Fore.GREEN + "[  OK  ] requests v2.25.1 imported successfully...")

        try:
            pub_ip = requests.get("https://api.ipify.org").text
            print(colorama.Fore.YELLOW + "[ INFO ] Public IP: " + colorama.Style.RESET_ALL + pub_ip)

        except requests.exceptions.ConnectionError as e:
            print(colorama.Fore.RED + f"[FAILED] {format(e)}")
            print("Exiting...")
            exit()

    except ModuleNotFoundError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        print(colorama.Fore.YELLOW + "[ INFO ] Use the following command to install requests: \'pip install requests\'")
        print("For more information: https://pypi.org/project/requests/")
        print("Exiting...")
        exit()

    print(colorama.Fore.YELLOW + "[ INFO ] Importing datetime...")
    import datetime
    print(colorama.Fore.GREEN + "datetime imported successfully...")

    try:
        print(colorama.Fore.YELLOW + "[ INFO ] Connecting to Gmail SMTP server, Please wait...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()  # WARNING THIS PROCESS DOES NOT THROW ANY EXCEPTIONS
        print(colorama.Fore.GREEN + "[  OK  ] Successfully connected to \'smtp.gmail.com:587\'.")

        print(colorama.Fore.YELLOW + "[ INFO ] Starting TLS Handshake...")
        server.starttls()  # WARNING THIS PROCESS DOES NOT THROW ANY EXCEPTIONS
        print(colorama.Fore.GREEN + "[  OK  ] TLS Handshake started successfully...")

        if os.path.isfile("SVeM.cache"):
            cache = open("SVeM.cache", "rb")

            try:
                print(colorama.Fore.YELLOW + "[ INFO ] Importing saved credentials from cache file...")
                user_credential = pickle.load(cache)
                print(colorama.Fore.GREEN + "[  OK  ] Login credentials are loaded successfully...")

                name = user_credential[0]
                email = user_credential[1]
                passwd = user_credential[2]

                cache.close()

                try:
                    print(colorama.Fore.YELLOW + "[ INFO ] Logging in to your Google account, Please wait...")
                    server.login(email, passwd)  # WARNING THIS PROCESS DOES NOT THROW ANY EXCEPTIONS
                    print(colorama.Fore.GREEN + "[  OK  ] SignIn completed successfully...")

                    logged_in_time = datetime.datetime.now()

                    msg = "To:" + email + \
                          "\nFrom:" + email + \
                          "\nSubject: Security Alert!" + \
                          "\nSomeone just used signed in your Google Account from SVeM (Simple Voice Email)." + \
                          "\nPublic IP Address: " + pub_ip + \
                          "\nTime: " + str(logged_in_time) + \
                          "\nOperating System: " + operating_system + \
                          "\nUsername: " + getpass.getuser()

                    server.sendmail(email, email, msg)

                    print(colorama.Fore.BLUE + "Welcome back to SVeM (Simple Voice Email), " +
                          colorama.Style.RESET_ALL + f"{name}.")
                    tts(f"Welcome back to SVeM (Simple Voice Email), {name}.")

                    print(colorama.Fore.BLUE + "Created by JahidFariz. " + colorama.Fore.RED + "Made with Love in " +
                          colorama.Fore.YELLOW + "In" +
                          colorama.Style.RESET_ALL + "d" +
                          colorama.Fore.GREEN + "ia" +
                          colorama.Style.RESET_ALL + ".")
                    tts("Created by JahidFariz. Made with love in India.")

                except smtplib.SMTPAuthenticationError as e:
                    print(colorama.Fore.RED + f"[FAILED] {format(e)}")
                    tts("An error occurred, Unable to login...")
                    print("Exiting...")
                    exit()

            except EOFError as e:
                print(colorama.Fore.RED + f"[FAILED] {format(e)}")
                tts("An error occurred, Unable to load cache config file...")
                print("Exiting...")
                exit()

            except pickle.UnpicklingError as e:
                print(colorama.Fore.RED + f"[FAILED] {format(e)}")
                tts("An error occurred, Unable to load cache config file...")
                print("Exiting...")
                exit()

        else:
            print(colorama.Fore.BLUE + "Welcome to SVeM (Simple Voice Email), Created by JahidFariz.")
            tts("Welcome to SVeM (Simple Voice Email), Created by JahidFariz.")

            print(colorama.Fore.RED + "Made with Love in " +
                  colorama.Fore.YELLOW + "In" +
                  colorama.Style.RESET_ALL + "d" +
                  colorama.Fore.GREEN + "ia" +
                  colorama.Style.RESET_ALL + "."
                  )
            tts("Made with love in India.")

            print(colorama.Fore.RED + "How should I call you?")
            tts("How should I call you?")

            main_loop = True
            while main_loop:
                name = input(colorama.Fore.RED + "Please enter your name or nickname : " +
                             colorama.Style.RESET_ALL).strip()

                if len(name) != 0:
                    main_loop = False
                    print(colorama.Fore.BLUE + "Hello " + colorama.Style.RESET_ALL + f"{name}!" + colorama.Fore.BLUE +
                          " Welcome to SVeM (Simple Voice Email), Created by JahidFariz.")
                    tts("Welcome to SVeM (Simple Voice Email), Created by JahidFariz.")

                    print(colorama.Fore.RED + "Made with Love in " +
                          colorama.Fore.YELLOW + "In" +
                          colorama.Style.RESET_ALL + "d" +
                          colorama.Fore.GREEN + "ia" +
                          colorama.Style.RESET_ALL + "."
                          )
                    tts("Made with love in India.")

                else:
                    print(colorama.Fore.RED + "[FAILED] Invalid name, Please try again...")
                    tts("Invalid name, Please try again...")

            main_loop = True
            while main_loop:
                email = input(colorama.Fore.RED + "Please enter your Gmail address : " +
                              colorama.Style.RESET_ALL).strip()

                if len(email) != 0:
                    main_loop = False

                else:
                    print(colorama.Fore.RED + "[FAILED] Email address cannot be empty!")
                    tts("Email address cannot be empty!")

            main_loop = True
            while main_loop:
                passwd = getpass.getpass()

                if len(passwd) == 0:
                    print(colorama.Fore.RED + "[FAILED] Password field cannot be empty!")
                    tts("Password field cannot be empty!")

                elif len(passwd) < 8 or len(passwd) > 100:
                    print(colorama.Fore.RED + "[FAILED] Incorrect Password, Please try again...")
                    tts("Incorrect password, Please try again...")

                else:
                    main_loop = False
                    print(colorama.Fore.BLUE + "Don't worry we never share your personal information and "
                                               "password to others...")
                    tts("Don't worry we never share your personal information and password to others...")

            print(colorama.Fore.RED + "Please don't forget to turn on less secure apps on your Google account...")
            tts("Please don't forget to turn on less secure apps on your Google account...")

            print("https://myaccount.google.com/lesssecureapps")
            tts("Use the following link to turn on less secure apps on your google account.")

            input(colorama.Fore.RED + "Press any key to continue..." + colorama.Style.RESET_ALL)

            try:
                print(colorama.Fore.YELLOW + "[ INFO ] Logging in to your Google Account, Please wait...")
                server.login(email, passwd)  # WARNING THIS PROCESS DOES NOT THROW ANY EXCEPTIONS
                print(colorama.Fore.GREEN + "[  OK  ] Login completed successfully...")

                print(colorama.Fore.RED + "SECURITY REMINDER, STORAGE PERMISSION!")
                print("SVeM (Simple Voice Email) needs to access your storage to access your cache files.")
                tts("SVeM (Simple Voice Email) needs to access your storage.")

                main_loop = True
                while main_loop:
                    choice = input(colorama.Fore.RED + "SVeM (Simple Voice Email) is trying to access your storage, "
                                                       "do you allow? [y|n] : " + colorama.Style.RESET_ALL).lower()

                    if choice.strip() == "y" or choice.strip() == "yes":
                        print(colorama.Fore.GREEN + "[  OK  ] Storage Permission Granted!")
                        tts("Storage permission granted.")

                        user_credentials = [name, email, passwd]

                        cache = open("SVeM.cache", "wb")
                        pickle.dump(user_credentials, cache)
                        cache.close()

                        print(colorama.Fore.GREEN + "[  OK  ] Login credential saved successfully...")
                        tts("Login credential saved successfully...")

                        main_loop = False

                    elif choice.strip() == "n" or choice.strip() == "no":
                        print(colorama.Fore.RED + "[FAILED] Storage Permission Denied!")
                        tts("Storage Permission Denied!")

                        print(colorama.Fore.RED + "[FAILED] Failed to save login credentials...")
                        tts("Failed to save login credentials...")

                        main_loop = False

                    else:
                        print(colorama.Fore.RED + "[FAILED] Invalid choice, Please try again...")
                        tts("Invalid choice, Please try again...")

            except smtplib.SMTPAuthenticationError as e:
                print(colorama.Fore.RED + f"[FAILED] {format(e)}")
                tts("An error occurred, Unable to login...")
                print("Exiting...")
                exit()

        main_loop = True
        while main_loop:
            print(colorama.Fore.BLUE + "To whom do you want to send email?")
            tts("To whom do you want to send email?")
            to_addr = stt().lower()

            if len(to_addr):
                # "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
                if re.search("^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$", to_addr):
                    main_loop = False

                else:
                    print(colorama.Fore.RED + "[FAILED] Invalid email address. Please Try again...")
                    tts("Sorry, Invalid email address. Please try again...")

            else:
                print(colorama.Fore.YELLOW + "[ NOTE ] To address cannot be empty! Please try again...")
                tts("To address cannot be empty! Please try again...")

        main_loop = True
        while main_loop:
            print(colorama.Fore.BLUE + "What is the subject of your email?")
            tts("What is the subject of your email?")
            subj = stt().title()

            if len(subj) <= 63:
                main_loop = False

            else:
                print(colorama.Fore.YELLOW + "[ NOTE ] Your subject update cannot exceed 63 characters. "
                                             "Please try again...")
                tts("Your subject update cannot exceed 63 characters. Please try again...")

        main_loop = True
        while main_loop:
            print(colorama.Fore.BLUE + "What is the body of your email message?")
            tts("What is the body of your email message?")
            msg = stt()

            if len(msg):
                main_loop = False

            else:
                print(colorama.Fore.YELLOW + "[ NOTE ] Message field cannot be empty! Please try again...")
                tts("Message field cannot be empty. Please try again...")

        print(colorama.Fore.RED + "From : " + colorama.Style.RESET_ALL + email)
        print(colorama.Fore.RED + "To : " + colorama.Style.RESET_ALL + to_addr)
        print(colorama.Fore.RED + "Subject : " + colorama.Style.RESET_ALL + subj)
        print(colorama.Fore.RED + "Message : " + colorama.Style.RESET_ALL + msg)

        msg = "To:" + to_addr + "\n" + "From:" + email + "\n" + "Subject:" + subj + "\n" + msg

        input(colorama.Fore.RED + "Press enter key to send." + colorama.Style.RESET_ALL)

        print(colorama.Fore.YELLOW + "[ INFO ] Sending eMail, Please wait...")
        server.sendmail(email, to_addr, msg)  # WARNING THIS PROCESS DOES NOT THROW ANY EXCEPTIONS
        print(colorama.Fore.GREEN + "[  OK  ] eMail sent successfully...")
        tts("Email sent successfully...")

        print(colorama.Fore.YELLOW + "[ INFO ] Closing server...")
        server.close()
        print(colorama.Fore.GREEN + "[  OK  ] Server closed successfully...")

    except socket.gaierror as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        tts("An error occurred, Unable to reach the service...")
        print("Exiting...")
        exit()

    except OSError as e:
        print(colorama.Fore.RED + f"[FAILED] {format(e)}")
        tts("An error occurred, Unable to reach the service...")
        print("Exiting...")
        exit()

except KeyboardInterrupt:
    print("\n[FAILED] KeyboardInterrupt occurred, Bye!")
    exit()
