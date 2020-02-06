class Config:

    def __init__(self, suiteFlagNumber=0):

        self.suiteFlagNumber = suiteFlagNumber

        # Config Flags
        self.FLAG_Prod = 1  # Binary 00001
        self.FLAG_Staging = 2  # Binary 00010
        self.FLAG_Email = 4  # Binary 00100
        self.FLAG_Chrome = 8  # Binary 01000
        self.FLAG_Firefox = 16  # Binary 010000
        self.FLAG_Edge = 32  # Binary 0100000
        self.FLAG_Safari = 64  # Binary 01000000
        self.FLAG_Android = 128  # Binary 010000000P
        self.FLAG_Ios = 256  # Binary 0100000000
        self.FLAG_Suite = 512  # Binary 01000000000
        self.FLAG_MobileApp = 1024  # Binary 010000000000
        self.FLAG_Cloud = 2048  # Binary 0100000000000
        self.FLAG_Grid = 4096  # Binary  01000000000000
        self.FLAG_Local = 8192  # Binary 010000000000000



    def display_suite_bits(self):
        bits = ""

        if self.check_suite_prod():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_staging():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_email():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_chrome():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_firefox():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_edge():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_safari():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_android():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_ios():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_suite():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_mobileapp():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_cloud():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_grid():
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.check_suite_local():
            bits = "1" + bits
        else:
            bits = "0" + bits

        return bits

    def get_bits(self, _num):
        bits = ""

        if self.prod(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.staging(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.email(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.chrome(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.firefox(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.edge(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.safari(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.android(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.ios(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.suite(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.mobileapp(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.cloud(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.grid(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        if self.local(_num):
            bits = "1" + bits
        else:
            bits = "0" + bits

        return bits

    def display_config(self, _num):
        bits = ""
        if self.prod(_num):
            print("Suite Prod : 1")
            bits = "1" + bits
        else:
            print("Suite Prod : 0")
            bits = "0" + bits

        if self.staging(_num):
            print("Suite Staging : 1")
            bits = "1" + bits
        else:
            print("Suite Staging : 0")
            bits = "0" + bits

        if self.email(_num):
            print("Suite Email : 1")
            bits = "1" + bits
        else:
            print("Suite Email : 0")
            bits = "0" + bits

        if self.chrome(_num):
            print("Suite Chrome : 1")
            bits = "1" + bits
        else:
            print("Suite Chrome : 0")
            bits = "0" + bits

        if self.firefox(_num):
            print("Suite Firefox : 1")
            bits = "1" + bits
        else:
            print("Suite Firefox : 0")
            bits = "0" + bits

        if self.edge(_num):
            print("Suite Edge : 1")
            bits = "1" + bits
        else:
            print("Suite Edge : 0")
            bits = "0" + bits

        if self.safari(_num):
            print("Suite Safari: 1")
            bits = "1" + bits
        else:
            print("Suite Safari : 0")
            bits = "0" + bits

        if self.android(_num):
            print("Suite Android: 1")
            bits = "1" + bits
        else:
            print("Suite Android : 0")
            bits = "0" + bits

        if self.ios(_num):
            print("Suite IOS: 1")
            bits = "1" + bits
        else:
            print("Suite IOS : 0")
            bits = "0" + bits

        if self.suite(_num):
            print("Suite Suite: 1")
            bits = "1" + bits
        else:
            print("Suite Suite: 0")
            bits = "0" + bits

        if self.mobileapp(_num):
            print("Suite MobileApp: 1")
            bits = "1" + bits
        else:
            print("Suite MobileApp: 0")
            bits = "0" + bits

        if self.cloud(_num):
            print("Suite Cloud: 1")
            bits = "1" + bits
        else:
            print("Suite Cloud: 0")
            bits = "0" + bits

        if self.grid(_num):
            print("Suite Grid: 1")
            bits = "1" + bits
        else:
            print("Suite Grid: 0")
            bits = "0" + bits

        if self.local(_num):
            print("Suite Local: 1")
            bits = "1" + bits
        else:
            print("Suite Local: 0")
            bits = "0" + bits

        print("Value of suite is ", _num, " Binary " + bits)

    def display_suite_config(self):
        bits = ""
        if self.check_suite_prod():
            print("Suite Prod : 1")
            bits = "1" + bits
        else:
            print("Suite Prod : 0")
            bits = "0" + bits

        if self.check_suite_staging():
            print("Suite Staging : 1")
            bits = "1" + bits
        else:
            print("Suite Staging : 0")
            bits = "0" + bits

        if self.check_suite_email():
            print("Suite Email : 1")
            bits = "1" + bits
        else:
            print("Suite Email : 0")
            bits = "0" + bits

        if self.check_suite_chrome():
            print("Suite Chrome : 1")
            bits = "1" + bits
        else:
            print("Suite Chrome : 0")
            bits = "0" + bits

        if self.check_suite_firefox():
            print("Suite Firefox : 1")
            bits = "1" + bits
        else:
            print("Suite Firefox : 0")
            bits = "0" + bits

        if self.check_suite_edge():
            print("Suite Edge : 1")
            bits = "1" + bits
        else:
            print("Suite Edge : 0")
            bits = "0" + bits

        if self.check_suite_safari():
            print("Suite Safari: 1")
            bits = "1" + bits
        else:
            print("Suite Safari : 0")
            bits = "0" + bits

        if self.check_suite_android():
            print("Suite Android: 1")
            bits = "1" + bits
        else:
            print("Suite Android : 0")
            bits = "0" + bits

        if self.check_suite_ios():
            print("Suite IOS: 1")
            bits = "1" + bits
        else:
            print("Suite IOS : 0")
            bits = "0" + bits

        if self.check_suite_suite():
            print("Suite Suite: 1")
            bits = "1" + bits
        else:
            print("Suite Suite: 0")
            bits = "0" + bits

        if self.check_suite_mobileapp():
            print("Suite MobileApp: 1")
            bits = "1" + bits
        else:
            print("Suite MobileApp: 0")
            bits = "0" + bits

        if self.check_suite_cloud():
            print("Suite Cloud: 1")
            bits = "1" + bits
        else:
            print("Suite Cloud: 0")
            bits = "0" + bits

        if self.check_suite_grid():
            print("Suite Grid: 1")
            bits = "1" + bits
        else:
            print("Suite Grid: 0")
            bits = "0" + bits

        if self.check_suite_local():
            print("Suite Local: 1")
            bits = "1" + bits
        else:
            print("Suite Local: 0")
            bits = "0" + bits

        print("Value of suite is ", self.suiteFlagNumber, " Binary " + bits)

    # Operator: | Binary OR

    def set_suite_prod(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Prod
        print("set_suite_prod - Value of suite is ", self.suiteFlagNumber, " Decimal ",
              self.FLAG_Prod, " (Prod Binary 00001)")

    def set_suite_staging(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Staging
        print("set_suite_staging - Value of suite is ", self.suiteFlagNumber, " Decimal ",
              self.FLAG_Staging, " (Prod Binary 00010)")

    def set_suite_email(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Email
        print("set_suite_email - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Email, " (Email Binary 00100")

    def set_suite_chrome(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Chrome
        print("set_suite_chrome - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Chrome, " (Chrome Binary 01000")

    def set_suite_firefox(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Firefox
        print("set_suite_firefox - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Firefox, " (Firefox Binary 010000")

    def set_suite_edge(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Edge
        print("set_suite_edge - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Edge, " (Edge Binary 0100000")

    def set_suite_safari(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Safari
        print("set_suite_edge - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Safari, " (Safari Binary 01000000")

    def set_suite_android(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Android
        print("set_suite_android - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Android, " (Android Binary 010000000")

    def set_suite_ios(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Ios
        print("set_suite_android - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Ios, " (Android IOS 0100000000")

    def set_suite_suite(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Suite
        print("set_suite_android - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Suite, " (Android Suite 01000000000")

    def set_suite_mobileapp(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_MobileApp
        print("set_suite_mobileapp - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_MobileApp, " (Android Suite 010000000000")

    def set_suite_cloud(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Cloud
        print("set_suite_cloud - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Cloud, " (Android Suite 0100000000000")

    def set_suite_grid(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Grid
        print("set_suite_grid - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Grid, " (Android Suite 01000000000000")

    def set_suite_local(self):
        self.suiteFlagNumber = self.suiteFlagNumber | self.FLAG_Local
        print("set_suite_grid - Value of suite is ", self.suiteFlagNumber, " Decimal",
              self.FLAG_Local, " (Android Suite 010000000000000")

    def get_suite_flag_number(self):
        return self.suiteFlagNumber

    # Checking the flag - To test the value of a flag, use bitwise AND:
    def prod(self, _flagNumber):
        return _flagNumber & self.FLAG_Prod == self.FLAG_Prod

    def staging(self, _flagNumber):
        return _flagNumber & self.FLAG_Staging == self.FLAG_Staging

    def email(self, _flagNumber):
        return _flagNumber & self.FLAG_Email == self.FLAG_Email

    def chrome(self, _flagNumber):
        return _flagNumber & self.FLAG_Chrome == self.FLAG_Chrome

    def firefox(self, _flagNumber):
        return _flagNumber & self.FLAG_Firefox == self.FLAG_Firefox

    def edge(self, _flagNumber):
        return _flagNumber & self.FLAG_Edge == self.FLAG_Edge

    def safari(self, _flagNumber):
        return _flagNumber & self.FLAG_Safari == self.FLAG_Safari

    def android(self, _flagNumber):
        return _flagNumber & self.FLAG_Android == self.FLAG_Android

    def ios(self, _flagNumber):
        return _flagNumber & self.FLAG_Ios == self.FLAG_Ios

    def suite(self, _flagNumber):
        return _flagNumber & self.FLAG_Suite == self.FLAG_Suite

    def mobileapp(self, _flagNumber):
        return _flagNumber & self.FLAG_MobileApp == self.FLAG_MobileApp

    def cloud(self, _flagNumber):
        return _flagNumber & self.FLAG_Cloud == self.FLAG_Cloud

    def grid(self, _flagNumber):
        return _flagNumber & self.FLAG_Grid == self.FLAG_Grid

    def local(self, _flagNumber):
        return _flagNumber & self.FLAG_Local == self.FLAG_Local

    #
    # Checking the flag - To test the value of a flag, use bitwise AND:
    def check_suite_prod(self):
        return self.suiteFlagNumber & self.FLAG_Prod == self.FLAG_Prod

    def check_suite_staging(self):
        return self.suiteFlagNumber & self.FLAG_Staging == self.FLAG_Staging

    def check_suite_email(self):
        return self.suiteFlagNumber & self.FLAG_Email == self.FLAG_Email

    def check_suite_chrome(self):
        return self.suiteFlagNumber & self.FLAG_Chrome == self.FLAG_Chrome

    def check_suite_firefox(self):
        return self.suiteFlagNumber & self.FLAG_Firefox == self.FLAG_Firefox

    def check_suite_edge(self):
        return self.suiteFlagNumber & self.FLAG_Edge == self.FLAG_Edge

    def check_suite_safari(self):
        return self.suiteFlagNumber & self.FLAG_Safari == self.FLAG_Safari

    def check_suite_android(self):
        return self.suiteFlagNumber & self.FLAG_Android == self.FLAG_Android

    def check_suite_ios(self):
        return self.suiteFlagNumber & self.FLAG_Ios == self.FLAG_Ios

    def check_suite_suite(self):
        return self.suiteFlagNumber & self.FLAG_Suite == self.FLAG_Suite

    def check_suite_mobileapp(self):
        return self.suiteFlagNumber & self.FLAG_MobileApp == self.FLAG_MobileApp

    def check_suite_cloud(self):
        return self.suiteFlagNumber & self.FLAG_Cloud == self.FLAG_Cloud

    def check_suite_grid(self):
        return self.suiteFlagNumber & self.FLAG_Grid == self.FLAG_Grid

    def check_suite_local(self):
        return self.suiteFlagNumber & self.FLAG_Local == self.FLAG_Local

    # Flipping Bits  - To test the value of a flag, use bitwise AND:

    def flip_suite_prod(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Prod
        print("flip_suite_prod")

    def flip_suite_staging(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Staging
        print("flip_suite_staging")

    def flip_suite_email(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Email
        print("flip_suite_email")

    def flip_suite_chrome(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Chrome
        print("flip_suite_chrome")

    def flip_suite_firefox(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Firefox
        print("flip_suite_firefox")

    def flip_suite_edge(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Edge
        print("flip_suite_edge")

    def flip_suite_safari(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Safari
        print("flip_suite_safari")

    def flip_suite_android(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Android
        print("flip_suite_android")

    def flip_suite_ios(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Ios
        print("flip_suite_ios")

    def flip_suite_suite(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Suite
        print("flip_suite_suite")

    def flip_suite_mobileapp(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_MobileApp
        print("flip_suite_mobileapp")

    def flip_suite_cloud(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Cloud
        print("flip_suite_cloud")

    def flip_suite_grid(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Grid
        print("flip_suite_grid")

    def flip_suite_local(self):
        self.suiteFlagNumber = self.suiteFlagNumber & ~ self.FLAG_Local
        print("flip_suite_local")

    def flip_all_suite_bits(self):
        self.suiteFlagNumber = ~ self.suiteFlagNumber
        print("flip_suite_suite")

    def clear_all_suite_bits(self):
        self.suiteFlagNumber = 0
        print("clear_all_suite_bits")

    def configBuilder(self):
        my_config = Config()
        print("Configuration Builder")
        while True:
            action = input("Select to build a config? \n[P]roduction, [S]taging, [E]mail, \n[C]hrome, [F]irefox, "
                           "[V] IE Edge, \n[M] Safari, [A]ndroid, [I]os, [U] Suite, \n[B] MobileApp, [D] Cloud, "
                           "[G]rid  [L]ocal \n[Y] Clear Bits or \n[Z] Flip Bits \n [R]un Test ? " + "\n").upper()
            if action not in "PSECFVMAIUBDGLYZR" or len(action) != 1:
                print("I don't know how to do that")
                continue
            beforeBits = my_config.display_suite_bits()

            if action == 'P':
                # Prod
                if my_config.check_suite_staging():
                    my_config.flip_suite_staging()
                my_config.set_suite_prod()

            elif action == 'S':
                # Staging
                if my_config.check_suite_prod():
                    my_config.flip_suite_prod()

                my_config.set_suite_staging()

            elif action == 'E':
                # Email
                my_config.set_suite_email()

            elif action == 'C':

                # Chrome
                if my_config.check_suite_firefox():
                    my_config.flip_suite_firefox()

                if my_config.check_suite_edge():
                    my_config.flip_suite_edge()

                if my_config.check_suite_safari():
                    my_config.flip_suite_safari()

                if my_config.check_suite_ios():
                    my_config.flip_suite_ios()

                my_config.set_suite_chrome()

            elif action == 'F':
                # firefox
                if my_config.check_suite_chrome():
                    my_config.flip_suite_chrome()

                if my_config.check_suite_edge():
                    my_config.flip_suite_edge()

                if my_config.check_suite_safari():
                    my_config.flip_suite_safari()

                if my_config.check_suite_ios():
                    my_config.flip_suite_ios()

                my_config.set_suite_firefox()

            elif action == 'V':
                # Edge
                if my_config.check_suite_chrome():
                    my_config.flip_suite_chrome()

                if my_config.check_suite_firefox():
                    my_config.flip_suite_firefox()

                if my_config.check_suite_safari():
                    my_config.flip_suite_safari()

                if my_config.check_suite_ios():
                    my_config.flip_suite_ios()

                my_config.set_suite_edge()

            elif action == 'M':
                # Safari
                if my_config.check_suite_chrome():
                    my_config.flip_suite_chrome()

                if my_config.check_suite_firefox():
                    my_config.flip_suite_firefox()

                if my_config.check_suite_edge():
                    my_config.flip_suite_edge()

                if my_config.check_suite_android():
                    my_config.flip_suite_android()

                if not my_config.check_suite_ios():
                    my_config.flip_suite_ios()

                my_config.set_suite_safari()

            elif action == 'A':
                # Android Device

                if my_config.check_suite_safari():
                    my_config.flip_suite_safari()

                if my_config.check_suite_ios():
                    my_config.flip_suite_ios()

                if not my_config.check_suite_grid():
                    my_config.flip_suite_grid()

                my_config.set_suite_android()

            elif action == 'I':
                # Ios Device
                if my_config.check_suite_android():
                    my_config.flip_suite_android()

                if my_config.check_suite_chrome():
                    my_config.flip_suite_chrome()

                if my_config.check_suite_edge():
                    my_config.flip_suite_edge()

                if my_config.check_suite_chrome():
                    my_config.flip_suite_chrome()

                my_config.set_suite_ios()

            elif action == 'U':
                my_config.set_suite_suite()

            elif action == 'B':
                # Mobile Application
                # If it's a hybrid app it may have a browser defined to is.
                my_config.set_suite_mobileapp()

            elif action == 'D':
                # Cloud - Sauce Labs
                if my_config.check_suite_local():
                    my_config.flip_suite_local()

                if my_config.check_suite_grid():
                    my_config.flip_suite_grid()

                my_config.set_suite_cloud()

            elif action == 'G':
                # Grid
                if my_config.check_suite_local():
                    my_config.flip_suite_local()

                if my_config.check_suite_cloud():
                    my_config.flip_suite_cloud()

                my_config.set_suite_grid()

            elif action == 'L':
                # Local - Same computer as Jenkins
                if my_config.check_suite_grid():
                    my_config.flip_suite_grid()

                if my_config.check_suite_cloud():
                    my_config.flip_suite_cloud()

                my_config.set_suite_local()

            elif action == 'Y':
                my_config.clear_all_suite_bits()

            elif action == 'Z':
                my_config.flip_all_suite_bits()
            elif action == 'R':
                return my_config.suiteFlagNumber

            my_config.display_suite_config()
            print("Before : " + beforeBits)
            b = my_config.display_suite_bits()
            print("After  : " + b)
